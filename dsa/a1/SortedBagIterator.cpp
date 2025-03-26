#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

//BC=WC=TC=Theta(1)
SortedBagIterator::SortedBagIterator(const SortedBag& b) : bag(b) {
	this->current = 0;
}


//BC=WC=TC=Theta(1)
TComp SortedBagIterator::getCurrent() {
	if (!valid()) {
		throw exception();
	}
	return bag.elements[current];
}


//BC=WC=TC=Theta(1)
bool SortedBagIterator::valid() {
	 return this->current <this->bag.size_bag;
}


//BC=WC=TC=Theta(1)
void SortedBagIterator::next() {
	if (!valid()) {
		throw exception();
	}
	this->current++;
}


//BC=WC=TC=Theta(1)
void SortedBagIterator::first() {
	this->current = 0;
}



