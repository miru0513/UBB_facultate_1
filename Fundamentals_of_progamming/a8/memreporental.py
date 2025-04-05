class RentalMemoryRepository:
    """
    In-memory repository for managing rentals.
    This class stores rental information in memory for easy access and manipulation.
    """

    def __init__(self):
        # Initialize the in-memory storage as a dictionary
        self._rentals = {}

    def add_rental(self, rental_id, client_id, book_id):
        if rental_id in self._rentals:
            raise ValueError(f"Rental with ID {rental_id} already exists.")

        # Each rental entry is stored as a dictionary
        self._rentals[rental_id] = {
            'rental_id': rental_id,
            'client_id': client_id,
            'book_id': book_id
        }

    def get_rental(self, rental_id):
        """
        Retrieves a rental by its ID.
        :param rental_id: Unique ID of the rental
        :return: Rental data
        """
        return self._rentals.get(rental_id, None)

    def update_rental(self, rental_id, rental_data):
        """
        Updates an existing rental in the repository.
        :param rental_id: Unique ID of the rental
        :param rental_data: Updated rental details
        """
        if rental_id not in self._rentals:
            raise ValueError(f"Rental with ID {rental_id} does not exist.")
        self._rentals[rental_id] = rental_data

    def remove_rental(self, rental_id:int):
        """
        Deletes a rental by its ID.
        :param rental_id: Unique ID of the rental
        """
        if rental_id not in self._rentals:
            raise ValueError(f"Rental with ID {rental_id} does not exist.")
        del self._rentals[rental_id]

    def list_all_rentals(self):
        """
        Lists all rentals in the repository.
        :return: A list of all rental records.
        """
        return list(self._rentals.values())

    def is_rented(self, book_id:int):
        """
        Checks if a book is currently rented.
        :param book_id: ID of the book to check.
        :return: True if the book is rented, False otherwise.
        """
        for rental in self._rentals.values():  # Iterate over all rentals
            if rental['book_id'] == book_id:
                return True
        return False