import random

class ClientGenerator:
    def __init__(self,client_service, client_names):
        self._client_service = client_service
        self.client_names = client_names
        self.used_client_names = set()  # To ensure unique client names

    def generate_unique_client_name(self):
        """Generates a unique client name from the list."""
        while True:
            name = random.choice(self.client_names)
            if name not in self.used_client_names:
                self.used_client_names.add(name)
                return name

    def generate_clients(self, number_of_clients):
        """Generates a list of unique clients with random IDs."""
        clients = []
        for _ in range(number_of_clients):
            client_name = self.generate_unique_client_name()
            client_id = random.randint(100, 999)  # Random 3-digit client ID
            self._client_service.add_client_service(client_id,client_name)
