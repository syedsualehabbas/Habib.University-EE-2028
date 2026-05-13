#include<iostream>
using namespace std;
void echange(int* x, int* y){
    int temp=*x;
    *x = *y;        
    *y = temp;
}

int main(){
    int x, y;
    cin>>x>>y;
    echange(&x, &y);
}