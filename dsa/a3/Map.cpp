#include "Map.h"
#include "MapIterator.h"
#include <exception>

Map::Map() {
    capacity = INITIAL_CAPACITY;
    elements = new TElem[capacity];
    next = new int[capacity];
    prev = new int[capacity];

    for (int i = 0; i < capacity - 1; i++) {
        next[i] = i + 1;
    }
    next[capacity - 1] = -1;

    for (int i = 0; i < capacity; i++) {
        prev[i] = i - 1;
    }

    head = -1;
    tail = -1;
    firstEmpty = 0;
    count = 0;
}

Map::~Map() {
    delete[] elements;
    delete[] next;
    delete[] prev;
}

void Map::resize() {
    int newCapacity = capacity * 2;
    TElem* newElements = new TElem[newCapacity];
    int* newNext = new int[newCapacity];
    int* newPrev = new int[newCapacity];

    for (int i = 0; i < capacity; i++) {
        newElements[i] = elements[i];
        newNext[i] = next[i];
        newPrev[i] = prev[i];
    }

    for (int i = capacity; i < newCapacity - 1; i++) {
        newNext[i] = i + 1;
        newPrev[i] = i - 1;
    }
    newNext[newCapacity - 1] = -1;

    delete[] elements;
    delete[] next;
    delete[] prev;

    elements = newElements;
    next = newNext;
    prev = newPrev;

    firstEmpty = capacity;
    capacity = newCapacity;
}

//BC=Theta(1)
//WC=Theta(n)
//TC=O(n)
TValue Map::add(TKey c, TValue v) {
    int current = head;
    while (current != -1 && elements[current].first != c) {
        current = next[current];
    }

    if (current != -1) {
        TValue oldValue = elements[current].second;
        elements[current].second = v;
        return oldValue;
    }

    if (firstEmpty == -1) {
        resize();
    }

    int newPosition = firstEmpty;
    firstEmpty = next[firstEmpty];

    elements[newPosition] = TElem(c, v);

    if (head == -1) {
        head = tail = newPosition;
        next[newPosition] = prev[newPosition] = -1;
    }
    else {
        next[tail] = newPosition;
        prev[newPosition] = tail;
        next[newPosition] = -1;
        tail = newPosition;
    }

    count++;
    return NULL_TVALUE;
}

//BC=Theta(1)
//WC=Theta(n)
//TC=O(n)
TValue Map::search(TKey c) const {
    int current = head;
    while (current != -1 && elements[current].first != c) {
        current = next[current];
    }

    if (current != -1) {
        return elements[current].second;
    }

    return NULL_TVALUE;
}

//BC=Theta(1)
//WC=Theta(n)
//TC=O(n)
TValue Map::remove(TKey c) {
    int current = head;
    while (current != -1 && elements[current].first != c) {
        current = next[current];
    }

    if (current == -1) {
        return NULL_TVALUE;
    }

    TValue value = elements[current].second;

    if (current == head) {
        head = next[head];
        if (head != -1) prev[head] = -1;
        else tail = -1;
    }
    else if (current == tail) {
        tail = prev[tail];
        if (tail != -1) next[tail] = -1;
    }
    else {
        next[prev[current]] = next[current];
        prev[next[current]] = prev[current];
    }

    next[current] = firstEmpty;
    firstEmpty = current;

    count--;

    return value;
}

//BC=WC=TC=Theta(1)
int Map::size() const {
    return count;
}

//BC=WC=TC=Theta(1)
bool Map::isEmpty() const {
    return count == 0;
}

//BC=WC=TC=Theta(1)
MapIterator Map::iterator() const {
    return MapIterator(*this);
}

//new functionality
//BC=WC=TC=Theta(n^2)
TValue Map::mostFrequent() const {
    if (isEmpty())
        return NULL_TVALUE;

    // First, copy all values into a temporary array
    int current = head;
    int n = 0;
    TValue* values = new TValue[count];

    while (current != -1) {
        values[n++] = elements[current].second;
        current = next[current];
    }

    // Now count frequencies manually
    int maxFreq = 0;
    TValue result = NULL_TVALUE;

    for (int i = 0; i < n; i++) {
        int freq = 1;
        for (int j = i + 1; j < n; j++) {
            if (values[i] == values[j]) {
                freq++;
            }
        }
        if (freq > maxFreq) {
            maxFreq = freq;
            result = values[i];
        }
    }

    delete[] values;
    return result;
}
