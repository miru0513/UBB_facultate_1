from src.exceptions.exception_validator import ValidatorException

class ClientValidator:
    @staticmethod
    def validate_client_id(client_id):
        """ Validates client ID (should be a positive 3-digit integer) """
        try:
            client_id = int(client_id)  # Try to convert client_id to integer
        except (ValidatorException,ValueError):
            raise ValidatorException(f"Invalid client ID: {client_id}. It should be an integer.")

        # Perform checks for valid client_id
        if client_id <= 0:
            raise ValidatorException(f"Invalid client ID: {client_id}. It should be a positive integer.")

        if client_id < 100 or client_id > 999:
            raise ValidatorException(
                f"Invalid client ID: {client_id}. It should be a 3-digit number (between 100 and 999).")

        return True

    @staticmethod
    def validate_client_name(name):
        """ Validates the client name (should be a non-empty string) """
        if not isinstance(name, str) or not name.strip():
            raise ValidatorException(f"Invalid client name: '{name}'. Name cannot be empty or non-string.")
        return True
