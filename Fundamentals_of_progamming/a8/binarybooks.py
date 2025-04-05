import pickle

from src.domain.book import Book
from src.repository.memrepobooks import InMemoryRepository


class BinaryFileRepository(InMemoryRepository):
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
                # Explicitly convert to list to avoid `dict_values` serialization error
                pickle.dump(list(self.list()), out_file)
        except IOError as e:
            raise ValueError(f"Error writing to file: {e}")

    def remove(self, book_id: str):
        super().remove(book_id)
        self.save_file()




