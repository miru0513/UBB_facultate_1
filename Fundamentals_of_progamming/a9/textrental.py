import os
from datetime import datetime
from src.exceptions.exception_repo import RepositoryException
from src.repository.memreporental import RentalMemoryRepository


class RentalTextRepository(RentalMemoryRepository):
    """
    A repository that manages rentals stored in a text file.
    Inherits from RentalMemoryRepository to allow easy in-memory manipulation.
    """

    def __init__(self, file_name):
        super().__init__()
        self.file_path = file_name

    def load_file(self):
        """
        Load rental data from a text file into the in-memory repository.
        """
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w'):  # Create an empty file if it doesn't exist
                pass

        with open(self.file_path, 'r') as file:
            for line in file:
                rental_id, client_id, book_id, rented_date, returned_date = line.strip().split(',')
                rented_date = datetime.strptime(rented_date, '%Y-%m-%d')
                returned_date = datetime.strptime(returned_date, '%Y-%m-%d') if returned_date != 'None' else None
                self.add_rental(int(rental_id), client_id, book_id, rented_date, returned_date)

    def save_file(self):
        """
        Save rental data from the in-memory repository to the text file.
        """
        with open(self.file_path, 'w') as file:
            for rental in list(self.list_rentals()):
                rental_line = (f"{rental['rental_id']},{rental['client_id']},"
                               f"{rental['book_id']},{rental['rented_date']},"
                               f"{rental['returned_date'] if ['rental.returned_date'] else 'None'}\n")
                file.write(rental_line)

    def add_rental(self, rental_id, client_id, book_id, rented_date, returned_date):
        """
        Add a rental to the repository and update the file.
        """
        super().add_rental(rental_id, client_id, book_id, rented_date, returned_date)
        with open(self.file_path, 'a') as file:
            rental_line = (f"{rental_id},{client_id},{book_id},{rented_date.strftime('%Y-%m-%d')},"
                           f"{returned_date.strftime('%Y-%m-%d') if returned_date else 'None'}\n")
            file.write(rental_line)

    def list_rentals(self):
        return super().list_rentals()

    def get_rental(self, rental_id):
        return super().get_rental(rental_id)

    def is_book_rented(self, book_id):
        return super().is_book_rented(book_id)

    def remove_rental(self, rental_id):
        super().remove_rental(rental_id)
        self.save_file()

    def list_rentals_for_book(self, book_id):
        return super().list_rentals_for_book(book_id)