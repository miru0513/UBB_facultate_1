#include "ui.h"
#include <iostream>

UI::UI(Service& service) : service(service) {}

void UI::run() {
    int choice;
    do {
        std::cout << "1. Add school\n2. Show all schools\n3. Show 3 closest schools\n0. Exit\nChoice: ";
        std::cin >> choice;
        if (choice == 1) {
            std::string name, date;
            double lat, lon;
            std::cout << "Name: "; std::cin >> name;
            std::cout << "Latitude: "; std::cin >> lat;
            std::cout << "Longitude: "; std::cin >> lon;
            std::cout << "Visit date (DD.MM.YYYY): "; std::cin >> date;
            if (service.addSchool(School(name, lat, lon, date)))
                std::cout << "School added.\n";
            else
                std::cout << "Duplicate school. Not added.\n";
        }
        else if (choice == 2) {
            for (const auto& s : service.getAllSchools()) {
                std::cout << s.getName() << " | " << s.getLatitude() << ", " << s.getLongitude()
                    << " | " << s.getVisitDate() << "\n";
            }
        }
        else if (choice == 3) {
            double lat, lon;
            std::cout << "Enter your latitude: "; std::cin >> lat;
            std::cout << "Enter your longitude: "; std::cin >> lon;
            auto closest = service.getClosestSchools(lat, lon);
            for (const auto& s : closest) {
                std::cout << s.getName() << " | " << s.getLatitude() << ", " << s.getLongitude()
                    << " | " << s.getVisitDate() << "\n";
            }
        }
    } while (choice != 0);
}