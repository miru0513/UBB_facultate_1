#pragma once
#include "repository.h"
#include <algorithm>
class Service {
private:
    Repository& repo;

public:
    Service(Repository& repo);
    bool addSchool(const School& school);
    std::vector<School> getAllSchools() const;
    std::vector<School> getClosestSchools(double lat, double lon) const;
};