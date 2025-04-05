from src.exceptions.exception_validator import ValidatorException

class BookValidator:
    @staticmethod
    def validate_book_id(book_id):
        """ Validates book ID (should be a positive 3-digit integer) """
        try:
            book_id = int(book_id)  # Try to convert book_id to integer
        except (ValidatorException, ValueError):
            raise ValidatorException(f"Invalid book ID: {book_id}. It should be an integer.")

        # Perform checks for valid book_id
        if book_id <= 0:
            raise ValidatorException(f"Invalid book ID: {book_id}. It should be a positive integer.")

        if book_id < 100 or book_id > 999:
            raise ValidatorException(
                f"Invalid book ID: {book_id}. It should be a 3-digit number (between 100 and 999).")

        return True

    @staticmethod
    def validate_title(title):
        """ Validates the book title (should be a non-empty string) """
        if not isinstance(title, str) or not title.strip():
            raise ValidatorException(f"Invalid book title: '{title}'. Title cannot be empty or non-string.")
        return True

    @staticmethod
    def validate_author(author):
        """ Validates the author name (should be a non-empty string) """
        if not isinstance(author, str) or not author.strip():
            raise ValidatorException(f"Invalid author name: '{author}'. Author cannot be empty or non-string.")
        return True
