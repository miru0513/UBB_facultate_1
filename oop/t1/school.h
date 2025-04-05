#pragma once
#include <string>

class School {
private:
    std::string name;
    double latitude;
    double longitude;
    std::string visitDate;

public:
    School(const std::string& name, double latitude, double longitude, const std::string& visitDate);
    ~School();

    std::string getName() const;
    double getLatitude() const;
    double getLongitude() const;
    std::string getVisitDate() const;

    bool equals(const School& other) const;
    double distanceTo(double lat, double lon) const;
};