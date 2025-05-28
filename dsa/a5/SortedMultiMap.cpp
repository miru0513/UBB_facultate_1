#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <iostream>
#include <vector>
#include <exception>
using namespace std;

SortedMultiMap::SortedMultiMap(Relation r) {
    // TODO - Implementation
    this->capacity = 10;
    this->keys = new TKey[capacity];
    this->values = new TValue[capacity];
    this->left = new int[capacity];
    this->right = new int[capacity];
    this->root = -1;
    this->firstFree = 0;
    this->sizeMap = 0;
    this->relation = r;

    for (int i = 0; i < capacity; i++) {
        left[i] = right[i] = -1;
    }
}

//BC=theta(log n)
//WC=theta(n)
//TC=O(log n)
void SortedMultiMap::add(TKey c, TValue v) {
    // TODO - Implementation
    if (firstFree == capacity) {
        int newCapacity = 2 * capacity;
        TKey* newKeys = new TKey[newCapacity];
        TValue* newValues = new TValue[newCapacity];
        int* newLeft = new int[newCapacity];
        int* newRight = new int[newCapacity];

        for (int i = 0; i < capacity; i++) {
            newKeys[i] = keys[i];
            newValues[i] = values[i];
            newLeft[i] = left[i];
            newRight[i] = right[i];
        }

        for (int i = capacity; i < newCapacity; i++) {
            newLeft[i] = newRight[i] = -1;
        }

        delete[] keys;
        delete[] values;
        delete[] left;
        delete[] right;

        keys = newKeys;
        values = newValues;
        left = newLeft;
        right = newRight;
        capacity = newCapacity;
    }

    int newNode = firstFree++;
    keys[newNode] = c;
    values[newNode] = v;
    left[newNode] = right[newNode] = -1;

    if (root == -1) {
        root = newNode;
    }
    else {
        int current = root;
        int parent = -1;
        while (current != -1) {
            parent = current;
            if (relation(c, keys[current])) {
                current = left[current];
            }
            else {
                current = right[current];
            }
        }

        if (relation(c, keys[parent])) {
            left[parent] = newNode;
        }
        else {
            right[parent] = newNode;
        }
    }

    sizeMap++;
}

// BC=theta(log n)
// WC=theta(n)
// TC=O(log n+m) n= number of pairs m=nr of pairs with the searched key
vector<TValue> SortedMultiMap::search(TKey c) const {
  
    TValue* tempResults = new TValue[sizeMap];
    int count = 0;

    int current = root;
    while (current != -1) {
        if (keys[current] == c) {
            tempResults[count++] = values[current];
            current = left[current];
        }
        else if (relation(c, keys[current])) {
            current = left[current];
        }
        else {
            current = right[current];
        }
    }

    
    vector<TValue> result(count);
    for (int i = 0; i < count; ++i) {
        result[i] = tempResults[i];
    }

    delete[] tempResults;
    return result;
}

// BC=theta(log n)
// WC=theta(n)
// TC=O(log n)
bool SortedMultiMap::remove(TKey c, TValue v) {
    // TODO - Implementation
    int current = root;
    int parent = -1;
    bool isLeftChild = false;

    while (current != -1 && !(keys[current] == c && values[current] == v)) {
        parent = current;
        if (relation(c, keys[current])) {
            current = left[current];
            isLeftChild = true;
        }
        else {
            current = right[current];
            isLeftChild = false;
        }
    }

    if (current == -1) return false;  // not found

    // Case 1: no children
    if (left[current] == -1 && right[current] == -1) {
        if (current == root) root = -1;
        else if (isLeftChild) left[parent] = -1;
        else right[parent] = -1;
    }
    // Case 2: one child
    else if (left[current] == -1) {
        if (current == root) root = right[current];
        else if (isLeftChild) left[parent] = right[current];
        else right[parent] = right[current];
    }
    else if (right[current] == -1) {
        if (current == root) root = left[current];
        else if (isLeftChild) left[parent] = left[current];
        else right[parent] = left[current];
    }
    // Case 3: two children
    else {
        int succParent = current;
        int succ = right[current];
        while (left[succ] != -1) {
            succParent = succ;
            succ = left[succ];
        }

        keys[current] = keys[succ];
        values[current] = values[succ];

        if (succParent == current) {
            right[succParent] = right[succ];
        }
        else {
            left[succParent] = right[succ];
        }
    }

    sizeMap--;
    return true;
}

//new functionality
int SortedMultiMap::getValueRange() const {
    if (sizeMap == 0)
        return -1;

  
    int* stack = new int[sizeMap + 1];
    int top = -1;
    int current = root;

    
    int minValue = values[root];
    int maxValue = values[root];

    while (current != -1 || top >= 0) {
        
        while (current != -1) {
            stack[++top] = current;
            current = left[current];
        }

       
        current = stack[top--];
        int val = values[current];
        if (val < minValue) minValue = val;
        if (val > maxValue) maxValue = val;

       
        current = right[current];
    }

    delete[] stack;
    return maxValue - minValue;
}



//BC=WC=TC=Theta(1)
int SortedMultiMap::size() const {
    // TODO - Implementation
    return sizeMap;
}
//BC=WC=TC=Theta(1)
bool SortedMultiMap::isEmpty() const {
    // TODO - Implementation
    return sizeMap == 0;
}
//BC=WC=TC=Theta(1)
SMMIterator SortedMultiMap::iterator() const {
    return SMMIterator(*this);
}

SortedMultiMap::~SortedMultiMap() {
    // TODO - Implementation
    delete[] keys;
    delete[] values;
    delete[] left;
    delete[] right;
}
