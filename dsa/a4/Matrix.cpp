#include "Matrix.h"
#include <exception>
#include <cmath>

using namespace std;

int Matrix::hash(int line, int column) const {
    int raw = line * numColumns + column;
    if (raw < 0) raw = -raw;
    return raw % capacity;
}


Matrix::Matrix(int nrLines, int nrCols) {
    if (nrLines <= 0 || nrCols <= 0)
        throw exception();

    numLines = nrLines;
    numColumns = nrCols;
    size = 0;
    capacity = 16; 
    maxLoadFactor = 0.75; 

  
    table = new Node * [capacity];
    for (int i = 0; i < capacity; i++) {
        table[i] = nullptr;
    }
}



void Matrix::resize() {
    int oldCapacity = capacity;
    capacity = capacity * 2; 

    Node** oldTable = table;
    table = new Node * [capacity];

    
    for (int i = 0; i < capacity; i++) {
        table[i] = nullptr;
    }

 
    for (int i = 0; i < oldCapacity; i++) {
        Node* current = oldTable[i];
        while (current != nullptr) {
            Node* next = current->next;

            
            int newIndex = hash(current->data.line, current->data.column);

            current->next = table[newIndex];
            table[newIndex] = current;

            current = next;
        }
    }

    delete[] oldTable;
}
//BC=WC=TC=Theta(1)
int Matrix::nrLines() const {
    return numLines;
}
//BC=WC=TC=Theta(1)
int Matrix::nrColumns() const {
    return numColumns;
}

//BC=Theta(1)
//WC=Theta(n)
//TC=O(n)
TElem Matrix::element(int i, int j) const {
    if (i < 0 || i >= numLines || j < 0 || j >= numColumns)
        throw exception();

    int index = hash(i, j);
    Node* current = table[index];

  
    while (current != nullptr) {
        if (current->data.line == i && current->data.column == j) {
            return current->data.value;
        }
        current = current->next;
    }


    return NULL_TELEM;
}

//BC=Theta(1)
//WC=Theta(n)
//TC=O(n)
TElem Matrix::modify(int i, int j, TElem e) {
    if (i < 0 || i >= numLines || j < 0 || j >= numColumns)
        throw exception();

    int index = hash(i, j);
    Node* current = table[index];
    Node* prev = nullptr;

    while (current != nullptr) {
        if (current->data.line == i && current->data.column == j) {
            TElem oldValue = current->data.value;

           
            if (e == NULL_TELEM) {
                if (prev == nullptr) {
                    table[index] = current->next;
                }
                else {
                    prev->next = current->next;
                }
                delete current;
                size--;
            }
            else {
                current->data.value = e;
            }

            return oldValue;
        }
        prev = current;
        current = current->next;
    }

    if (e != NULL_TELEM) {
        Triple newTriple(i, j, e);
        Node* newNode = new Node(newTriple);
        Node* curr = table[index];
        Node* prev = nullptr;

        
        while (curr != nullptr &&
            (curr->data.line < i ||
                (curr->data.line == i && curr->data.column < j))) {
            prev = curr;
            curr = curr->next;
        }

        newNode->next = curr;
        if (prev == nullptr) {
            table[index] = newNode;
        }
        else {
            prev->next = newNode;
        }

        size++;

        double loadFactor = static_cast<double>(size) / capacity;
        if (loadFactor > maxLoadFactor) {
            resize();
        }
    }


    return NULL_TELEM;
}

std::pair<int, int> Matrix::positionOf(TElem elem) const {
    for (int b = 0; b < capacity; ++b) {
        Node* current = table[b];
        while (current != nullptr) {
            if (current->data.value == elem) {
                return { current->data.line, current->data.column };
            }
            current = current->next;
        }
    }
    return { -1, -1 };
}






















// Destructor
Matrix::~Matrix() {
    // Free all allocated memory
    for (int i = 0; i < capacity; i++) {
        Node* current = table[i];
        while (current != nullptr) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }
    delete[] table;
}