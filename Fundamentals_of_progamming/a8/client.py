class Client:
    def __init__(self,client_id,name):
        self.__client_id = client_id
        self.__name = name

    @property
    def client_id(self):
        return self.__client_id

    @property
    def name(self):
        return self.__name

    @client_id.setter
    def client_id(self,client_id):
        self.__client_id=client_id

    @name.setter
    def name(self,name):
        self.__name=name

    def __str__(self):
        return f"Client: {self.__client_id} - {self.__name}"