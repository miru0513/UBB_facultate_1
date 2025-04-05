class RentalService:
    def __init__(self,rental_repo,client_repo,book_repo):
        self._rental_repo = rental_repo
        self._client_repo = client_repo
        self._book_repo = book_repo

    def find_by_id(self,rental_id):
        for rent in self._rental_repo:
            if rent.id == rental_id:
                return rent
        return None

    def rent_book(self,rental_id, client_id, book_id):
        """Allows a client to rent a book if it is available"""
        book = self._book_repo.find_by_id(book_id)
        client = self._client_repo.find_by_id(client_id)

        if book is None:
            raise ValueError("The book with the given ID does not exist.")
        if client is None:
            raise ValueError("The client with the given ID does not exist.")
        if self._rental_repo.is_rented(book_id):
            raise ValueError("The book is currently rented and not available.")

        self._rental_repo.add_rental(rental_id,client_id, book_id)
        print(f"Book with ID {book_id} rented by client with ID {client_id}.")

    def return_book(self, book_id):
       #Allows a client to return a rented book
#        if not self._rental_repo.is_rented(book_id):
  #          raise ValueError("The book is not currently rented, so it can't be returned.")

        self._rental_repo.remove_rental(book_id)
        print(f"Book with ID {book_id} has been returned.")




