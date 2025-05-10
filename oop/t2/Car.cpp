#include "Car.h"
#include <sstream>

Car::Car(const std::string& bodyStyle, std::shared_ptr<Engine> engine)
    : bodyStyle(bodyStyle), engine(engine) {
}

double Car::computePrice() const {
    double base = (bodyStyle == "Sedan") ? 8000 : 9000;
    return base + engine->getPrice();
}

std::string Car::toString() const {
    std::ostringstream oss;
    oss << "Body Style: " << bodyStyle << "\nEngine Type: " << engine->toString()
        << "\nEngine Price: " << engine->getPrice() << "\nBase Price: " << computePrice();
    return oss.str();
}