#include <iostream>
using namespace std;

void printingarray(int a[]){
    for (int i=0; i<4; i++){
        cout<<a[i]<<" ";
    }

}
int main(){
    //array contains elements of same data typr. we declare array by specifying the data type, followed by name of array followed by its size.
    int a[4],y;
    for(int i=0; i<4;i++){
        cout<<"Enter element "<<i+1<<": ";
        cin>>y;
        a[i]=y;
    }
    printingarray(a);
}