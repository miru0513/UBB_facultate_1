#pragma once
#include <vector>
#include "school.h"

class Repository {
private:
    std::vector<School> schools;

public:
    bool addSchool(const School& school);
    const std::vector<School>& getAllSchools() const;
};