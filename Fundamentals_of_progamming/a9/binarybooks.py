import pickle

from src.domain.book import Book
from src.exceptions.exception_repo import RepositoryException
from src.repository.memrepobooks import InMemoryRepository


class BinaryFileRepository(InMemoryRepository):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.load_file()

    def load_file(self):
        try:
            with open(self.file_name, 'rb') as input_file:
                books = pickle.load(input_file)
                for book in books:
                    super().add_book(book)
        except (IOError, EOFError):
            # If the file doesn't exist or is empty, we'll start with an empty repository.
            pass

    def save_file(self):
        try:
            with open(self.file_name, 'wb') as out_file:
                # Explicitly convert to list to avoid `dict_values` serialization error
                pickle.dump(list(self.list_book()), out_file)
            out_file.close()
        except IOError as e:
            raise RepositoryException(f"Error writing to file: {e}")

    def list_book(self):
        return super().list_book()

    def find_by_id_book(self, book_id):
        return super().find_by_id_book(book_id)

    def add_book(self, new_book: Book):
        super().add_book(new_book)
        self.save_file()

    def remove_book(self, book_id: str):
        super().remove_book(book_id)
        self.save_file()

    def update_book(self, book: Book):
        super().update_book(book)
        self.save_file()



