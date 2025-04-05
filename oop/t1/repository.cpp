#include "repository.h"


/*
* Adds a school to the repository.
* If the school already exists (based on name), it will not be added.
* Returns true if the school was added successfully, false if it already exists.
*/
bool Repository::addSchool(const School& school) {
	for (const auto& s : schools) {
		if (s.equals(school)) return false;
	}
	schools.push_back(school);
	return true;
}

/*
* Returns a constant reference to the vector of schools.
*/
const std::vector<School>& Repository::getAllSchools() const {
	return schools;
}