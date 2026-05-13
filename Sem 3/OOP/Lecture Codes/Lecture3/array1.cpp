#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;

bool isprime(int x){
    for (int i=2; i<x; i++){
        if (x%i==0) return false;
    }
    return true;
}
int main(){
    int number;
    cout<<"Enter an integer: ";
    cin>>number;
    for (int i=2; i<number; i++){
        if (isprime(i)) cout<<i<<endl;
    }
}