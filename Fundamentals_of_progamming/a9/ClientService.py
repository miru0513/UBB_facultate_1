import copy
from datetime import datetime

from faker import Faker
from src.domain.client import Client
from src.exceptions.exception_service import ServiceException
from src.services.UndoService import FunctionCall
from src.services.UndoService import Operation


class ClientService:
    def __init__(self, repo, undo_service, rental_repo):
        self.__repo = repo
        self.__undo_service = undo_service
        self._rentals_repo = rental_repo

    def list_clients_service(self):
        return self.__repo.list_client()

    def find_by_id_client_service(self, client_id):
        return self.__repo.find_by_id_client(client_id)

    def add_client_service(self, client_id, name):
        """
        Adds a client to the repository and records undo/redo operations.
        """
        client = Client(client_id, name)
        self.__repo.add_client(client)

        # Define undo and redo actions
        undo_action = FunctionCall(self.__repo.remove_client, client_id)
        redo_action = FunctionCall(self.__repo.add_client, client)

        # Record the operation in UndoService
        operation = Operation(undo_action, redo_action)
        self.__undo_service.record(operation)

    def remove_client_service(self, client_id):
        """
        Removes a client from the repository, deleting any associated rentals first.
        If the client has active rentals, they will be deleted before the client is removed.
        """

        # Find all rentals associated with the client
        rentals_to_delete = [rental for rental in self._rentals_repo.list_rentals() if rental['client_id'] == client_id]

        # Prepare undo/redo actions for the client removal
        client = self.__repo.find_by_id_client(client_id)
        if client is None:
            print(f"Client with ID {client_id} does not exist.\n")
            return

        undo_client_action = FunctionCall(self.__repo.add_client, client)  # Undo: Add the client back
        redo_client_action = FunctionCall(self.__repo.remove_client, client_id)  # Redo: Remove the client

        # Prepare undo/redo actions for rentals removal
        undo_rentals = []
        redo_rentals = []

        # If there are related rentals, prepare the actions
        if rentals_to_delete:
            for rental in rentals_to_delete:
                # Undo: Add rental back to the repository
                undo_rentals.append(
                    FunctionCall(self._rentals_repo.add_rental, rental['rental_id'], rental['client_id'],
                                 rental['book_id'], rental['rented_date'], rental['returned_date'])
                )
                # Redo: Remove the rental
                redo_rentals.append(FunctionCall(self._rentals_repo.remove_rental, rental['rental_id']))

            # Perform the cascading delete for rentals
            for rental in rentals_to_delete:
                self._rentals_repo.remove_rental(rental['rental_id'])

        # Perform the client removal
        self.__repo.remove_client(client_id)

        # Record undo/redo actions for the client and the rentals
        operation = Operation(undo_client_action, redo_client_action)

        # Add cascading undo/redo actions for the rentals
        for undo_rental, redo_rental in zip(undo_rentals, redo_rentals):
            operation.add_cascade(undo_rental, redo_rental)

        # Record the operation in UndoService
        self.__undo_service.record(operation)

    def update_client_service(self, client_id, name):
        """
        Updates a client in the repository and records undo/redo operations.
        """
        old_client = self.__repo.find_by_id_client(client_id)
        if old_client is None:
            raise ValueError(f"Client with ID {client_id} does not exist.\n")

        old_old_client = copy.deepcopy(old_client)
        updated_client = Client(client_id, name)
        self.__repo.update_client(updated_client)

        # Define undo and redo actions
        undo_action = FunctionCall(self.__repo.update_client, old_old_client)
        redo_action = FunctionCall(self.__repo.update_client, updated_client)

        # Record the operation in UndoService
        operation = Operation(undo_action, redo_action)
        self.__undo_service.record(operation)


    def search_clients(self, query):
        """
        Searches for clients using a case-insensitive, partial match for id or name.
        :param query: The search query string.
        :return: A list of clients that match the query.
        """
        query = query.lower()
        return [
            client for client in self.__repo.list_client()
            if query in str(client.client_id).lower() or
               query in client.name.lower()
        ]

    from datetime import datetime

    def most_active_clients_service(self):

        client_activity = {}

        for rental in self._rentals_repo.list_rentals():
            client_id = rental['client_id']


            if isinstance(rental['rented_date'], str):
                rented_date = datetime.strptime(rental['rented_date'], "%Y-%m-%d")
            else:
                rented_date = rental['rented_date']

            if isinstance(rental['returned_date'], str):
                returned_date = datetime.strptime(rental['returned_date'], "%Y-%m-%d")
            else:
                returned_date = rental['returned_date']

            rental_days = (returned_date - rented_date).days +1


            if client_id in client_activity:
                client_activity[client_id] += rental_days
            else:
                client_activity[client_id] = rental_days

        sorted_clients = sorted(client_activity.items(), key=lambda x: x[1], reverse=True)

        active_clients = []
        for client_id, total_days in sorted_clients:
            client = self.__repo.find_by_id_client(client_id)
            active_clients.append({
                'client_id': client_id,
                'client_name': client.name,
                'total_days': total_days
            })

        return active_clients
