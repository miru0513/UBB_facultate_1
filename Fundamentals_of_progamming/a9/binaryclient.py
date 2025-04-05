import pickle

from src.domain.client import Client
from src.exceptions.exception_repo import RepositoryException
from src.repository.memrepoclient import MemRepoClient


class BinaryClient(MemRepoClient):
    def __init__(self,file_name):
        super().__init__()
        self.file_name=file_name
        self.load_file()

    def load_file(self):
        try:
            with open(self.file_name, 'rb') as input_file:
                clients = pickle.load(input_file)
                for client in clients:
                    super().add_client(client)
            input_file.close()
        except (IOError, EOFError):
            # If the file doesn't exist or is empty, we'll start with an empty repository.
            pass

    def save_file(self):
        try:
            with open(self.file_name, 'wb') as out_file:
                # Explicitly convert to list to avoid `dict_values` serialization error
                pickle.dump(list(self.list_client()), out_file)
            out_file.close()
        except IOError as e:
            raise RepositoryException(f"Error writing to file: {e}")

    def list_client(self):
        return super().list_client()

    def find_by_id_client(self, client_id):
        return super().find_by_id_client(client_id)

    def add_client(self, new_client: Client):
        super().add_client(new_client)
        self.save_file()

    def remove_client(self, client_id):
        super().remove_client(client_id)
        self.save_file()

    def update_client(self, client: Client):
        super().update_client(client)
        self.save_file()

