import unittest

from src.domain import Driver, Order
from src.repository import OrderRepository, DriverRepository
from src.services import TaxiService


class TestTaxiManagement(unittest.TestCase):

    def setUp(self):
        self.drivers = [
            Driver(1, "Alex"),
            Driver(2, "Ion"),
            Driver(3, "Maria")
        ]

        self.orders = [
            Order(1, 10),
            Order(2, 8),
            Order(1, 5)
        ]

        self.driver_repo = DriverRepository(None)
        self.order_repo = OrderRepository(None)


        self.driver_repo.get_all_drivers = lambda: self.drivers
        self.driver_repo.find_driver_by_id = lambda driver_id: next((d for d in self.drivers if d.id == driver_id), None)

        self.order_repo.get_all_orders = lambda: self.orders
        self.order_repo.add_order = lambda driver_id, distance: self.orders.append(Order(driver_id, distance))

        self.service = TaxiService(self.driver_repo, self.order_repo)

    def test_add_order_success(self):
        self.service.add_order(1, 15)


    def test_add_order_invalid_distance(self):
        with self.assertRaises(ValueError):
            self.service.add_order(1, 0)

    def test_add_order_invalid_driver(self):
        with self.assertRaises(ValueError):
            self.service.add_order(99, 10)

    def test_get_all_drivers_with_orders(self):
        result = self.service.get_all_drivers_with_orders()
        self.assertEqual(len(result), 3)



    def test_compute_income_invalid_driver(self):
        with self.assertRaises(ValueError):
            self.service.compute_income(99)

if __name__ == "__main__":
    unittest.main()
