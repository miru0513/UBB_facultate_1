#include "ListIterator.h"
#include "SortedIndexedList.h"
#include <iostream>
using namespace std;
#include <exception>

// BC = WC = TC = Theta(1)
SortedIndexedList::SortedIndexedList(Relation r) {
    head = nullptr;
    listSize = 0;
    relation = r;
}

// BC = WC = TC = theta(1)
int SortedIndexedList::size() const {
    return listSize;
}

// BC = WC = TC = theta(1)
bool SortedIndexedList::isEmpty() const {
    return listSize == 0;
}

//BC = theta(1), WC =theta(n)  ,TC=O(n)
TComp SortedIndexedList::getElement(int pos) const {
    if (pos < 0 || pos >= listSize) {
        throw exception();
    }
    Node* current = head;
    int index = 0;
    while (current != nullptr && index < pos) {
        current = current->next;
        index++;
    }
    return current->value;
}

//BC = theta(1), WC =theta(n)  ,TC=O(n)
void SortedIndexedList::add(TComp e) {
    Node* newNode = new Node{ e, nullptr };
    if (head == nullptr || relation(e, head->value)) {
        newNode->next = head;
        head = newNode;
    }
    else {
        Node* current = head;
        while (current->next != nullptr && relation(current->next->value, e)) {
            current = current->next;
        }
        newNode->next = current->next;
        current->next = newNode;
    }
    listSize++;
}
//BC = theta(1), WC =theta(n)  ,TC=O(n)
TComp SortedIndexedList::remove(int pos) {
    if (pos < 0 || pos >= listSize) {
        throw exception();
    }
    Node* toDelete = nullptr;
    TComp removedValue;
    if (pos == 0) {
        toDelete = head;
        head = head->next;
    }
    else {
        Node* prev = head;
        for (int i = 0; i < pos - 1; ++i) {
            prev = prev->next;
        }
        toDelete = prev->next;
        prev->next = toDelete->next;
    }
    removedValue = toDelete->value;
    delete toDelete;
    listSize--;
    return removedValue;
}

//BC = theta(1), WC =theta(n)  ,TC=O(n)
int SortedIndexedList::search(TComp e) const {
    Node* current = head;
    int index = 0;
    while (current != nullptr) {
        if (current->value == e) {
            return index;
        }
        current = current->next;
        index++;
    }
    return -1;
}

// BC = WC = TC = theta(n)
SortedIndexedList::~SortedIndexedList() {
    Node* current = head;
    while (current != nullptr) {
        Node* next = current->next;
        delete current;
        current = next;
    }
}

//BC = WC = TC = theta(1)
ListIterator SortedIndexedList::iterator(){
	return ListIterator(*this);
}

//new functionality
//BC=Theta(1)
//WC=Theta(n)
//TC=O(end+1)   
void SortedIndexedList::removeBetween(int start, int end) {
    if (start < 0 || end >= listSize || start > end) {
        throw std::exception();
    }

 
    if (start == 0) {
        Node* current = head;
        for (int i = start; i <= end; i++) {
            Node* toDelete = current;
            current = current->next;
            delete toDelete;
        }
        head = current;
    }
    else {
        Node* prev = head;
        for (int i = 0; i < start - 1; i++) {
            prev = prev->next;
        }

        Node* current = prev->next;
        for (int i = start; i <= end; i++) {
            Node* toDelete = current;
            current = current->next;
            delete toDelete;
        }

        prev->next = current;
    }

    listSize -= (end - start + 1);
}
