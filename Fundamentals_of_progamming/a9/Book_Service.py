import copy

from faker import Faker
from src.domain.book import Book
from src.exceptions.exception_service import ServiceException
from src.services.UndoService import FunctionCall
from src.services.UndoService import Operation

class BookService:
    def __init__(self, repo, undo_service, rental_repo):
        self.__repo = repo
        self._rentals_repo = rental_repo
        self.__undo_service = undo_service  # UndoService dependency

    def list_books_service(self):
        return self.__repo.list_book()

    def find_by_id_book_service(self, book_id):
        return self.__repo.find_by_id_book(book_id)

    def add_book_service(self, id, title, author):
        book = Book(id, title, author)
        self.__repo.add_book(book)

        # Define undo and redo actions for adding a book
        undo_action = FunctionCall(self.__repo.remove_book, id)
        redo_action = FunctionCall(self.__repo.add_book, book)

        # Record the undo/redo operation for the book
        operation = Operation(undo_action, redo_action)
        self.__undo_service.record(operation)

    def remove_book_service(self, id):
        """
        Removes a book from the repository, deleting any associated rentals first.
        If the book has active rentals, they will be deleted before the book is removed.
        """
        # Find the book by ID to ensure it exists
        book = self.__repo.find_by_id_book(id)
        if book is None:
            raise ServiceException(f"Book with ID {id} does not exist.\n")

        # Find all rentals associated with the book
        rentals_to_delete = [rental for rental in self._rentals_repo.list_rentals() if rental['book_id'] == id]

        # Prepare undo/redo actions for the book removal
        undo_book_action = FunctionCall(self.__repo.add_book, book)  # Undo: Add the book back
        redo_book_action = FunctionCall(self.__repo.remove_book, id)  # Redo: Remove the book

        # Prepare undo/redo actions for rentals removal
        undo_rentals = []
        redo_rentals = []

        # If there are related rentals, prepare the actions
        if rentals_to_delete:
            for rental in rentals_to_delete:
                # Undo: Add rental back
                undo_rentals.append(
                    FunctionCall(self._rentals_repo.add_rental, rental['rental_id'], rental['client_id'],
                                 rental['book_id'], rental['rented_date'], rental['returned_date'])
                )
                # Redo: Remove the rental
                redo_rentals.append(FunctionCall(self._rentals_repo.remove_rental, rental['rental_id']))

            # Perform the cascading delete for rentals
            for rental in rentals_to_delete:
                self._rentals_repo.remove_rental(rental['rental_id'])


        # Perform the book removal
        self.__repo.remove_book(id)

        # Record undo/redo actions for the book and the rentals
        operation = Operation(undo_book_action, redo_book_action)

        # Add cascading undo/redo actions for the rentals
        for undo_rental, redo_rental in zip(undo_rentals, redo_rentals):
            operation.add_cascade(undo_rental, redo_rental)

        # Record the operation in UndoService
        self.__undo_service.record(operation)

    def update_book_service(self, id, title, author):
        # Updates a book in the repository and records the undo/redo operations
        old_book = self.__repo.find_by_id_book(id)

        if old_book is None:
            raise ServiceException(f"Book with ID {id} does not exist.\n")

        updated_book = Book(id, title, author)
        old_old_book = copy.deepcopy(old_book)
        self.__repo.update_book(updated_book)

        # Define undo/redo actions for the book itself
        undo_action = FunctionCall(self.__repo.update_book, old_old_book)
        redo_action = FunctionCall(self.__repo.add_book, updated_book)

        # Record the operation in UndoService
        operation = Operation(undo_action, redo_action)
        self.__undo_service.record(operation)

    def search_books(self, query):
        """
        Searches for books using a case-insensitive, partial match for id, title, or author.
        :param query: The search query string.
        :return: A list of books that match the query.
        """
        query = query.lower()
        return [
            book for book in self.__repo.list_book()
            if query in str(book.book_id).lower() or
               query in book.title.lower() or
               query in book.author.lower()
        ]

    def most_rented_books_service(self):
        """
        Provides the list of books sorted by the number of times they were rented in descending order.
        :return: List of tuples (book, rental_count), sorted by rental_count in descending order.
        """

        rental_counts = {}
        for rental in self._rentals_repo.list_rentals():
            book_id = rental['book_id']
            if book_id not in rental_counts:
                rental_counts[book_id] = 0
            rental_counts[book_id] += 1

        sorted_books = sorted(
            rental_counts.items(),
            key=lambda item: item[1],
            reverse=True
        )


        result = []
        for book_id, rental_count in sorted_books:
            book = self.__repo.find_by_id_book(book_id)
            if book:
                result.append((book, rental_count))

        return result

    def most_rented_author_service(self):
        """
        Returns the list of authors sorted by the number of times their books have been rented.
        """

        book_rental_counts = {}
        for rental in self._rentals_repo.list_rentals():
            book_id = rental['book_id']
            if book_id in book_rental_counts:
                book_rental_counts[book_id] += 1
            else:
                book_rental_counts[book_id] = 1


        author_rental_counts = {}
        for book_id, rental_count in book_rental_counts.items():
            book = self.__repo.find_by_id_book(book_id)
            if book:
                author = book.author
                if author in author_rental_counts:
                    author_rental_counts[author] += rental_count
                else:
                    author_rental_counts[author] = rental_count


        sorted_authors = sorted(author_rental_counts.items(), key=lambda x: x[1], reverse=True)

        # Step 4: Prepare the result as a list of dictionaries
        most_rented_authors = [{'author': author, 'total_rentals': total_rentals} for author, total_rentals in sorted_authors]

        return most_rented_authors