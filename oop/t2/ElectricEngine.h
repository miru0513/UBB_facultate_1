#pragma once
#include "Engine.h"

class ElectricEngine : public Engine {
private:
    double autonomy;
public:
    ElectricEngine(double autonomy);
    double getPrice() const override;
    std::string toString() const override;
};