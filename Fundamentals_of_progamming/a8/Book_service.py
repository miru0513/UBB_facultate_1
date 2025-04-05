from faker import Faker

from src.domain.book import Book


class BookService:
   def __init__(self,repo):
       self.__repo=repo

   def add_book(self,id,title,author):
        book=Book(id,title,author)
        self.__repo.add(book)

   def list_books(self):
        return self.__repo.list()

   def remove_book(self,id):
        self.__repo.remove(id)

   def update_book(self,id,tile,author):
       book=Book(id,tile,author)
       self.__repo.update(book)

   def generate_books(self, number_of_books: int):
       """
       Generates a specified number of random books and adds them to the repository.
       :param number_of_books: The number of books to generate.
       """
       fake = Faker()
       for _ in range(number_of_books):
           book_id = fake.unique.random_int(min=10000, max=99999)  # Unique 5-digit book ID
           title = fake.sentence(nb_words=4)  # Random book title with 4 words
           author = fake.name()  # Random author name
           self.add_book(book_id, title, author)

   def search_books(self, query):
       """
       Searches for books using a case-insensitive, partial match for id, title, or author.
       :param query: The search query string.
       :return: A list of books that match the query.
       """
       query = query.lower()
       return [
           book for book in self.__repo.list()
           if query in str(book.book_id).lower() or
              query in book.title.lower() or
              query in book.author.lower()
       ]

   def find_by_id(self, book_id):
       """
       Finds a book in the repository by its ID.
       :param book_id: The ID of the book to find.
       :return: The book with the matching ID, or None if not found.
       """
       for book in self.__repo.list():
           #print(book_id)
           if book.book_id == book_id:
               return book
       return None
