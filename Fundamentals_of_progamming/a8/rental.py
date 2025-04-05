class Rental:
    def __init__(self,rental_id,book_id,client_id,rented_date,return_date):
        self.__rental_id = rental_id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__return_date = return_date

    @property
    def rental_id(self):
        return self.__rental_id

    @property
    def book_id(self):
        return self.__book_id

    @property
    def client_id(self):
        return self.__client_id

    @property
    def rented_date(self):
        return self.__rented_date

    @property
    def return_date(self):
        return self.__return_date

    @rental_id.setter
    def rental_id(self,rental_id):
        self.__rental_id=rental_id

    @book_id.setter
    def book_id(self,book_id):
        self.__book_id=book_id

    @client_id.setter
    def client_id(self,client_id):
        self.__client_id=client_id

    @rented_date.setter
    def rented_date(self,rented_date):
        self.__rented_date=rented_date

    @return_date.setter
    def return_date(self,return_date):
        self.__return_date=return_date

    def __str__(self):
        return f"Rental: {self.__rental_id} - {self.__book_id} - {self.__client_id} - {self.__rented_date} - {self.__return_date}"