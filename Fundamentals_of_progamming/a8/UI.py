
from src.services.Book_service import BookService
from src.services.ClientService import ClientService
from src.services.RentalService import RentalService


class UI:
    def __init__(self, service1:ClientService,service2:BookService,service3:RentalService, variable):
        self.__service1=service1
        self.__service2=service2
        self.__service3=service3
        self.__variable = variable
#book
    def add_book(self):
        while True:
            try:
                book_id = int(input("Enter id: "))
                if book_id <= 0:  # Check if the number is positive
                    print("ID must be a positive number. Please try again.")
                    continue
                break  # Exit the loop if the input is valid
            except ValueError:
                print("Invalid id! Please enter a valid positive integer.")

        author = input("Enter author: ")
        title = input("Enter title: ")

        try:
            self.__service2.add_book(book_id, title, author)
            print("Book added successfully!")
        except ValueError as ve:
            print(f"Error: {ve}")

    def display_books(self):
        books=self.__service2.list_books()
        if not books:
            print("no books found")
        else:
            for book in books:
                print(book)

    def remove_book(self):
        book_id=input("Enter id: ")
        try:
            self.__service2.remove_book(book_id)
            print("Book removed successfully!")
        except ValueError as ve:
            print(f"Error: {ve}")
    
    def update_book(self):

        book_id = input("Enter id  ")
        new_title = input("Enter new title: ")
        new_author = input("Enter new author: ")
        try:
            self.__service2.update_book(book_id, new_title, new_author)
            print("Book updated successfully!")
        except ValueError as ve:
            print(f"Error: {ve}")

    def search_books(self):
        query = input("Enter search query: ")
        results = self.__service2.search_books(query)
        if not results:
            print("No matching books found.")
        else:
            for book in results:
                print(book)
#client
    def add_client(self):
        while True:
            try:
                client_id = int(input("Enter id: "))
                if client_id <= 0:  # Check if the number is positive
                    print("ID must be a positive number. Please try again.")
                    continue
                break  # Exit the loop if the input is valid
            except ValueError:
                print("Invalid id! Please enter a valid positive integer.")

        name = input("Enter name: ")

        try:
            self.__service1.add_client(client_id, name)
            print("Client added successfully!")
        except ValueError as ve:
            print(f"Error: {ve}")

    def display_clients(self):
        clients=self.__service1.list_clients()
        if not clients:
            print("no clients found")
        else:
            for client in clients:
                print(client)
    def remove_client(self):
        client_id=input("Enter id: ")
        try:
            self.__service1.remove_client(client_id)
            print("Client removed successfully!")
        except ValueError as ve:
            print(f"Error: {ve}")
    def update_client(self):
        client_id=input("Enter id: ")
        new_name=input("Enter new name: ")
        try:
            self.__service1.update_client(client_id,new_name)
            print("Client updated successfully!")
        except ValueError as ve:
            print(f"Error: {ve}")

    def search_clients(self):
        query = input("Enter search query: ")
        results = self.__service1.search_clients(query)
        if not results:
            print("No matching clients found.")
        else:
            for client in results:
                print(client)
#rentals
    def add_rental(self):

        if self.__variable == "memory":
            rental_id = int(input("Enter rental id: "))
            client_id =int(input("Enter client id: "))
            book_id = int(input("Enter book id: "))
        else:
            rental_id = input("Enter rental id: ")
            client_id =input("Enter client id: ")
            book_id = input("Enter book id: ")

        try:
            self.__service3.rent_book(rental_id, client_id,book_id)
            print("Rental added successfully!")
        except ValueError as ve:
            print(f"Error: {ve}")


    def return_rental(self):
        if self.__variable == "memory":
            rental_id = int(input("Enter rental id to return: "))
        else:
            rental_id = input("Enter rental id to return: ")
        try:
            self.__service3.return_book(rental_id)
            print("Rental returned successfully!")
        except ValueError as ve:
            print(f"Error: {ve}")

    @staticmethod
    def display_menu():
        print("1.Books")
        print("2.Clients")
        print("3.Searching")
        print("4.Rentals")
        print("5.Exit")


    def run_menu(self):
        while True:
            self.display_menu()
            choice1 = input("Enter your choice of sets: ")
            if choice1 == "1":
                print("1. Add book")
                print("2. List books")
                print("3. Remove book")
                print("4. Update book")
                print("5. Exit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.add_book()
                elif choice == "2":
                    self.display_books()
                elif choice == "3":
                    self.remove_book()
                elif choice == "4":
                    self.update_book()
                elif choice == "5":
                    print("Exiting the program...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            if choice1 == "2":
                print("1. Add client")
                print("2. List clients")
                print("3. Remove client")
                print("4. Update client")
                print("5. Exit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.add_client()
                elif choice == "2":
                    self.display_clients()
                elif choice == "3":
                    self.remove_client()
                elif choice == "4":
                    self.update_client()
                elif choice == "5":
                    print("Exiting the program...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            if choice1=="3":
                print("1. Search books")
                print("2. Search clients")
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.search_books()
                if choice == "2":
                    self.search_clients()

            if choice1=="4":

                print("1. Add rental")
                print("2. Return rental")
                print("3. Exit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.add_rental()
                elif choice == "2":
                    self.return_rental()
                elif choice == "3":
                    print("Exiting the program...")
                    break
                else:
                    print("Invalid choice. Please try again.")






