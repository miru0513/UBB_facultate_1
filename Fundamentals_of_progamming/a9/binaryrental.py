import pickle
from datetime import datetime
from src.exceptions.exception_repo import RepositoryException
from src.repository.memreporental import RentalMemoryRepository

class BinaryRentalRepository(RentalMemoryRepository):
    """
    Binary file-based repository for managing rentals, extending the memory-based repository.
    """
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.load_file()

    def load_file(self):
        """
        Loads all rentals from the binary file into memory.
        If the file does not exist or is empty, it initializes an empty repository.
        """
        try:
            with open(self.file_name, 'rb') as input_file:
                rentals = pickle.load(input_file)
                for rental in rentals:
                    # If dates are stored as string, convert them back to datetime objects
                    if isinstance(rental['rented_date'], str):
                        rental['rented_date'] = datetime.strptime(rental['rented_date'], '%Y-%m-%d')
                    if isinstance(rental['returned_date'], str):
                        rental['returned_date'] = datetime.strptime(rental['returned_date'], '%Y-%m-%d')
                    self._rentals[rental['rental_id']] = rental
        except (IOError, EOFError):
            # If the file doesn't exist or is empty, start with an empty repository
            self._rentals = {}

    def save_file(self):
        """
        Saves all rentals to the binary file.
        This method ensures that the dates are formatted as strings before saving.
        """
        try:
            # Before saving, make sure the dates are converted to string if they are datetime objects
            for rental in self._rentals.values():
                if isinstance(rental['rented_date'], datetime):
                    rental['rented_date'] = rental['rented_date'].strftime('%Y-%m-%d')  # Convert datetime to string
                if isinstance(rental['returned_date'], datetime):
                    rental['returned_date'] = rental['returned_date'].strftime('%Y-%m-%d')  # Convert datetime to string

            with open(self.file_name, 'wb') as out_file:
                pickle.dump(list(self._rentals.values()), out_file)
        except IOError as e:
            raise RepositoryException(f"Error writing to file: {e}")

    def get_rental(self, rental_id):
        """
        Retrieves a rental by its ID, using the inherited method from RentalMemoryRepository.
        """
        return super().get_rental(rental_id)

    def is_book_rented(self, book_id):
        """
        Checks if a book is rented by any client, using the inherited method from RentalMemoryRepository.
        """
        return super().is_book_rented(book_id)

    def add_rental(self, rental_id, client_id, book_id, rented_date, returned_date):
        """
        Adds a new rental to the repository.
        After adding, it will save the updated rentals to the binary file.
        """
        super().add_rental(rental_id, client_id, book_id, rented_date, returned_date)
        self.save_file()  # Save to the file after adding the rental

    def remove_rental(self, rental_id):
        """
        Removes a rental from the repository by its unique ID.
        After removing, it will save the updated rentals to the binary file.
        """
        super().remove_rental(rental_id)
        self.save_file()  # Save to the file after removing the rental

    def list_rentals(self):
        """
        Lists all rentals in the repository, using the inherited method from RentalMemoryRepository.
        """
        return super().list_rentals()


    def list_rentals_for_book(self, book_id):
        super().list_rentals_for_book(book_id)

