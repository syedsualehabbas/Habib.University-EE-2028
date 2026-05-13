#include "Matrix.hpp"

Matrix::Matrix(const int rows, const int cols){
    this->rows = rows;
    this->cols = cols;
    elements.resize(rows*cols, 0.0);
}

Matrix::Matrix(Matrix const& other){
    rows=other.rows;
    cols=other.cols;
    elements=other.elements;
}

Matrix Matrix::operator+(const Matrix& other) const{
    Matrix output(rows, cols);
    int size=rows*cols;
    for (int i=0; i<size; i++){
        output.elements[i]=elements[i]+other.elements[i];
    }
    return output;
}

Matrix Matrix::operator-(const Matrix& other) const{
    Matrix output(rows, cols);
    int size=rows*cols;
    for (int i = 0; i<size; i++){
        output.elements[i]=elements[i]-other.elements[i];
    }
    return output;
}

Matrix Matrix::operator*(const Matrix& other)const{
    if (cols != other.rows)
        return Matrix(0, 0);
    Matrix output(rows, other.cols);
    for (int i=0; i<rows; i++){
        for (int j=0; j<other.cols; j++) {
            double sum =0;
            for (int k=0; k<cols; k++)
                sum += elements[i*cols+k]*other.elements[k*other.cols+j];
            output.elements[i*other.cols+j]=sum;
        }
    }
    return output;
}
bool Matrix::operator==(const Matrix& other) const{
    int size=rows*cols;
    for (int i=0; i<size; i++){
        if (elements[i] != other.elements[i])
            return false;
    }
    return true;
}
double Matrix::getElement(const int row, const int col) const{
    return elements[row*cols+col];
}
void Matrix::setElement(const int row, const int col, const double value){
    elements[row*cols+col]=value;
}
int Matrix::getRows() const{
    return rows;
}
int Matrix::getCols() const{
    return cols;
}
int Matrix::getElementsSize() const{
    return rows*cols;
}