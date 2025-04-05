import pickle

from src.domain.client import Client
from src.repository.memrepoclient import MemRepoClient


class BinaryClient(MemRepoClient):
    def __init__(self,file_name='clients.bin'):
        super().__init__()
        self.file_name=file_name
        self.load_file()

    def add(self, client: Client):
        super().add(client)
        self.save_file()

    def load_file(self):
        try:
            with open(self.file_name, 'rb') as input_file:
                books = pickle.load(input_file)
                for book in books:
                    super().add(book)
        except (IOError, EOFError):
            # If the file doesn't exist or is empty, we'll start with an empty repository.
            pass

    def save_file(self):
        try:
            with open(self.file_name, 'wb') as out_file:
                # Explicitly convert to list to avoid `dict_values` serialization error
                pickle.dump(list(self.list()), out_file)
        except IOError as e:
            raise ValueError(f"Error writing to file: {e}")

    def remove(self, client_id):
        super().remove(client_id)
        self.save_file()
