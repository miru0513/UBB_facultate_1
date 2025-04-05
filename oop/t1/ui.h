#pragma once
#include "service.h"

class UI {
private:
    Service& service;

public:
    UI(Service& service);
    void run();
};