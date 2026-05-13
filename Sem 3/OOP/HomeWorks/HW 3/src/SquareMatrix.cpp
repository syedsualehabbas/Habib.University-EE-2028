#include "SquareMatrix.hpp"

SquareMatrix::SquareMatrix(const int size):Matrix(size,size){}
SquareMatrix::SquareMatrix(const SquareMatrix& other){
    rows=other.rows; 
    cols=other.cols;
    for (int i=0; i<rows*cols; i++){
        elements[i] =other.elements[i];
    }
}

SquareMatrix SquareMatrix::operator+(const SquareMatrix& other) const{
    SquareMatrix output(rows);
    for (int i=0; i<rows*cols; i++){
        output.elements[i]=elements[i]+other.elements[i];
    }
    return output;
}

SquareMatrix SquareMatrix::operator-(const SquareMatrix& other) const{
    SquareMatrix output(rows);
    for (int i=0; i<rows*cols; i++){
        output.elements[i]=elements[i]-other.elements[i];
    }
    return output;
}

SquareMatrix SquareMatrix::operator*(const SquareMatrix& other) const{
    SquareMatrix output(rows);
    for (int i=0; i<rows; i++){
        for (int j=0; j<cols; j++){
            double sum=0;
            for (int k=0; k<cols; k++){
                sum += elements[i*cols+k]*other.elements[k*cols+j];
            }
            output.elements[i*cols+j]=sum;
        }
    }
    return output;
}

bool SquareMatrix::operator==(const SquareMatrix& other) const{
    for (int i=0; i<rows*cols; i++){
        if (elements[i]!= other.elements[i]){ 
        return false;
        }
    }
    return true;
}

double SquareMatrix::getElement(const int row, const int col) const{
    return Matrix::getElement(row,col);
}

void SquareMatrix::setElement(const int row, const int col, const double value){
    Matrix::setElement(row,col,value);
}
