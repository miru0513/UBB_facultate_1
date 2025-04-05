from src.domain.client import Client


class MemRepoClient:
    def __init__(self):
        self._data = {}

    def add(self,client: Client):
        if client.client_id in self._data:
            raise ValueError("Client with this id already exists.")
        self._data[client.client_id] = client

    def remove(self,client_id:str):
        if client_id not in self._data:
            raise ValueError("Client with this id doesn't exist.")
        del self._data[client_id]

    def update(self,client:Client):
        if client.client_id not in self._data:
            raise ValueError("Client with this id doesn't exist.")
        self._data[client.client_id] = client

    def list(self):
        return self._data.values()

    def find_by_id(self,client_id:str):
        return self._data.get(client_id,None)