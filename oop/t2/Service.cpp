#include "Service.h"
#include <fstream>
#include <algorithm>

void Service::addCar(const std::shared_ptr<Car>& car) {
    cars.push_back(car);
}

const std::vector<std::shared_ptr<Car>>& Service::getAll() const {
    return cars;
}

std::vector<std::shared_ptr<Car>> Service::getCarsWithPriceLessThan(double price) const {
    std::vector<std::shared_ptr<Car>> result;
    for (const auto& c : cars) {
        if (c->computePrice() < price) {
            result.push_back(c);
        }
    }
    return result;
}

void Service::saveToFile(const std::string& filename, double price) const {
    auto filtered = getCarsWithPriceLessThan(price);
    std::sort(filtered.begin(), filtered.end(), [](const auto& a, const auto& b) {
        return a->computePrice() < b->computePrice();
        });
    std::ofstream fout(filename);
    for (const auto& c : filtered) {
        fout << c->toString() << "\n\n";
    }
    fout.close();
}