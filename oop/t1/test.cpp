
#include "test.h"
#include "service.h"
#include "repository.h"
#include <cassert>
#include <iostream>

void testAddSchoolSuccess() {
    Repository repo;
    Service service(repo);
    bool added = service.addSchool(School("TestSchool", 46.70, 23.50, "01.01.2025"));
    assert(added == true);
    assert(service.getAllSchools().size() == 1);
    std::cout << "Test addSchoolSuccess passed.\n";
}
/*
int main() {
	testAddSchoolSuccess();
	
	return 0;
}
*/