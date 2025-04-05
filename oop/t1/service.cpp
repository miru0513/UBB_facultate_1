
#include "service.h"
#include <algorithm>

Service::Service(Repository& repo) : repo(repo) {}


/*
 * Adds a school to the repository.
 * Returns true if the school was added successfully, false if it already exists.
 */ 
bool Service::addSchool(const School& school) {
    return repo.addSchool(school);
}

/*
 * Returns a vector of all schools in the repository.
*/
std::vector<School> Service::getAllSchools() const {
    return repo.getAllSchools();
}


/*
 * Returns a vector of the 3 closest schools to the given latitude and longitude.
 * The schools are sorted by distance, and then by name.
 * lat and lon are the coordinates of the user's location.
*/
std::vector<School> Service::getClosestSchools(double lat, double lon) const {
    std::vector<School> sorted = repo.getAllSchools();
    std::sort(sorted.begin(), sorted.end(), [lat, lon](const School& a, const School& b) {
        return a.distanceTo(lat, lon) < b.distanceTo(lat, lon);
        });
    std::vector<School> result;
    for (size_t i = 0; i < std::min(size_t(3), sorted.size()); ++i) {
        result.push_back(sorted[i]);
    }
    std::sort(result.begin(), result.end(), [](const School& a, const School& b) {
        return a.getName() < b.getName();
        });
    return result;
}

