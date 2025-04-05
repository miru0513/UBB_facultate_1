import random
from datetime import datetime, timedelta
from faker import Faker

from src.services.UndoService import FunctionCall
from src.services.UndoService import Operation
from src.exceptions.exception_service import ServiceException


class RentalService:
    def __init__(self, rental_repo, book_service, clients_service, undo_service):
        self._rental_repo = rental_repo  # The repository can be in-memory or other types
        self._book_service = book_service
        self._clients_service = clients_service
        self._undo_service = undo_service

    def add_rental(self, rental_id, client_id, book_id, rented_date, returned_date):
        """
        Add a new rental and record undo/redo operations.
        """
        self._rental_repo.add_rental(rental_id, client_id, book_id, rented_date, returned_date)

        # Define undo and redo actions
        undo_action = FunctionCall(self._rental_repo.remove_rental, rental_id)
        redo_action = FunctionCall(
            self._rental_repo.add_rental, rental_id, client_id, book_id, rented_date, returned_date
        )

        # Record the operation in UndoService
        operation = Operation(undo_action, redo_action)
        self._undo_service.record(operation)

    def return_book(self, rental_id):
        """
        Return a book by removing a rental and record undo/redo operations.
        """
        rental = self._rental_repo.get_rental(rental_id)
        if rental is None:
            raise ValueError(f"Rental with ID {rental_id} does not exist.\n")

        # Remove the rental
        self._rental_repo.remove_rental(rental_id)

        # Define undo and redo actions
        undo_action = FunctionCall(
            self._rental_repo.add_rental, rental.rental_id, rental.client_id, rental.book_id, rental.rented_date, rental.return_date
        )
        redo_action = FunctionCall(self._rental_repo.remove_rental, rental_id)

        # Record the operation in UndoService
        operation = Operation(undo_action, redo_action)
        self._undo_service.record(operation)

    def get_rental(self, rental_id):
        """
        Retrieve a rental by its ID.
        """
        return self._rental_repo.get_rental(rental_id)

    def list_rentals(self):
        """
        List all rentals in the repository.
        """
        return self._rental_repo.list_rentals()

    def is_book_rented(self, book_id):
        """
        Check if a book is currently rented.
        """
        return self._rental_repo.is_book_rented(book_id)

    def generate_rentals(self, number_of_clients: int):
        """
        Generate rentals with random dates for rented_date and returned_date,
        ensuring books are not already rented. Records undo/redo for each generated rental.
        """
        for _ in range(number_of_clients):
            # Get list of books and clients using the provided services
            books = self._book_service.list_books_service()
            clients = self._clients_service.list_clients_service()

            if not books or not clients:
                raise ServiceException("Cannot generate rental. No books or clients available.")

            # Convert dict_values to list for random selection
            books_list = list(books)
            clients_list = list(clients)

            # Filter out books that are already rented
            available_books = [book for book in books_list if not self._rental_repo.is_book_rented(book.book_id)]

            if not available_books:
                raise ServiceException("No available books for rental.")

            # Randomly select a book and a client from the available lists
            selected_book = random.choice(available_books)
            selected_client = random.choice(clients_list)

            fake = Faker()

            # Ensure rental_id is unique
            rental_id = fake.unique.random_int(min=100, max=999)
            while any(rental['rental_id'] == rental_id for rental in self._rental_repo.list_rentals()):
                rental_id = fake.unique.random_int(min=100, max=999)  # Regenerate ID if it exists

            book_id = selected_book.book_id
            client_id = selected_client.client_id

            # Generate random rented date (from 30 days ago to today)
            rented_date = datetime.now() - timedelta(days=random.randint(1, 30))

            # Generate random returned date (from 1 to 14 days after rented_date)
            returned_date = rented_date + timedelta(days=random.randint(1, 14))

            # Add rental and record undo/redo
            self.add_rental(rental_id, client_id, book_id, rented_date, returned_date)

    def remove_rentals_for_book(self, book_id):
        """
        Removes all rentals related to a specific book.
        :param book_id: The ID of the book whose related rentals need to be removed.
        """
        rentals_to_remove = [rental for rental in self._rental_repo if rental.book_id == book_id]
        for rental in rentals_to_remove:
            self._rental_repo.remove_rental(rental.rental_id)  # This method handles the removal of individual rentals