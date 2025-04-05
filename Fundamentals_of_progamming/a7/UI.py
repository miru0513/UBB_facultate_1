from src.services.Service import BookService


class UI:
    def __init__(self, service: BookService):
        self.__service = service
        self.__x = 1


    def add_book(self, x):
        isbn = input("Enter ISBN: ")
        author = input("Enter author: ")
        title = input("Enter title: ")
        try:
            self.__service.add_book(isbn, author, title,x)1

            print("Book added successfully!")
        except ValueError as ve:
            print(f"Error: {ve}")

    def display_books(self, x):
        books = self.__service.get_all_books(x) #codeaza optiunea
        if not books:
            print("No books available.")
        else:
            for book in books:
                print(book)

    def filter_books(self, x):
        prefix = input("Enter title prefix to filter: ")
        try:
            self.__service.filter_books_by_title(prefix,x)
            print("Books filtered successfully!")
        except ValueError as ve:
            print(f"Error: {ve}")

    def undo(self,x):
        try:
            self.__service.undo(x)
            print("Undo successful!")
        except ValueError as ve:
            print(f"Error: {ve}")

    @staticmethod
    def help_menu(self):
        print("1. Add book")
        print("2. Display books")
        print("3. Filter books by title prefix")
        print("4. Undo last action")
        print("5. Exit")
        print("* another memory type")
        if self.__x == 1 :
            print("* Select memory repository (Memory Repository Selected)")
        elif self.__x == 2 :
            print("* Select memory repository (Text File Selected)")
        else:
            if self.__x == 3:
                print("* Select memory repository (Binary File Selected)")

    def start(self):
        while True:
            self.help_menu(self)
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_book(self.__x)
            elif choice == '2':
                self.display_books(self.__x)
            elif choice == '3':
                self.filter_books(self.__x)
            elif choice == '4':
                self.undo(self.__x)
            elif choice == '5':
                break
            elif choice == '*':
                p = int(input("Choose MemoryType 1 2 3: "))
                self.__x = p
            else:
                print("Invalid choice, please try again.")
