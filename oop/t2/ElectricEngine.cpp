#include "ElectricEngine.h"
#include <sstream>

ElectricEngine::ElectricEngine(double autonomy) : autonomy(autonomy) {}

double ElectricEngine::getPrice() const {
    return 3000 + autonomy * 0.01;
}

std::string ElectricEngine::toString() const {
    std::ostringstream oss;
    oss << "Electric, Autonomy: " << autonomy;
    return oss.str();
}
