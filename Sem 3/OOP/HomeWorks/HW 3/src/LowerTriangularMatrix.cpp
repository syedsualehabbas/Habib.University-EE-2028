#include "LowerTriangularMatrix.hpp"
using namespace std;

LowerTriangularMatrix::LowerTriangularMatrix(const int size):SquareMatrix(size) {}

LowerTriangularMatrix::LowerTriangularMatrix(const LowerTriangularMatrix& other) {
    rows=other.rows; 
    cols=other.cols;
    for (int i=0; i<rows*cols; i++){
        elements[i]=other.elements[i];
    }
}

LowerTriangularMatrix LowerTriangularMatrix::operator+(const LowerTriangularMatrix& other) const{
    LowerTriangularMatrix output(rows);
    for (int i=0; i<rows; i++){
        for (int j=0; j<=i; j++){
            output.elements[i*cols+j]=elements[i*cols+j]+other.elements[i*cols+j];
        }
    }
    return output;
}

LowerTriangularMatrix LowerTriangularMatrix::operator-(const LowerTriangularMatrix& other) const{
    LowerTriangularMatrix output(rows);
    for (int i=0; i<rows; i++){
        for (int j=0; j<=i; j++){
            output.elements[i*cols+j]= elements[i*cols+j]-other.elements[i*cols+j];
        }
    }
    return output;
}

LowerTriangularMatrix LowerTriangularMatrix::operator*(const LowerTriangularMatrix& other) const{
    LowerTriangularMatrix output(rows);
    for (int i=0; i<rows; i++){
        for (int j=0; j<=i; j++){
            double sum=0;
            for (int k=j; k<=i; k++){ 
                sum+=elements[i*cols+k]*other.elements[k*cols+j];
            }
            output.elements[i*cols+j]=sum;
        }
    }
    return output;
}

bool LowerTriangularMatrix::operator==(const LowerTriangularMatrix& other) const{
    for (int i = 0; i<rows; i++){
        for (int j=0; j<=i; j++){
            if (elements[i*cols+j]!= other.elements[i*cols+j]){
                return false;
            }
        }
    }
    return true;
}

double LowerTriangularMatrix::getElement(const int row, const int col) const{
    return (col <=row) ? elements[row*cols+col]:0.0;
}

void LowerTriangularMatrix::setElement(const int row, const int col, const double value){
    if (col<=row){
        elements[row*cols+col]=value;
    }
}
