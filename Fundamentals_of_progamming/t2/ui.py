

from src.repository import DriverRepository, OrderRepository
from src.services import TaxiService


class TaxiUI:
    def __init__(self, taxi_service):
        self.taxi_service = taxi_service

    def menu(self):
        while True:
            print("\nMenuu")
            print("1. Add Order")
            print("2. Display All Drivers with Orders")
            print("3. Compute Driver Income")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_order_ui()
            elif choice == "2":
                self.display_all_drivers_with_orders()
            elif choice == "3":
                self.display_driver_income_ui()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice..")

    def display_all_drivers_with_orders(self):
        data = self.taxi_service.get_all_drivers_with_orders()
        for driver_id, details in data.items():
            print(f"Driver ID: {driver_id}, Name: {details['name']}, Orders: {details['orders']}")

    def display_driver_income_ui(self):
        try:
            driver_id = int(input("Enter Driver ID: "))
            income_data = self.taxi_service.compute_income(driver_id)
            print(f"Driver ID: {income_data['id']}, Name: {income_data['name']}, Income: {income_data['income']} RON")
        except ValueError as e:
            print(e)

    def add_order_ui(self):
        try:
            driver_id = int(input("Enter Driver ID: "))
            distance = int(input("Enter Distance Travelled (in km): "))
            self.taxi_service.add_order(driver_id, distance)
            print("Order added successfully!")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    drivers_file = "drivers.txt"
    orders_file = "orders.txt"

    driver_repo = DriverRepository(drivers_file)
    order_repo = OrderRepository(orders_file)
    taxi_service = TaxiService(driver_repo, order_repo)
    ui = TaxiUI(taxi_service)

    ui.menu()


