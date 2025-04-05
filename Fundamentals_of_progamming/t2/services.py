class TaxiService:
    def __init__(self, driver_repo, order_repo):
        self.driver_repo = driver_repo
        self.order_repo = order_repo

    def add_order(self, driver_id, distance):
        """
        add an order
        :param driver_id: the id of the driver
        :param distance:  the distance traveled for the order
        """

        if distance < 1:
            raise ValueError("Distance must be at least 1 km.")
        driver = self.driver_repo.find_driver_by_id(driver_id)
        if not driver:
            raise ValueError("Driver ID does not exist.")
        self.order_repo.add_order(driver_id, distance)

    def get_all_drivers_with_orders(self):
        """
        gets all drivers +their orders.
        returns: driver information and orders
        """
        drivers = self.driver_repo.get_all_drivers()
        orders = self.order_repo.get_all_orders()
        result = {}
        for driver in drivers:
            result[driver.id] = {
                'name': driver.name,
                'orders': [order.distance for order in orders if order.driver_id == driver.id]
            }
        return result

    def compute_income(self, driver_id):
        """
        calculate the total income for a driver
        :param driver_id: the driver id
        :return: driver details and their income.
        """

        driver = self.driver_repo.find_driver_by_id(driver_id)
        if not driver:
            raise ValueError("Driver ID does not exist.")
        orders = self.order_repo.get_all_orders()
        total_income = sum(
            order.distance * 2.5 for order in orders if order.driver_id == driver_id
        )
        return {'id': driver.id, 'name': driver.name, 'income': total_income}


