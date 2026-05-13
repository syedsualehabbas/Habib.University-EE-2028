#include "DiagonalMatrix.hpp"

DiagonalMatrix::DiagonalMatrix(const int size):SquareMatrix(size){}

DiagonalMatrix::DiagonalMatrix(DiagonalMatrix const& other){
    rows=other.rows;
    cols=other.cols;
    elements=other.elements;
}

DiagonalMatrix DiagonalMatrix::operator+(const DiagonalMatrix& other) const{
    DiagonalMatrix output(rows);
    for (int i=0; i<rows; i++){
        output.elements[i]= elements[i]+ other.elements[i];
    }
    return output;
}

DiagonalMatrix DiagonalMatrix::operator-(const DiagonalMatrix& other) const{
    DiagonalMatrix output(rows);
    for (int i=0; i <rows; i++){
        output.elements[i]=elements[i]-other.elements[i];
    }
    return output;
}

DiagonalMatrix DiagonalMatrix::operator*(const DiagonalMatrix& other) const{
    DiagonalMatrix output(rows);
    for (int i = 0; i<rows; i++){
        output.elements[i] = elements[i]*other.elements[i];
    }
    return output;
}

bool DiagonalMatrix::operator==(const DiagonalMatrix& other) const{
    for (int i =0; i<rows; i++){
        if (elements[i] != other.elements[i]){
            return false;
        }
    }
    return true;
}

double DiagonalMatrix::getElement(const int row, const int col) const{
    if (row == col){
        return elements[row];
    }
    return 0.0;
}

void DiagonalMatrix::setElement(const int row, const int col, const double value){
    if (row == col){
        elements[row] = value;
    }
}