#pragma once
#include "Service.h"

class UI {
private:
    Service& service;

public:
    UI(Service& service);
    void run();
};