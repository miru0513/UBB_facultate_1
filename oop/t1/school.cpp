#include "school.h"
#include <cmath>


School::School(const std::string& name, double latitude, double longitude, const std::string& visitDate)
    : name(name), latitude(latitude), longitude(longitude), visitDate(visitDate) {
}

School::~School() {}

std::string School::getName() const { return name; }
double School::getLatitude() const { return latitude; }
double School::getLongitude() const { return longitude; }
std::string School::getVisitDate() const { return visitDate; }

bool School::equals(const School& other) const {
    return name == other.name;
}

double School::distanceTo(double lat, double lon) const {
    return std::sqrt((latitude - lat) * (latitude - lat) + (longitude - lon) * (longitude - lon));
}
