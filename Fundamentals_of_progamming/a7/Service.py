from src.domain.entities import Book
import random

class BookService:
    def __init__(self, repo, textReporo, binaryRepo):
        """
            Initializes the BookService with three types of repositories.
            :param repo: General repository for storing books.
            :param textReporo: Text-based repository for storing books.
            :param binaryRepo: Binary-based repository for storing books.
        """
        self.__repo = repo
        self.__textReporo = textReporo
        self.__binaryRepo= binaryRepo
        self.__undo_stack = []

    def add_book(self, isbn: str, author: str, title: str,x):
        """
        Adds a book to the specified repository.
        :param isbn: The ISBN of the book (string).
        :param author: The author of the book (string).
        :param title: The title of the book (string).
        :param x: The repository type (1 for general, 2 for text, 3 for binary).
        """
        book = Book(isbn, author, title)
        if x== 1:
            self.__repo.add(book)
        elif x== 2:
            self.__textReporo.add(book)
        elif x== 3:
            self.__binaryRepo.add(book)
        self.__undo_stack.append(('add', isbn))

    def get_all_books(self, x):
        """
            Retrieves all books from the specified repository.
            :param x: The repository type (1 for general, 2 for text, 3 for binary).
            :return: A list of all books in the specified repository.
        """
        if x == 1:
            return self.__repo.get_all()
        elif x == 2:
            return self.__textReporo.get_all()
        elif x == 3:
            return self.__binaryRepo.get_all()

    def filter_books_by_title(self, prefix: str, x):
        """
            Removes books with titles starting with the specified prefix.
            :param prefix: The prefix to match titles against (string).
            :param x: The repository type (1 for general, 2 for text, 3 for binary).
        """
        books_to_remove = []
        if x == 1:
            books_to_remove = [book for book in self.__repo.get_all() if book.title.startswith(prefix)]
            for book in books_to_remove:
                self.__repo.remove(book.isbn)
        elif x == 2:
            books_to_remove = [book for book in self.__textReporo.get_all() if book.title.startswith(prefix)]
            for book in books_to_remove:
                self.__textReporo.remove_by_isbn(book.isbn)
        elif x == 3:
            books_to_remove = [book for book in self.__binaryRepo.get_all() if book.title.startswith(prefix)]
            for book in books_to_remove:
                self.__binaryRepo.remove_by_isbn(book.isbn)
        self.__undo_stack.append(('filter', books_to_remove, x))


    def undo(self, x):
        """
        :param x: The repository type (1 for general, 2 for text, 3 for binary).
        :raises ValueError: If no actions are available to undo.
        """
        if not self.__undo_stack:
            raise ValueError("No actions to undo!")

        last_action = self.__undo_stack.pop()

        if last_action[0] == 'add':
            if x == 1:
                self.__repo.remove(last_action[1])
            elif x == 2:
                self.__textReporo.remove_by_isbn(last_action[1])  # Use remove or remove_by_isbn
            elif x == 3:
                self.__binaryRepo.remove_by_isbn(last_action[1])
        elif last_action[0] == 'filter':
            for book in last_action[1]:  # Restore books
                if x == 1:
                    self.__repo.add(book)
                elif x == 2:
                    self.__textReporo.add(book)
                elif x == 3:
                    self.__binaryRepo.add(book)

    def generate_books(self, number_of_books: int, repo_type: int):
        """
            Generates a specified number of random books and adds them to the specified repository.
             :param number_of_books: The number of books to generate (int).
            :param repo_type: The repository type (1 for general, 2 for text, 3 for binary).
        """
        isbns = [str(x).zfill(5) for x in range(10000, 10000 + 1000)]
        authors = ['John Steinbeck', 'Harper Lee', 'George Orwell', 'J.K. Rowling', 'J.R.R. Tolkien',
                   'Ernest Hemingway',
                   'F. Scott Fitzgerald', 'Mark Twain', 'Jane Austen', 'Emily Bronte']
        titles = ['The Grapes of Wrath', 'To Kill a Mockingbird', '1984', 'Harry Potter', 'The Hobbit',
                  'The Old Man and the Sea', 'The Great Gatsby', 'Adventures of Huckleberry Finn',
                  'Pride and Prejudice',
                  'Wuthering Heights']

        for _ in range(number_of_books):
            isbn = random.choice(isbns)
            author = random.choice(authors)
            title = random.choice(titles)
            book = Book(isbn, author, title)

            if repo_type == 1:
                self.__repo.add(book)
            elif repo_type == 2:
                self.__textReporo.add(book)
            elif repo_type == 3:
                self.__binaryRepo.add(book)

