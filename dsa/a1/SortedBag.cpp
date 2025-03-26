#include "SortedBag.h"
#include "SortedBagIterator.h"



//BC=WC=AC=Theta(1)
SortedBag::SortedBag(Relation r) {
	this->relation = r;
	this->size_bag = 0;
	this->capacity = 1;
	this->elements = new TComp[this->capacity];
	
}

//BC=Theta(1) ->elementul e mai mare decat toate celalete
// WC=Theta(n) ->n=nr de elemente  TC=O(n)
void SortedBag::add(TComp e) {
	 if (this->size_bag == this->capacity) {
		this->capacity *= 2;
		TComp* new_elements = new TComp[this->capacity];
		for (int i = 0; i < this->size_bag; i++) {
			new_elements[i] = this->elements[i];
		}
		delete[] this->elements;
		this->elements = new_elements;
	}

	int i = this->size_bag - 1;
	while (i >= 0 && !this->relation(this->elements[i], e)) {
		this->elements[i + 1] = this->elements[i];
		i--;
	}
	this->elements[i + 1] = e;
	this->size_bag++;
}

//BC=Theta(1) ->elementul e pe prima pozitie
// WC=Theta(n) -> elemntul poate nu exista sau e ultimul  TC=O(n)
bool SortedBag::remove(TComp e) {
	for (int i = 0; i < this->size_bag; i++) {
		if (this->elements[i] == e) {
			for (int j = i; j < this->size_bag - 1; j++) {
				this->elements[j] = this->elements[j + 1];
			}
			this->size_bag--;
			return true;
		}
	}
	return false;
}

//BC=Theta(1) ->elementul e pe prima pozitie
// WC=TC=O(n) -> elemntul poate nu exista sau e ultimul
bool SortedBag::search(TComp elem) const {
	for (int i = 0; i < this->size_bag; i++) {
		if (this->elements[i] == elem) {
			return true;
		}
	}
	return false;
}

//BC=WC=TC=Theta(n) trebuie mers prin tot sirul orice elem ar fi
int SortedBag::nrOccurrences(TComp elem) const {
	int count = 0;
	for (int i = 0; i < this->size_bag; i++) {
		if (this->elements[i] == elem) {
			count++;
		}
	}
	return count;
}


//BC=WC=TC=Theta(1)
int SortedBag::size() const {
	return this->size_bag;
}

//BC=WC=TC=Theta(1)
bool SortedBag::isEmpty() const {
	return this->size_bag == 0;
}

//BC=WC=TC=Theta(1)
SortedBagIterator SortedBag::iterator() const {
	return SortedBagIterator(*this);
}

//BC=WC=TC=Theta(1) 
SortedBag::~SortedBag() {
	delete[] this->elements;
}


//neu functionality
void SortedBag::intersection(const SortedBag& b) {
    // sir pentru rezultat
    TComp* result = new TComp[this->capacity];
    int resultSize = 0;


    TComp* uniqueElements = new TComp[this->size_bag];
    int uniqueCount = 0;

    for (int i = 0; i < this->size_bag; i++) {
        
        bool found = false;
        for (int j = 0; j < uniqueCount; j++) {
            if (this->elements[i] == uniqueElements[j]) {
                found = true;
                break;
            }
        }

        if (!found) {
            uniqueElements[uniqueCount] = this->elements[i];
            uniqueCount++;
        }
    }
    for (int i = 0; i < uniqueCount; i++) {
        TComp currentElement = uniqueElements[i];

        // apritiile in fieacre bag
        int countInThis = this->nrOccurrences(currentElement);
        int countInB = b.nrOccurrences(currentElement);

        if (countInB > 0) {
            int minCount;
            if (countInThis < countInB) {
                minCount = countInThis;
            }
            else {
                minCount = countInB;
            }
            for (int j = 0; j < minCount; j++) {
                if (resultSize == this->capacity) {
                    this->capacity *= 2;
                    TComp* newResult = new TComp[this->capacity];
                    for (int k = 0; k < resultSize; k++) {
                        newResult[k] = result[k];
                    }
                    delete[] result;
                    result = newResult;
                }

                result[resultSize] = currentElement;
                resultSize++;
            }
        }
    }


    delete[] this->elements;
    this->elements = result;
    this->size_bag = resultSize;

    delete[] uniqueElements;
}