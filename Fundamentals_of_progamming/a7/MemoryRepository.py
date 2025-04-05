
from src.domain.entities import Book


class MemoryRepo:
    def __init__(self):
        self._data = {}

    def add(self, book: Book):
        if book.isbn in self._data:
            raise ValueError("Book with this ISBN already exists!")
        self._data[book.isbn] = book


    def remove(self, isbn: str):
        if isbn not in self._data:
            raise ValueError("Book with this ISBN does not exist!")
        del self._data[isbn]


    def get_all(self):
        return list(self._data.values())


    def find_by_isbn(self, isbn: str):
        return self._data.get(isbn, None)


