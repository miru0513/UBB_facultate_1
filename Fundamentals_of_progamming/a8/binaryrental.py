import pickle
from src.repository.memreporental import RentalMemoryRepository


class BinaryRentalRepository(RentalMemoryRepository):
    """
    Binary file-based repository for managing rentals.
    """
    def __init__(self, file_name='rentals.bin'):
        super().__init__()
        self.file_name = file_name
        self.load_file()

    def add_rental(self, rental_id, client_id, book_id):
        """
        Adds a new rental to the repository and saves it to the binary file.
        """
        super().add_rental(rental_id, client_id, book_id)
        self.save_file()

    def load_file(self):
        """
        Loads all rentals from the binary file into memory.
        """
        try:
            with open(self.file_name, 'rb') as input_file:
                rentals = pickle.load(input_file)
                for rental in rentals:
                    self._rentals[rental['rental_id']] = rental
        except (IOError, EOFError):
            # If the file doesn't exist or is empty, start with an empty repository.
            self._rentals = {}

    def save_file(self):
        """
        Saves all rentals to the binary file.
        """
        try:
            with open(self.file_name, 'wb') as out_file:
                pickle.dump(list(self._rentals.values()), out_file)
        except IOError as e:
            raise ValueError(f"Error writing to file: {e}")

    def remove_rental(self, rental_id):
        """
        Removes a rental from the repository and updates the binary file.
        """
        super().remove_rental(rental_id)
        self.save_file()

    def update_rental(self, rental_id, rental_data):
        """
        Updates an existing rental in the repository and the binary file.
        """
        super().update_rental(rental_id, rental_data)
        self.save_file()
