import pickle
from src.domain.entities import Book
from src.repository.BinaryFileRepository import BinaryFileRepo
from src.repository.MemoryRepository import MemoryRepo
import os
from src.repository.TextFileRepo import TextFileRepo
from src.domain.entities import Book
from src.services.Service import BookService


class TestMemoryRepo:
    def __init__(self):
        self.repo = MemoryRepo()

    def run_tests(self):
        results = []
        results.append(self.test_add_book())
        results.append(self.test_get_all_books())
        results.append(self.test_find_by_isbn())
        self.log_results(results)

    def test_add_book(self):
        try:
            book = Book("1234567890", "Author A", "Title A")
            self.repo.add(book)
            books = self.repo.get_all()
            if len(books) == 1 and books[0].isbn == "1234567890":
                return "test_add_book: PASSED"
            return "test_add_book: FAILED"
        except Exception as e:
            return f"test_add_book: FAILED with error {e}"

    def test_get_all_books(self):
        try:
            book1 = Book("1234567890", "Author A", "Title A")
            book2 = Book("0987654321", "Author B", "Title B")
            self.repo.add(book1)
            self.repo.add(book2)
            books = self.repo.get_all()
            if len(books) == 2 and all(b.isbn in ["1234567890", "0987654321"] for b in books):
                return "test_get_all_books: PASSED"
            return "test_get_all_books: FAILED"
        except Exception as e:
            return f"test_get_all_books: FAILED with error {e}"

    def test_find_by_isbn(self):
        try:
            book = Book("1234567890", "Author A", "Title A")
            self.repo.add(book)
            found = self.repo.find_by_isbn("1234567890")
            if found and found.isbn == "1234567890":
                return "test_find_by_isbn: PASSED"
            return "test_find_by_isbn: FAILED"
        except Exception as e:
            return f"test_find_by_isbn: FAILED with error {e}"

    @staticmethod
    def log_results(results):
        for result in results:
            print(result)

import os
from src.domain.entities import Book
from src.repository.TextFileRepo import TextFileRepo


class TestTextFileRepo:
    def __init__(self):
        self.test_file = "test_file.txt"
        self.repo = TextFileRepo(self.test_file)

    def run_tests(self):
        results = []
        results.append(self.test_add_book())
        results.append(self.test_remove_book())
        results.append(self.test_load_file())
        self.cleanup()
        self.log_results(results)

    def cleanup(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        try:
            book = Book("1234567890", "Author A", "Title A")
            self.repo.add(book)
            books = self.repo.get_all()
            with open(self.test_file, 'r') as file:
                content = file.read().strip()
            if len(books) == 1 and books[0].isbn == "1234567890" and content == "1234567890,Author A,Title A":
                return "test_add_book: PASSED"
            return "test_add_book: FAILED"
        except Exception as e:
            return f"test_add_book: FAILED with error {e}"

    def test_remove_book(self):
        try:
            book1 = Book("1234567890", "Author A", "Title A")
            book2 = Book("0987654321", "Author B", "Title B")
            self.repo.add(book1)
            self.repo.add(book2)
            self.repo.remove_by_isbn("1234567890")
            books = self.repo.get_all()
            with open(self.test_file, 'r') as file:
                content = file.read().strip()
            if len(books) == 1 and books[0].isbn == "0987654321" and content == "0987654321,Author B,Title B":
                return "test_remove_book: PASSED"
            return "test_remove_book: FAILED"
        except Exception as e:
            return f"test_remove_book: FAILED with error {e}"

    def test_load_file(self):
        try:
            with open(self.test_file, 'w') as file:
                file.write("1234567890,Author A,Title A\n")
                file.write("0987654321,Author B,Title B\n")
            self.repo = TextFileRepo(self.test_file)
            books = self.repo.get_all()
            if len(books) == 2 and all(b.isbn in ["1234567890", "0987654321"] for b in books):
                return "test_load_file: PASSED"
            return "test_load_file: FAILED"
        except Exception as e:
            return f"test_load_file: FAILED with error {e}"

    @staticmethod
    def log_results(results):
        for result in results:
            print(result)





class TestBinaryFileRepo:
    def __init__(self):
        self.test_file = "test_file.bin"
        self.repo = BinaryFileRepo(self.test_file)

    def run_tests(self):
        results = []
        results.append(self.test_add_book())
        results.append(self.test_remove_book())
        results.append(self.test_load_file())
        self.cleanup()
        self.log_results(results)

    def cleanup(self):
        # Remove the test file after running the tests
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        try:
            book = Book("1234567890", "Author A", "Title A")
            self.repo.add(book)
            books = self.repo.get_all()
            if len(books) == 1 and books[0].isbn == "1234567890":
                # Check if data is persisted in the binary file
                with open(self.test_file, 'rb') as file:
                    saved_books = pickle.load(file)
                if len(saved_books) == 1 and saved_books[0].isbn == "1234567890":
                    return "test_add_book: PASSED"
            return "test_add_book: FAILED"
        except Exception as e:
            return f"test_add_book: FAILED with error {e}"

    def test_remove_book(self):
        try:
            book1 = Book("1234567890", "Author A", "Title A")
            book2 = Book("0987654321", "Author B", "Title B")
            self.repo.add(book1)
            self.repo.add(book2)
            self.repo.remove_by_isbn("1234567890")
            books = self.repo.get_all()
            if len(books) == 1 and books[0].isbn == "0987654321":
                # Check if data is updated in the binary file
                with open(self.test_file, 'rb') as file:
                    saved_books = pickle.load(file)
                if len(saved_books) == 1 and saved_books[0].isbn == "0987654321":
                    return "test_remove_book: PASSED"
            return "test_remove_book: FAILED"
        except Exception as e:
            return f"test_remove_book: FAILED with error {e}"

    def test_load_file(self):
        try:
            # Manually create a binary file with some test data
            books = [
                Book("1234567890", "Author A", "Title A"),
                Book("0987654321", "Author B", "Title B")
            ]
            with open(self.test_file, 'wb') as file:
                pickle.dump(books, file)

            # Reload the repository to test loading from the binary file
            self.repo = BinaryFileRepo(self.test_file)
            loaded_books = self.repo.get_all()
            if len(loaded_books) == 2 and all(b.isbn in ["1234567890", "0987654321"] for b in loaded_books):
                return "test_load_file: PASSED"
            return "test_load_file: FAILED"
        except Exception as e:
            return f"test_load_file: FAILED with error {e}"

    @staticmethod
    def log_results(results):
        for result in results:
            print(result)


TestBinaryFileRepo().run_tests()
TestTextFileRepo().run_tests()
TestMemoryRepo().run_tests()
