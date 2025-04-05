
from src.domain import Driver, Order


class DriverRepository:
    def __init__(self, drivers_file):
        self.drivers_file = drivers_file

    def get_all_drivers(self):
        drivers = []
        with open(self.drivers_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                drivers.append(Driver(driver_id=int(parts[0]), name=parts[1]))
        return drivers

    def find_driver_by_id(self, driver_id):
        """
        Find a driver by theri id
        :param driver_id:
        """
        drivers = self.get_all_drivers()
        for driver in drivers:
            if driver.id == driver_id:
                return driver
        return None


class OrderRepository:
    def __init__(self, orders_file):
        self.orders_file = orders_file

    def get_all_orders(self):
        orders = []
        with open(self.orders_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                orders.append(Order(driver_id=int(parts[0]), distance=int(parts[1])))
        return orders

    def add_order(self, driver_id, distance):
        if distance < 1:
            raise ValueError("Distance must be at least 1 km.")
        with open(self.orders_file, 'a') as file:
            file.write(f"{driver_id},{distance}\n")


