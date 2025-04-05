class Driver:
    def __init__(self, driver_id, name):
        self.__id = driver_id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return f"Driver(ID: {self.id}, Name: {self.name})"


class Order:
    def __init__(self, driver_id, distance):
        self.__driver_id = driver_id
        self.__distance = distance

    @property
    def driver_id(self):
        return self.__driver_id

    @driver_id.setter
    def driver_id(self, value):
        self.__driver_id = value

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, value):
        if value < 1:
            raise ValueError("Distance must be at least 1 km.")
        self.__distance = value

    def __str__(self):
        return f"Order(Driver ID: {self.driver_id}, Distance: {self.distance} km)"

