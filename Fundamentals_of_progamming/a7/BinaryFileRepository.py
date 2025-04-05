import pickle

from src.domain.entities import Book
from src.repository.MemoryRepository import MemoryRepo


class BinaryFileRepo(MemoryRepo):
    def __init__(self, file_name='file.bin'):
        super().__init__()
        self.file_name = file_name
        self.load_file()

    def add(self, book: Book):
        super().add(book)
        self.save_file()

    def load_file(self):
        try:
            with open(self.file_name, 'rb') as input_file:
                books = pickle.load(input_file)
                for book in books:
                    super().add(book)
        except (IOError, EOFError):
            # If the file doesn't exist or is empty, we'll start with an empty repository.
            pass

    def save_file(self):
        try:
            with open(self.file_name, 'wb') as out_file:
                pickle.dump(self.get_all(), out_file)
        except IOError as e:
            raise ValueError(f"Error writing to file: {e}")

    def remove_by_isbn(self, isbn: str):
        super().remove(isbn)
        self.save_file()
