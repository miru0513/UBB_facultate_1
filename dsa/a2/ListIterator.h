#pragma once
#include "SortedIndexedList.h"


//DO NOT CHANGE THIS PART
class ListIterator{
	friend class SortedIndexedList;
private:
	const SortedIndexedList& list;
	SortedIndexedList::Node* currentNode;
	ListIterator(const SortedIndexedList& list);



public:
	void first();
	void next();
	bool valid() const;
    TComp getCurrent() const;
};


