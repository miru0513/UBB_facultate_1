#include <assert.h>
#include "Matrix.h"

using namespace std;

void testAll() { 
	Matrix m(4, 4);
	assert(m.nrLines() == 4);
	assert(m.nrColumns() == 4);	
	m.modify(1, 1, 5);
	assert(m.element(1, 1) == 5);
	TElem old = m.modify(1, 1, 6);
	assert(m.element(1, 2) == NULL_TELEM);
	assert(old == 5);

	Matrix n(4, 4);
	n.modify(0, 1, 10);
	n.modify(2, 2, 20);
	n.modify(3, 0, 10);  // duplicate value

	// Check 10 is found somewhere
	std::pair<int, int> pos = n.positionOf(10);
	bool ok = (pos.first == 0 && pos.second == 1) || (pos.first == 3 && pos.second == 0);
	assert(ok);

	// Check 20 is found
	std::pair<int, int> pos2 = n.positionOf(20);
	assert(pos2.first == 2 && pos2.second == 2);

	// Check value that doesn't exist
	std::pair<int, int> pos3 = n.positionOf(999);
	assert(pos3.first == -1 && pos3.second == -1);


}