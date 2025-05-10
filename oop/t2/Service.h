#pragma once
#include <vector>
#include <memory>
#include "Car.h"

class Service {
private:
    std::vector<std::shared_ptr<Car>> cars;

public:
    void addCar(const std::shared_ptr<Car>& car);
    const std::vector<std::shared_ptr<Car>>& getAll() const;
    std::vector<std::shared_ptr<Car>> getCarsWithPriceLessThan(double price) const;
    void saveToFile(const std::string& filename, double price) const;
};
