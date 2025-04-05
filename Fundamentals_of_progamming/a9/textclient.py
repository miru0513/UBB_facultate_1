from src.domain.client import Client
from src.exceptions.exception_repo import RepositoryException
from src.repository.memrepoclient import MemRepoClient

class TextClient(MemRepoClient):
    def __init__(self,file_name):
        super().__init__()
        self.file_name=file_name
        self.load_file()

    def load_file(self):
        try:
            with open(self.file_name, 'rt') as input_file:
                for line in input_file.readlines():
                    properties = line.strip().split(',')
                    if len(properties)==2:
                        client=Client(properties[0],properties[1])
                        super().add_client(client)
            input_file.close()
        except FileNotFoundError:
            pass

    def save_file(self):
        try:
            with open(self.file_name, 'wt') as out_file:
                for client in super().list_client():
                    client_string= f"{client.client_id},{client.name}\n"
                    out_file.write(client_string)
            out_file.close()
        except IOError as e:
            raise RepositoryException(f"Error writing to file: {e}")

    def list_client(self):
        return super().list_client()

    def find_by_id_client(self,client_id):
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

