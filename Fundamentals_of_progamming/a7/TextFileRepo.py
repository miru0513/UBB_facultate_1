from src.domain.entities import Book
from src.repository.MemoryRepository import MemoryRepo


class TextFileRepo(MemoryRepo):

    def __init__(self, file_name='file.txt'):
        super().__init__()
        self.file_name = file_name
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
                for book in super().get_all():
                    book_string = f"{book.isbn},{book.author},{book.title}\n"
                    out_file.write(book_string)
        except IOError as e:
            raise ValueError(f"Error writing to file: {e}")

    def add(self, new_book: Book):

        super().add(new_book)
        self.save_file()       # Save changes to file

    def remove_by_isbn(self, isbn: str):
        book_to_remove = self.find_by_isbn(isbn)
        if book_to_remove is None:
            raise ValueError("Book with the given ISBN does not exist!")
        super().remove(isbn)
        self.save_file()


