from src.domain.book import Book


class InMemoryRepository:
    def __init__(self):
        self._data = {}

    def add(self,book:Book) :
        if book.book_id in  self._data:
            raise ValueError("Book with this id already exists.")
        self._data[book.book_id] = book

    def remove(self,book_id:str):
        if book_id not in self._data:
            raise ValueError("Book with this id doesn't exist.")
        del self._data[book_id]

    def update(self,book:Book):
        if book.book_id not in self._data:
            raise ValueError("Book with this id doesn't exist.")
        self._data[book.book_id] = book

    def list(self):
        return self._data.values()

    def find_by_id(self,book_id):
        return self._data.get(book_id,None)

