#pragma once
#include <utility>

//DO NOT CHANGE THIS PART
typedef int TElem;
#define NULL_TELEM 0

class Matrix {
private:
    // Triple structure to store <line, column, value>
    struct Triple {
        int line;
        int column;
        TElem value;

        Triple(int l, int c, TElem v) : line(l), column(c), value(v) {}

    };

   
    struct Node {
        Triple data;
        Node* next;

        Node(const Triple& t) : data(t), next(nullptr) {}
    };

   
    Node** table;
    int capacity;
    int size;
    int numLines;
    int numColumns;
    double maxLoadFactor;

    // Hash function
    int hash(int i, int j) const;

    // Resize and rehash the table
    void resize();

public:
    // Constructor
    Matrix(int nrLines, int nrCols);

    // Destructor
    ~Matrix();

    // Returns the number of lines
    int nrLines() const;

    // Returns the number of columns
    int nrColumns() const;

    // Returns the element from line i and column j (indexing starts from 0)
    // Throws exception if (i,j) is not a valid position in the Matrix
    TElem element(int i, int j) const;

    // Modifies the value from line i and column j
    // Returns the previous value from the position
    // Throws exception if (i,j) is not a valid position in the Matrix
    TElem modify(int i, int j, TElem e);

    //new functionality
    std::pair<int, int> positionOf(TElem elem) const;



};