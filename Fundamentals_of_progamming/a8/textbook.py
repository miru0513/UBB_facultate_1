from src.domain.book import Book
from src.repository.memrepobooks import InMemoryRepository


class TextFileRepository(InMemoryRepository):
    def __init__(self, file_name='books.txt'):
        super().__init__()
        self.file_name=file_name
        self.load_file()

    def load_file(self):
        try:
            with open(self.file_name, 'rt') as input_file:
                for line in input_file.readlines():
                    properties = line.strip().split(',')
                    if len(properties) == 3:
                        book = Book(properties[0], properties[1], properties[2])
                        super().add(book)
        except FileNotFoundError:
            # If the file doesn't exist, we'll simply start with an empty repository
            pass

    def save_file(self):
        try:
            with open(self.file_name, 'wt') as out_file:
                for book in super().list():
                    book_string = f"{book.book_id},{book.title},{book.author}\n"
                    out_file.write(book_string)
        except IOError as e:
            raise ValueError(f"Error writing to file: {e}")

    def add(self, new_book: Book):
        super().add(new_book)
        self.save_file()

    def remove(self, book_id: str):
        book_to_remove=self.find_by_id(book_id)
        if book_to_remove is None:
            raise ValueError("Book with the given ID does not exist.")
        super().remove(book_id)
        self.save_file()

    def update(self,book:Book):
        book_to_update=self.find_by_id(book.book_id)
        if book_to_update is None:
            raise ValueError("Book with the given ID does not exist.")
        book_to_update.title = book.title
        book_to_update.author = book.author
        self.save_file()

    def is_rented(self, book_id):
        """Checks if a book is currently rented."""
        for rental in self._data:
            # Assuming each rental record is a dictionary with 'book_id' and 'returned' keys
            if rental.get("book_id") == book_id and not rental.get("returned", True):
                return True
        return False

    def find_by_id(self, book_id):
        """
        Finds a book in the repository by its ID.
        :param book_id: The ID of the book to find.
        :return: The book with the matching ID, or None if not found.
        """
        for book in self.__repo.list():
            if book.book_id == book_id:
                return book
        return None


