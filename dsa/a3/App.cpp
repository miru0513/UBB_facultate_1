#include "ExtendedTest.h"
#include "ShortTest.h"

#include "Map.h"


#include <iostream>
using namespace std;


int main() {
	testAll();
	testMostFrequent();
	testAllExtended();

	cout << "That's all!" << endl;
	system("pause");
	return 0;
}


