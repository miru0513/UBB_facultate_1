#pragma once

#include "SortedMultiMap.h"

class SMMIterator {
    friend class SortedMultiMap;

private:
    // DO NOT CHANGE THIS PART
    const SortedMultiMap& map;
    SMMIterator(const SortedMultiMap& map);

    // TODO - Representation
    int* stack;
    int top;
    int currentNode;
    int capacity;

public:
    void first();
    void next();
    bool valid() const;
    TElem getCurrent() const;
    ~SMMIterator();
};
