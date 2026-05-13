#include<iostream>
using namespace std;
int main(){
    int x=9,y;
    int* ptr;
    ptr=&x;
    y=*ptr;
    cout<<"x = "<<x<<endl;
    cout<<"ptr = "<<ptr<<endl;
    cout<<"y = "<<y<<endl;
}