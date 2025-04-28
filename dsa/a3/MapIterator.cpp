#include "Map.h"
#include "MapIterator.h"
#include <exception>
using namespace std;

//BC=WC=TC=Theta(1)
MapIterator::MapIterator(const Map& d) : map(d) {
    
    first();
}

//BC=WC=TC=Theta(1)
void MapIterator::first() {
    
    currentPosition = map.head;
}

//BC=WC=TC=Theta(1)
void MapIterator::next() {
    
    if (!valid()) {
        throw exception();
    }

    
    currentPosition = map.next[currentPosition];
}

//BC=WC=TC=Theta(1)
TElem MapIterator::getCurrent() {
    
    if (!valid()) {
        throw exception();
    }

  
    return map.elements[currentPosition];
}

//BC=WC=TC=Theta(1)
bool MapIterator::valid() const {
    
    return currentPosition != -1;
}