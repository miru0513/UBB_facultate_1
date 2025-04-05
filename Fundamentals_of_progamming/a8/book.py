class Book:
    def __init__(self,book_id,title,author):
        self.__book_id=book_id
        self.__title=title
        self.__author=author

    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @book_id.setter
    def book_id(self,book_id):
        self.__book_id=book_id

    @title.setter
    def title(self,title):
        self.__title=title

    @author.setter
    def author(self,author):
        self.__author=author

    def __str__(self):
        return f"Book: {self.__book_id} - {self.__title} - {self.__author}"