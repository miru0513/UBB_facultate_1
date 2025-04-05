from src.domain.book import Book
from src.exceptions.exception_repo import RepositoryException
from src.repository.memrepobooks import InMemoryRepository


class TextFileRepository(InMemoryRepository):
    def __init__(self, file_name):
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
                        super().add_book(book)
            input_file.close()
        except FileNotFoundError:
            # If the file doesn't exist, we'll simply start with an empty repository
            pass

    def save_file(self):
        try:
            with open(self.file_name, 'wt') as out_file:
                for book in super().list_book():
                    book_string = f"{book.book_id},{book.title},{book.author}\n"
                    out_file.write(book_string)
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

    def update_book(self,book:Book):
        super().update_book(book)
        self.save_file()




