#include "TurboEngine.h"
#include <sstream>

TurboEngine::TurboEngine() {}

double TurboEngine::getPrice() const {
    return 3000;
}

std::string TurboEngine::toString() const {
    return "Turbo";
}
