from src.repository.memreporental import RentalMemoryRepository


class RentalTextRepo(RentalMemoryRepository):
    def __init__(self, file_name='rentals.txt'):
        super().__init__()  # Call to the parent class (if using inheritance)
        self.file_name = file_name
        self.load_file()

    def load_file(self):
        self.rentals = []
        try:
            with open(self.file_name, 'rt') as file:
                for line in file:
                    rental_id,client_id, book_id =line.strip().split(',')
                    self.rentals.append({
                        'rental_id': rental_id,
                        'client_id': client_id,
                        'book_id': book_id
                    })
        except FileNotFoundError:
            # If the file doesn’t exist, initialize with an empty list of rentals.
            self.rentals = []

    def save_file(self):
        """
        Save all rental data back to the file.
        """
        with open(self.file_name, 'w') as file:
            for rental in self.rentals:
                line = f"{rental['rental_id']},{rental['client_id']},{rental['book_id']}\n"
                file.write(line)


    def add_rental(self, rental_id,client_id, book_id):
        """
        Add a new rental to the repository.

        :param rental_id: Unique ID of the rental.
        :param customer_name: Name of the customer.
        :param rental_date: The date of the rental.
        :param return_date: The date of the return.
        """
       # super().add_rental(rental_id,client_id, book_id)
        self.rentals.append({
            'rental_id': rental_id,
            'client_id': client_id,
            'book_id': book_id
        })
        self.save_file()



    def is_rented(self, rental_id):
        """
        Find a specific rental by its unique ID.

        :param rental_id: The unique ID of the rental to find.
        :return: A dictionary representing the rental data, or None if not found.
        """
       # super().find_by_id(rental_id)
        for rental in self.rentals:
            if rental['book_id'] == rental_id:
                return True
        return False

    def remove_rental(self, rental_id):
        """
        Remove a rental from the repository by its unique ID.

        :param rental_id: The unique ID of the rental to remove.
        """
        found_rental = None
        for rental in self.rentals:
            if rental['rental_id'] == rental_id:
                found_rental = rental
                break

        if not found_rental:
            raise ValueError(f"Rental with ID {rental_id} does not exist.")

        self.rentals.remove(found_rental)
        self.save_file()
