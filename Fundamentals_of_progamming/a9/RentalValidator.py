from src.exceptions.exception_validator import ValidatorException
class RentalValidator:
    @staticmethod
    def validate_rental_id(rental_id):
        """ Validates rental ID (should be a positive 3-digit integer) """
        try:
            rental_id = int(rental_id)  # Try to convert rental_id to integer
        except (ValidatorException, ValueError):
            raise ValidatorException(f"Invalid rental ID: {rental_id}. It should be an integer.")

        # Perform checks for valid rental_id
        if rental_id <= 0:
            raise ValidatorException(f"Invalid rental ID: {rental_id}. It should be a positive integer.")

        if rental_id < 100 or rental_id > 999:
            raise ValidatorException(
                f"Invalid rental ID: {rental_id}. It should be a 3-digit number (between 100 and 999).")

        return True