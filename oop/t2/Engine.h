#pragma once
#include <string>

class Engine {
public:
    virtual ~Engine() = default;
    virtual double getPrice() const = 0;
    virtual std::string toString() const = 0;
};