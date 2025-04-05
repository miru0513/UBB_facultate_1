from src.domain.book import Book
from src.exceptions.exception_repo import RepositoryException

class InMemoryRepository:
    def __init__(self):
        self._data = {}

    def list_book(self):
        return self._data.values()

    def find_by_id_book(self, book_id):
        """
        Find a book by its ID.
        :param book_id: The ID of the book to find
        :return: The book object if found, None otherwise
        """
        book_id = str(book_id)
        return self._data.get(book_id, None)

    def add_book(self, book: Book):
        """
        Add a book to the repository.
        :param book: Book object to add
        :raises RepositoryException: If the book ID already exists
        """
        book_id = str(book.book_id)
        if book_id in self._data:
            raise RepositoryException("Book with this id already exists.")
        self._data[book_id] = book

    def remove_book(self, book_id):
        """
        Remove a book by its ID.
        :param book_id: The ID of the book to remove
        :raises RepositoryException: If the book ID does not exist
        """
        book_id = str(book_id)
        if book_id not in self._data:
            raise RepositoryException(f"Book with ID {book_id} does not exist.")
        del self._data[book_id]

    def update_book(self, book: Book):
        """
        Update a book's details.
        :param book: Book object with updated details
        :raises RepositoryException: If the book ID does not exist
        """
        book_id = str(book.book_id)
        book_to_update = self.find_by_id_book(book_id)
        if book_to_update is None:
            raise RepositoryException("Book with the given ID does not exist.")

        # Update the existing book's attributes
        book_to_update.title = book.title
        book_to_update.author = book.author



