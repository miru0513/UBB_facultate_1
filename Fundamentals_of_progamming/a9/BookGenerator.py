import random

class BookGenerator:
    def __init__(self, book_service, book_titles, authors):
        self._book_service = book_service
        self.book_titles = book_titles
        self.authors = authors
        self.used_book_ids = set()  # To ensure unique book IDs
        self.used_book_titles = set()  # To ensure unique book titles

    def generate_unique_book_id(self):
        """Generates a unique 3-digit random book ID."""
        while True:
            book_id = random.randint(100, 999)
            if book_id not in self.used_book_ids:
                self.used_book_ids.add(book_id)
                return book_id

    def generate_unique_book_title(self):
        """Generates a unique book title."""
        while True:
            title = random.choice(self.book_titles)
            if title not in self.used_book_titles:
                self.used_book_titles.add(title)
                return title

    def generate_books(self, number_of_books):
        """Generates a list of unique books with random IDs and titles. Authors can repeat."""
        books = []
        for _ in range(number_of_books):
            book_id = self.generate_unique_book_id()
            title = self.generate_unique_book_title()
            author = random.choice(self.authors)  # Same author can appear multiple times
            self._book_service.add_book_service( book_id, title, author)
