
from src.repository.binarybooks import BinaryFileRepository
from src.repository.binaryclient import BinaryClient
from src.repository.memrepobooks import InMemoryRepository
from src.repository.memrepoclient import MemRepoClient
from src.repository.memreporental import RentalMemoryRepository
from src.repository.textbook import TextFileRepository
from src.repository.textclient import TextClient
from src.repository.textrental import RentalTextRepo
from src.services.Book_service import BookService
from src.services.ClientService import ClientService
from src.services.RentalService import RentalService
from src.ui.UI import UI

option = "text" # sau text



















if option == "memory":
    #do smt
    book_repo = InMemoryRepository()
    book_service = BookService(book_repo)
    if not book_repo.list():
        book_service.generate_books(20)

    client_repo = MemRepoClient()
    client_service = ClientService(client_repo)
    if not client_repo.list():
        client_service.generate_clients(20)

    rental_repo = RentalMemoryRepository()  # Replace with appropriate rental repository class
    rental_service = RentalService(rental_repo, client_service,
                                   book_service)  # Replace with the correct service initialization
    ui = UI(client_service, book_service, rental_service, "memory")
    ui.run_menu()
elif option == "text":
    # Calling TextFileRepository for books
    book_repo = TextFileRepository(file_name='books.txt')
    book_service = BookService(book_repo)

    if not book_repo.list():
        book_service.generate_books(20)

    client_repo = TextClient(file_name='clients.txt')
    client_service = ClientService(client_repo)
    if not client_repo.list():
        client_service.generate_clients(20)

    # Assuming a rentals repository and service exist as well
    rental_repo = RentalTextRepo(file_name='rentals.txt')  # Replace with appropriate rental repository class
    rental_service = RentalService(rental_repo, client_service,
                                   book_service)  # Replace with the correct service initialization
    ui = UI(client_service, book_service, rental_service, "text")
    ui.run_menu()
else:
    book_repo = BinaryFileRepository(file_name='books.bin')
    book_service = BookService(book_repo)
    if not book_repo.list():
        book_service.generate_books(20)

    client_repo=BinaryClient(file_name='clients.bin')
    client_service=ClientService(client_repo)
    if not client_repo.list():
        client_service.generate_clients(20)

    rental_repo=BinaryFileRepository(file_name='rentals.bin')
    rental_service=RentalService(rental_repo,client_service,book_service)
    ui=UI(client_service,book_service,rental_service,"binary")
    ui.run_menu()

"""
# Calling TextFileRepository for books
book_repo = TextFileRepository(file_name='books.txt')
book_service = BookService(book_repo)

if not book_repo.list():
    book_service.generate_books(20)

client_repo = TextClient(file_name='clients.txt')
client_service = ClientService(client_repo)
if not client_repo.list():
    client_service.generate_clients(20)

# Assuming a rentals repository and service exist as well
rental_repo = RentalTextRepo(file_name='rentals.txt')  # Replace with appropriate rental repository class
rental_service = RentalService(rental_repo,client_service,book_service)  # Replace with the correct service initialization
"""


"""

book_repo = InMemoryRepository()
book_service = BookService(book_repo)
if not book_repo.list():
    book_service.generate_books(20)

client_repo =MemRepoClient()
client_service = ClientService(client_repo)
if not client_repo.list():
    client_service.generate_clients(20)


rental_repo = RentalMemoryRepository()  # Replace with appropriate rental repository class
rental_service = RentalService(rental_repo,client_service,book_service)  # Replace with the correct service initialization

"""
# Initialize UI and start the application with all services
ui = UI(client_service, book_service, rental_service, "memory")
ui.run_menu()