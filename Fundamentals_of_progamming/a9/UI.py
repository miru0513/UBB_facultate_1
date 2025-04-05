from datetime import datetime, timedelta
import random

from src.exceptions.exception_repo import RepositoryException
from src.exceptions.exception_service import ServiceException
from src.exceptions.exception_validator import ValidatorException
from src.services.Book_Service import BookService

from src.services.ClientService import ClientService
from src.services.RentalService import RentalService
from src.validator.BookValidator import BookValidator
from src.validator.ClientValidator import ClientValidator
from src.validator.RentalValidator import RentalValidator


class UI:
    def __init__(self, service1: ClientService, service2: BookService, service3: RentalService, undo_service):
        self.__service1 = service1
        self.__service2 = service2
        self.__service3 = service3
        self.__undo_service = undo_service

    # book
    def add_book(self):
        try:
            book_id = input("Enter id: ")
            author = input("Enter author: ")
            title = input("Enter title: ")
            BookValidator.validate_book_id(book_id)
            BookValidator.validate_author(author)
            BookValidator.validate_title(title)
            book_id = int(book_id)
            self.__service2.add_book_service(book_id, title, author)
            print("Book added successfully!\n")
        except (RepositoryException,ValidatorException) as ex:
            print(f"Error: {ex} \n")

    def display_books(self):
        books = self.__service2.list_books_service()
        if not books:
            print("No books found\n")
        else:
            for book in books:
                print(book)

    def remove_book(self):
        try:
            book_id = input("Enter id: ")
            book_id = int(book_id)
            BookValidator.validate_book_id(book_id)
            self.__service2.remove_book_service(book_id)
            print("Book removed successfully!\n")
        except (RepositoryException,ValidatorException) as ex:
            print(f"Error: {ex}\n")

    def update_book(self):

        try:
            book_id = input("Enter id  ")
            new_title = input("Enter new title: ")
            new_author = input("Enter new author: ")
            BookValidator.validate_book_id(book_id)
            BookValidator.validate_author(new_author)
            BookValidator.validate_title(new_title)
            book_id = int(book_id)
            self.__service2.update_book_service(book_id, new_title, new_author)
            print("Book updated successfully!\n")
        except (RepositoryException,ValidatorException) as ex:
            print(f"Error: {ex}\n")

    def search_books(self):
        query = input("Enter search query: ")
        results = self.__service2.search_books(query)
        if not results:
            print("No matching books found.\n")
        else:
            for book in results:
                print(book)

    def display_most_rented_books(self):
        """
        Displays the list of books sorted by the number of times they were rented, in descending order.
        """
        try:
            most_rented_books = self.__service2.most_rented_books_service()
            if not most_rented_books:
                print("No rentals found.\n")
                return
            print("Most Rented Books:")
            for book, count in most_rented_books:
                print(f"Count: {count} Book ID:{book.book_id} Title:{book.title} Author:{book.author} ")
        except (ServiceException, RepositoryException) as ex:
            print(f"Error: {ex}\n")

    def most_rented_authors_ui(self):
        """
        This function will display the authors with the most rented books in descending order of total rentals.
        It calls the service function `most_rented_author_service` to get the data.
        """
        # Call the service to get the most rented authors
        most_rented_authors = self.__service2.most_rented_author_service()

        # Check if there are any authors to display
        if not most_rented_authors:
            print("No rented books found or no authors available.\n")
            return

        # Display the results
        print("Most Rented Authors:")
        for author in most_rented_authors:
            print(f"Total Rentals: {author['total_rentals']}, Author: {author['author']}")

    # client
    def add_client(self):
        try:
            client_id = input("Enter id: ")
            name = input("Enter name: ")
            ClientValidator.validate_client_id(client_id)
            ClientValidator.validate_client_name(name)
            client_id = int(client_id)
            self.__service1.add_client_service(client_id, name)
            print("Client added successfully!\n")
        except (RepositoryException, ValidatorException) as ex:
            print(f"Error: {ex}\n")

    def display_clients(self):
        clients = self.__service1.list_clients_service()
        if not clients:
            print("No clients found\n")
        else:
            for client in clients:
                print(client)

    def remove_client(self):
        try:
            client_id = input("Enter id: ")
            ClientValidator.validate_client_id(client_id)
            self.__service1.remove_client_service(client_id)
            client_id = int(client_id)
            print("Client removed successfully!\n")
        except (RepositoryException, ValidatorException) as ex:
            print(f"Error: {ex}\n")

    def update_client(self):
        try:
            client_id = input("Enter id: ")
            new_name = input("Enter new name: ")
            ClientValidator.validate_client_id(client_id)
            ClientValidator.validate_client_name(new_name)
            client_id = int(client_id)
            self.__service1.update_client_service(client_id, new_name)
            print("Client updated successfully!\n")
        except (RepositoryException, ValidatorException) as ex:
            print(f"Error: {ex}\n")

    def search_clients(self):
        query = input("Enter search query: ")
        results = self.__service1.search_clients(query)
        if not results:
            print("No matching clients found.\n")
        else:
            for client in results:
                print(client)

    def most_active_clients_ui(self):
        active_clients = self.__service1.most_active_clients_service()
        if not active_clients:
            print("No active clients found.\n")
            return

        print("Most Active Clients:")
        for client in active_clients:
            print(
                f"Total Rental Days: {client['total_days']} ,Client ID: {client['client_id']}, Name: {client['client_name']} ")

    #RENTALS
    def display_rentals(self):
        """
        Displays all rentals in a simple format without headers and extra spacing.
        Calls the service method `list_rentals()` to fetch the data.
        """
        rentals = self.__service3.list_rentals()  # Get the list of rentals from the service
        if not rentals:
            print("No rentals found.\n")
            return

        # Iterate through each rental and print its details
        for rental in rentals:
            print(f"Rental ID: {rental['rental_id']}, Client ID: {rental['client_id']}, "
                  f"Book ID: {rental['book_id']}, Rented Date: {rental['rented_date']}, "
                  f"Returned Date: {rental['returned_date']}")

    def add_rental(self):
        """
        Adds a rental by getting input from the user and calling the service method `rent_book()`.
        """
        try:
            rental_id = input("Enter rental id: ")
            client_id = input("Enter client id: ")
            book_id = input("Enter book id: ")
            ok = True
            for book in self.__service2.list_books_service():
                if book.book_id == book_id:
                    ok = False
                    break

            if ok == False:
                print(f"Book with ID {book_id} doesn't exist.\n")

            ok = True
            for client in self.__service1.list_clients_service():
                if client.client_id == client_id:
                    ok = False
                    break
            if ok == False:
                print(f"Client with ID {client_id} doesn't exist.\n")

            RentalValidator.validate_rental_id(rental_id)
            ClientValidator.validate_client_id(client_id)
            BookValidator.validate_book_id(book_id)
            rental_id = int(rental_id)
            client_id = int(client_id)
            book_id = int(book_id)

            # Set the current date as rented_date
            rented_date = datetime.now()

            # Randomly pick a returned date between 1 and 30 days from now
            returned_date = rented_date + timedelta(days=random.randint(1, 30))

            self.__service3.add_rental(rental_id, client_id, book_id, rented_date, returned_date)
            print("Rental added successfully!\n")
        except (RepositoryException, ServiceException, ValidatorException) as ve:
            print(f"Error: {ve}\n")

    def return_rental(self):
        """
        Allows the user to return a rental by entering its rental ID.
        Calls the service method `return_book()` to handle the return.
        """

        try:
            rental_id = input("Enter rental id to return: ")
            RentalValidator.validate_rental_id(rental_id)
            rental_id = int(rental_id)
            self.__service3.return_book(rental_id)
            print(f"Book with Rental ID {rental_id} has been returned.\n")
        except (RepositoryException, ServiceException, ValidatorException) as ve:
            print(f"Error: {ve}\n")


    # UNDO / REDO
    def undo_action(self):
        try:
            self.__undo_service.undo()
            print("Undo operation completed successfully!")
        except ServiceException as e:
            print(f"Error during undo: {e}\n")

    def redo_action(self):
        try:
            self.__undo_service.redo()
            print("Redo operation completed successfully!")
        except ServiceException as e:
            print(f"Error during redo: {e}\n")

    @staticmethod
    def display_menu():
        print("1.Books")
        print("2.Clients")
        print("3.Searching")
        print("4.Rentals")
        print("5.Undo/Redo")
        print("0.Exit")

    def run_menu(self):
        while True:
            self.display_menu()
            choice1 = input("Enter your choice of sets: ")
            print("\n")

            if choice1 == "1":
                print("1. Add book")
                print("2. List books")
                print("3. Remove book")
                print("4. Update book")
                print("5. Most rented books")
                print("6. Most rented authors by total rentals")

                choice = input("Enter your choice: ")
                print("\n")
                if choice == "1":
                    self.add_book()
                elif choice == "2":
                    self.display_books()
                elif choice == "3":
                    self.remove_book()
                elif choice == "4":
                    self.update_book()
                elif choice == "5":
                    self.display_most_rented_books()
                elif choice == "6":
                    self.most_rented_authors_ui()
                else:
                    print("Invalid choice. Please try again.\n")

            elif choice1 == "2":
                print("1. Add client")
                print("2. List clients")
                print("3. Remove client")
                print("4. Update client")
                print("5. Most active clients")

                choice = input("Enter your choice: ")
                print("\n")
                if choice == "1":
                    self.add_client()
                elif choice == "2":
                    self.display_clients()
                elif choice == "3":
                    self.remove_client()
                elif choice == "4":
                    self.update_client()
                elif choice == "5":
                    self.most_active_clients_ui()
                else:
                    print("Invalid choice. Please try again.\n")

            elif choice1 == "3":
                print("1. Search books")
                print("2. Search clients")

                choice = input("Enter your choice: ")
                print("\n")
                if choice == "1":
                    self.search_books()
                elif choice == "2":
                    self.search_clients()
                else:
                    print("Invalid choice. Please try again.\n")

            elif choice1 == "4":
                print("1. Add rental")
                print("2. Return rental")
                print("3. Display rental")

                choice = input("Enter your choice: ")
                print("\n")
                if choice == "1":
                    self.add_rental()
                elif choice == "2":
                    self.return_rental()
                elif choice == "3":
                    self.display_rentals()
                else:
                    print("Invalid choice. Please try again.\n")

            elif choice1 == "5":
                print("1. Undo")
                print("2. Redo")

                choice = input("Enter your choice: ")
                print("\n")
                if choice == "1":
                    self.undo_action()
                elif choice == "2":
                    self.redo_action()
                else:
                    print("Invalid choice. Please try again.\n")

            elif choice1 == "0":
                print("Exiting the program...")
                break

            else:
                print("Invalid choice. Please try again.\n")

            print("\n")






