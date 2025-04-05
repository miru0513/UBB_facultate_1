from src.domain.client import Client
from src.exceptions.exception_repo import RepositoryException

class MemRepoClient:
    def __init__(self):
        self._data = {}  # Dictionary to store clients, keyed by client_id

    def list_client(self):
        """
        List all clients in the repository.
        :return: A collection of all client objects
        """
        return self._data.values()

    def find_by_id_client(self, client_id):
        """
        Find a client by their ID.
        :param client_id: The ID of the client to find
        :return: The client object if found, None otherwise
        """
        client_id = str(client_id)  # Ensure consistent key type
        return self._data.get(client_id, None)

    def add_client(self, client: Client):
        """
        Add a new client to the repository.
        :param client: Client object to add
        :raises RepositoryException: If the client ID already exists
        """
        client_id = str(client.client_id)  # Ensure consistent key type
        self._data[client_id] = client

    def remove_client(self, client_id: str):
        """
        Remove a client by their ID.
        :param client_id: The ID of the client to remove
        :raises RepositoryException: If the client ID does not exist
        """
        client_id = str(client_id)  # Ensure consistent key type
        if client_id not in self._data:
            raise RepositoryException("Client with this ID doesn't exist.")
        del self._data[client_id]

    def update_client(self, client: Client):
        """
        Update an existing client's details.
        :param client: Client object with updated details
        :raises RepositoryException: If the client ID does not exist
        """
        client_id = str(client.client_id)  # Ensure consistent key type
        client_to_update = self.find_by_id_client(client_id)
        if client_to_update is None:
            raise RepositoryException("Client with the given ID does not exist.")

        # Update the existing client's attributes
        client_to_update.name = client.name
