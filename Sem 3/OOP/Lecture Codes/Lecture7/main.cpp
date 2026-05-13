#include<iostream>
using namespace std;
class Matrix{
    private:
        int rows, cols;
        int** arr;
    public:
        Matrix(int r, int c){
            rows=r;
            cols=c;
            arr=new int*[rows];
            for(int i=0; i<rows; i++){
                arr[i]=new int[cols];
            }
            cout<<"Enter "<<rows*cols<<" elements:\n";
            for(int i=0; i<rows; i++){
                for(int j=0; j<cols; j++){
                    *(*(arr+i)+j)=i+j;
                }
            }
            
        }
        void print(){
            for(int i=0; i<rows; i++){
                for(int j=0; j<cols; j++){
                    cout << arr[i][j] << " ";
                }
                cout << endl;
            }
        }

};
int main(){
    Matrix HELLO(4,4);
    HELLO.print();

}