#include "UpperTriangularMatrix.hpp"
using namespace std;

UpperTriangularMatrix::UpperTriangularMatrix(const int size):SquareMatrix(size){}

UpperTriangularMatrix::UpperTriangularMatrix(const UpperTriangularMatrix& other){
    rows= other.rows; 
    cols=other.cols;
    for (int i=0; i<rows*cols; i++){
        elements[i]=other.elements[i];
    }
}

UpperTriangularMatrix UpperTriangularMatrix::operator+(const UpperTriangularMatrix& other) const{
    UpperTriangularMatrix output(rows);
    for (int i=0; i<rows; i++){
        for (int j=i; j<cols; j++){
            output.elements[i*cols+j] =elements[i*cols+j]+ other.elements[i*cols+j];
        }
    }
    return output;
}

UpperTriangularMatrix UpperTriangularMatrix::operator-(const UpperTriangularMatrix& other) const{
    UpperTriangularMatrix output(rows);
    for (int i=0;  i<rows;i++){
        for (int j=i; j<cols; j++){
            output.elements[i*cols+j]=elements[i*cols+j]-other.elements[i*cols+j];
        }
    }
    return output;
}

UpperTriangularMatrix UpperTriangularMatrix::operator*(const UpperTriangularMatrix& other) const{
    UpperTriangularMatrix output(rows);
    for (int i=0; i<rows; i++){
        for (int j=i; j<cols; j++){
            double sum = 0;
            for (int k=i; k <= j; k++){
                sum += elements[i*cols+k]*other.elements[k*cols+j];
            }
            output.elements[i*cols+j]=sum;
        }
    }
    return output;
}

bool UpperTriangularMatrix::operator==(const UpperTriangularMatrix& other) const {
    for (int i=0; i<rows; i++){
        for (int j=i; j<cols; j++){
            if (elements[i*cols+j] !=other.elements[i*cols+j]){
                return false;
            }
        }
    }
    return true;
}

double UpperTriangularMatrix::getElement(const int row, const int col) const {
    return (row<=col) ? elements[row*cols+col]:0.0;
}

void UpperTriangularMatrix::setElement(const int row, const int col, const double value) {
    if (row<=col) elements[row*cols+col]=value;
}
