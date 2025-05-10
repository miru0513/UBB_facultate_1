#include "UI.h"
#include "Service.h"
#include "ElectricEngine.h"
#include "TurboEngine.h"
#include <memory>
#include <string>
#include <iostream>

int main() {
    Service service;

    // 3 hardcoded cars
    service.addCar(std::make_shared<Car>("Convertible", std::make_shared<TurboEngine>()));
    service.addCar(std::make_shared<Car>("Sedan", std::make_shared<TurboEngine>()));


    UI ui(service);
    ui.run();
    return 0;
}
