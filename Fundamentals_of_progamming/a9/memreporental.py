from datetime import datetime
from src.exceptions.exception_repo import RepositoryException

class RentalMemoryRepository:
    def __init__(self):
        self._rentals = {}

    def get_rental(self, rental_id):
        """
        Retrieve a rental by its ID.
        :param rental_id: Unique ID of the rental
        :return: The rental dictionary if found, None otherwise
        """
        return self._rentals.get(int(rental_id), None)

    def list_rentals(self):
        """
        List all rentals in the repository.
        :return: A collection (list) of all rental objects
        """
        return list(self._rentals.values())

    def is_book_rented(self, book_id):
        """
        Check if a book is currently rented.
        :param book_id: Unique ID of the book
        :return: True if the book is rented, False otherwise
        """
        for rental in self._rentals.values():
            if rental['book_id'] == book_id:
                return True
        return False

    from datetime import datetime

    def add_rental(self, rental_id, client_id, book_id, rented_date, returned_date):
        """
        Add a new rental to the repository.
        :param rental_id: Unique ID of the rental
        :param client_id: Unique ID of the client
        :param book_id: Unique ID of the book
        :param rented_date: The date the rental starts (datetime object or string)
        :param returned_date: The date the rental ends (datetime object or string)
        :raises RepositoryException: If a rental with the given ID already exists
        """
        rental_id = int(rental_id)

        # Check if the rental already exists
        if rental_id in self._rentals:
            raise RepositoryException(f"Rental with ID {rental_id} already exists.")

        # Ensure rented_date and returned_date are datetime objects
        if isinstance(rented_date, str):
            rented_date = datetime.strptime(rented_date, '%Y-%m-%d')  # Convert string to datetime object

        if isinstance(returned_date, str):
            returned_date = datetime.strptime(returned_date, '%Y-%m-%d')  # Convert string to datetime object

        # Create the rental object to be added
        rental = {
            'rental_id': rental_id,
            'client_id': client_id,
            'book_id': book_id,
            'rented_date': rented_date.strftime('%Y-%m-%d'),  # Now safely call strftime() on datetime object
            'returned_date': returned_date.strftime('%Y-%m-%d')  # Same for returned_date
        }

        # Add the rental to the repository
        self._rentals[rental_id] = rental

    def remove_rental(self, rental_id):
        """
        Remove a rental by its ID.
        :param rental_id: Unique ID of the rental to remove
        :raises RepositoryException: If the rental ID does not exist
        """
        rental_id = int(rental_id)  # Ensure rental_id is an integer
        if rental_id not in self._rentals:
            raise RepositoryException(f"Rental with ID {rental_id} does not exist.")

        del self._rentals[rental_id]

    def list_rentals_for_book(self, book_id):
        """
        Returns all rentals associated with the given book_id.
        """
        rentals = list(self._rentals.values())  # Get all rentals from the repository
        # Filter and return only the rentals that match the given book_id
        return [rental for rental in rentals if rental['book_id'] == book_id] or []