
 class Book:
    def __init__(self, isbn ,author ,title):
         self.__isbn = isbn
         self.__author = author
         self.__title = title

    @property
    def isbn(self):
        return self.__isbn

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn

    @author.setter
    def author(self, author):
        self.__author = author

    @title.setter
    def title(self, title):
        self.__title = title

    def __str__(self):
        return  f'isbn:{self.isbn} author:{self.author} title:{self.title}'





