from src.domain.client import Client
from src.repository.memrepoclient import MemRepoClient


class TextClient(MemRepoClient):
    def __init__(self,file_name='clients.txt'):
        super().__init__()
        self.file_name=file_name
        self.load_file()

    def load_file(self):
        try:
            with open(self.file_name, 'rt') as input_file:
                for line in input_file.readlines():
                    properties = line.strip().split(',')
                    if(len(properties)==2):
                        client=Client(properties[0],properties[1])
                        super().add(client)
        except FileNotFoundError:
            pass

    def save_file(self):
        try:
            with open(self.file_name, 'wt') as out_file:
                for client in super().list():
                    client_string= f"{client.client_id},{client.name}\n"
                    out_file.write(client_string)
        except IOError as e:
            raise ValueError(f"Error writing to file: {e}")

    def add(self, new_client: Client):
        super().add(new_client)
        self.save_file()

    def remove(self, client_id):
        client_to_remove = self.find_by_id(client_id)
        if client_to_remove is None:
            raise ValueError("Book with the given ID does not exist.")
        super().remove(client_id)
        self.save_file()

    def update(self, client: Client):
        client_to_update = self.find_by_id(client.client_id)
        if client_to_update is None:
            raise ValueError("Book with the given ID does not exist.")
        client_to_update.name = client.name
        self.save_file()

