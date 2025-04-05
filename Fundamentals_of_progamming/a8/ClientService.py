from faker import Faker

from src.domain.client import Client

class ClientService:
    def __init__(self,repo):
        self.__repo=repo

    def add_client(self,client_id,name):
        client=Client(client_id,name)
        self.__repo.add(client)

    def list_clients(self):
        return self.__repo.list()

    def remove_client(self,client_id):
        self.__repo.remove(client_id)

    def update_client(self,client_id,name):
        client=Client(client_id,name)
        self.__repo.update(client)

    def generate_clients(self, number_of_clients: int):
        """
        Generates a specified number of random clients and adds them to the repository.
        :param number_of_clients: The number of clients to generate.
        """
        fake = Faker()
        for _ in range(number_of_clients):
            client_id = fake.unique.random_int(min=10000, max=99999)
            name = fake.name()
            self.add_client(client_id, name)

    def search_clients(self, query):
        """
        Searches for clients using a case-insensitive, partial match for id or name.
        :param query: The search query string.
        :return: A list of clients that match the query.
        """
        query = query.lower()
        return [
            client for client in self.__repo.list()
            if query in str(client.client_id).lower() or
               query in client.name.lower()
        ]


    def find_by_id(self, client_id):
        for client in self.__repo.list():
             if client.client_id == client_id:
                return client
        return None
