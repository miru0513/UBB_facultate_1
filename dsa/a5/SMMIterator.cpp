#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <exception>
using namespace std;

SMMIterator::SMMIterator(const SortedMultiMap& d) : map(d) {
    // TODO - Implementation
    capacity = map.sizeMap + 10;
    stack = new int[capacity];
    top = -1;
    currentNode = -1;
    first();
}

void SMMIterator::first() {
    // TODO - Implementation
    top = -1;
    int node = map.root;
    while (node != -1) {
        stack[++top] = node;
        node = map.left[node];
    }

    if (top >= 0)
        currentNode = stack[top--];
    else
        currentNode = -1;
}

void SMMIterator::next() {
    // TODO - Implementation
    if (!valid()) throw exception();

    int node = map.right[currentNode];
    while (node != -1) {
        stack[++top] = node;
        node = map.left[node];
    }

    if (top >= 0)
        currentNode = stack[top--];
    else
        currentNode = -1;
}

bool SMMIterator::valid() const {
    // TODO - Implementation
    return currentNode != -1;
}

TElem SMMIterator::getCurrent() const {
    // TODO - Implementation
    if (!valid()) throw exception();
    return make_pair(map.keys[currentNode], map.values[currentNode]);
}

SMMIterator::~SMMIterator() {
    
    delete[] stack;
}
