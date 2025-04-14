#include "ListIterator.h"
#include "SortedIndexedList.h"
#include <exception>
using namespace std;

//BC=WC=TC=Theta(1)
ListIterator::ListIterator(const SortedIndexedList& list) : list(list) {
    currentNode = list.head;
}
//BC=WC=TC=Theta(1)
void ListIterator::first() {
    currentNode = list.head;
}
//BC=WC=TC=Theta(1)
void ListIterator::next() {
    if (!valid()) {
        throw std::exception();
    }
    currentNode = currentNode->next;
}
//BC=WC=TC=Theta(1)
bool ListIterator::valid() const {
    return currentNode != nullptr;
}
//BC=WC=TC=Theta(1)
TComp ListIterator::getCurrent() const {
    if (!valid()) {
        throw std::exception();
    }
    return currentNode->value;
}


