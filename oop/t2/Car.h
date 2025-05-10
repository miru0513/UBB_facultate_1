#pragma once
#include <string>
#include <memory>
#include "Engine.h"

class Car {
private:
    std::string bodyStyle;
    std::shared_ptr<Engine> engine;

public:
    Car(const std::string& bodyStyle, std::shared_ptr<Engine> engine);
    double computePrice() const;
    std::string toString() const;
};