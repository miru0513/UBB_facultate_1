import re
from src.repository.binarybooks import BinaryFileRepository
from src.repository.binaryclient import BinaryClient
from src.repository.binaryrental import BinaryRentalRepository
from src.repository.memrepobooks import InMemoryRepository
from src.repository.memrepoclient import MemRepoClient
from src.repository.memreporental import RentalMemoryRepository
from src.repository.textbook import TextFileRepository
from src.repository.textclient import TextClient
from src.repository.textrental import RentalTextRepository
from src.services.Book_Service import BookService

from src.services.ClientService import ClientService
from src.services.RentalService import RentalService
from src.services.UndoService import UndoService
from src.ui.UI import UI

# Load settings from properties file
with open("settings.properties", 'r') as f:
    separators = r"[ =\"\n]"
    # Read repository type
    option = re.split(separators, f.readline())[3]
    # Read file paths
    book_file = re.split(separators, f.readline())[4]
    client_file = re.split(separators, f.readline())[4]
    rental_file = re.split(separators, f.readline())[4]
    if option == "binaryfiles":
        book_file = book_file.replace(".pickle", ".bin")
        client_file = client_file.replace(".pickle", ".bin")
        rental_file = rental_file.replace(".pickle", ".bin")

# Initialize UndoService
undo_service = UndoService()

# Configure based on repository type
if option == "inmemory":
    print("We are using InMemory Repository \n")
    book_repo = InMemoryRepository()
    client_repo = MemRepoClient()
    rental_repo = RentalMemoryRepository()

elif option == "textfile":
    print("We are using TextFile Repository \n")
    book_repo = TextFileRepository(file_name=book_file)
    client_repo = TextClient(file_name=client_file)
    rental_repo = RentalTextRepository(file_name=rental_file)

else:
    print("We are using Binary Repository \n")
    book_repo = BinaryFileRepository(file_name=book_file)
    client_repo = BinaryClient(file_name=client_file)
    rental_repo = BinaryRentalRepository(file_name=rental_file)

# Initialize Services
book_service = BookService(book_repo, undo_service, rental_repo)
client_service = ClientService(client_repo, undo_service, rental_repo)
rental_service = RentalService(rental_repo, book_service, client_service, undo_service)

# Prepare data for generators
client_names = [
    "John Doe", "Jane Smith", "Michael Johnson", "Emily Davis", "Daniel Brown", "Sarah Wilson",
    "David Miller", "Samantha Moore", "Chris Taylor", "Laura Anderson", "James Thomas", "Mary Jackson",
    "Matthew Harris", "Olivia Martin", "Joshua Lee", "Chloe Scott", "Benjamin Walker", "Megan Allen",
    "Ethan Young", "Isabella King", "Noah Hill", "Charlotte Green", "Oliver Adams", "Sophia Nelson",
    "Aiden Carter", "Grace Perez", "Jackson Murphy", "Amelia Richardson", "Lucas Robinson", "Mia Clark",
    "Liam Lewis", "Zoe Hall", "Mason Scott", "Harper Allen", "Daniel Harris", "Ella Walker",
    "Alexander Lewis", "Scarlett White", "Elijah Adams", "Sophie King", "Jacob Moore", "Ella Clark",
    "Mason Perez", "Avery Nelson", "William Young", "Madison Mitchell", "Jacob Taylor", "Charlotte Lewis",
    "James Harris", "Lily Anderson", "Owen Thomas", "Lucas White"
]

authors = [
    "J.K. Rowling", "George R.R. Martin", "J.R.R. Tolkien", "Agatha Christie",
    "Stephen King", "Isaac Asimov", "Arthur C. Clarke", "H.G. Wells",
    "Orson Scott Card", "Philip K. Dick", "Margaret Atwood", "Neil Gaiman",
    "Ray Bradbury", "Isaac Newton", "C.S. Lewis", "Kurt Vonnegut",
    "William Shakespeare", "F. Scott Fitzgerald", "Charles Dickens", "Jane Austen",
    "Ernest Hemingway", "Toni Morrison", "Mark Twain", "Harper Lee",
    "Virginia Woolf", "Herman Melville", "Jack London", "Emily Dickinson",
    "Ralph Waldo Emerson", "Thomas Hardy", "George Orwell", "Henry James",
    "Khaled Hosseini", "Alice Walker", "Paulo Coelho", "Dan Brown",
    "E.L. James", "J.D. Salinger", "Vladimir Nabokov", "Zadie Smith",
    "David Foster Wallace", "Philip Roth", "John Steinbeck", "Ian McEwan",
    "Chimamanda Ngozi Adichie", "Colleen Hoover", "Salman Rushdie", "Terry Pratchett",
    "Douglas Adams", "Kurt Vonnegut", "Kazuo Ishiguro", "Don DeLillo"
]

book_titles = [
    "The Great Adventure", "Mystery of the Shadows", "Life in the Stars", "Journey to the Unknown",
    "Echoes of Silence", "The Silent Watcher", "Whispers in the Dark", "Timeless Tales",
    "The Last Horizon", "Wings of Freedom", "Darkened Paths", "Beneath the Stars",
    "Chasing the Storm", "Secrets of the Deep", "The Phantom's Curse", "Shadows of Tomorrow",
    "The Forbidden Realm", "Legends Never Die", "Heart of the Ocean", "The Endless Road",
    "Awakening the Beast", "Fires of the Night", "The Hidden City", "Warriors of Light",
    "The Lost Kingdom", "The Song of the Earth", "The Watchers' Legacy", "Bringers of Hope",
    "The Valiant", "Echoes from the Abyss", "Children of the Void", "Nightfall Rising",
    "The Enchanted Forest", "Minds in Conflict", "Fate's Design", "The Last Ember",
    "The Shadows Speak", "The Stone of Destiny", "Tales of the Dragon", "Voices from the Past",
    "The Ghost of Winter", "Whispers of Eternity", "Legends of the Fallen", "Beyond the Dark",
    "The Edge of Infinity", "Return of the Ancients", "The Silent Blade", "A New Dawn",
    "Eyes of the Storm", "The Secret War", "Unbroken Chains", "Kingdom of Ashes"
]

# Import and Initialize Generators
from src.generator.BookGenerator import BookGenerator
from src.generator.ClientGenerator import ClientGenerator
from src.generator.RentalGenerator import RentalGenerator

book_generator = BookGenerator(book_service, book_titles, authors)
client_generator = ClientGenerator(client_service, client_names)
rental_generator = RentalGenerator(book_service, client_service, rental_service)

# Generate data if repositories are empty
if not book_repo.list_book():
    book_generator.generate_books(40)

if not client_repo.list_client():
    client_generator.generate_clients(40)

if not rental_repo.list_rentals():
    rental_generator.generate_rentals(20)

# Initialize and run the UI
ui = UI(client_service, book_service, rental_service, undo_service)
ui.run_menu()
