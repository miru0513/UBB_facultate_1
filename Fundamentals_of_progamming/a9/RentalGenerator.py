import random
from datetime import datetime, timedelta
from faker import Faker

from src.exceptions.exception_service import ServiceException

class RentalGenerator:
    def __init__(self, book_service, client_service, rental_service):
        self._book_service = book_service
        self._client_service = client_service
        self._rental_service = rental_service
        self.fake = Faker()

    def generate_rentals(self, number_of_rentals: int):
        """
        Generate rentals for a specified number of clients.
        This will handle generating unique rental IDs, randomly selecting books and clients,
        ensuring books are available, and generating rental and return dates.
        """
        for _ in range(number_of_rentals):
            # Get available books and clients
            books = self._book_service.list_books_service()
            clients = self._client_service.list_clients_service()

            if not books or not clients:
                raise ServiceException("Cannot generate rental. No books or clients available.")

            # Filter out books that are already rented
            available_books = [book for book in books if not self._rental_service.is_book_rented(book.book_id)]

            if not available_books:
                raise ServiceException("No available books for rental.")

            # Randomly select a book and a client from the available lists
            selected_book = random.choice(available_books)
            selected_client = random.choice(list(clients))

            # Generate unique rental ID
            rental_id = self.fake.unique.random_int(min=100, max=999)
            while any(rental['rental_id'] == rental_id for rental in self._rental_service.list_rentals()):
                rental_id = self.fake.unique.random_int(min=100, max=999)

            # Generate random rented and returned dates
            rented_date = datetime.today() - timedelta(days=random.randint(1, 30))
            returned_date = rented_date + timedelta(days=random.randint(1, 14))

            # Add rental to the repository
            self._rental_service.add_rental(rental_id, selected_client.client_id, selected_book.book_id, rented_date, returned_date)