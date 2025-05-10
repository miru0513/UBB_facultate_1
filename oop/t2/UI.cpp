#include "UI.h"
#include "ElectricEngine.h"
#include "TurboEngine.h"
#include <iostream>
#include <memory>
#include <string>
#include <iostream>


UI::UI(Service & service) : service(service) {}

void UI::run() {
    while (true) {
        std::cout << "\n1. Add new car\n2. Show all cars\n3. Save cars cheaper than price\n0. Exit\nChoice: ";
        int cmd; std::cin >> cmd;
        if (cmd == 0) break;
        if (cmd == 1) {
            std::string style; std::cout << "Body style (Sedan/Convertible): "; std::cin >> style;
            std::cout << "Engine type (1 = Electric, 2 = Turbo): "; int type; std::cin >> type;

            std::shared_ptr<Engine> engine;
            if (type == 1) {
                double autonomy; std::cout << "Autonomy: "; std::cin >> autonomy;
                engine = std::make_shared<ElectricEngine>(autonomy);
            }
            else if (type == 2) {
                engine = std::make_shared<TurboEngine>();
            }

           
            else {
                std::cout << "Invalid engine type.\n"; continue;
            }

            auto car = std::make_shared<Car>(style, engine);
            service.addCar(car);
            std::cout << "Car added. Price: " << car->computePrice() << "\n";

        }
        else if (cmd == 2) {
            for (const auto& c : service.getAll()) {
                std::cout << c->toString() << "\n\n";
            }
        }
        else if (cmd == 3) {
            double price; std::cout << "Max price: "; std::cin >> price;
            service.saveToFile("cars.txt", price);
            std::cout << "Cars saved to cars.txt\n";
        }
    }
}