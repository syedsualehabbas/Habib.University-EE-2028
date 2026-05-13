#include<iostream>
using namespace std;
int main(){
    //the name of array is itself the address of first element.
    int arr[]={1,2,3,4,5}; //static array (stacks)
    cout<<*arr<<endl;
    for(int ix=0; ix<5; ix++){
        cout << "arr["<<ix<<"] = "<<*(arr+ix)<<endl;
    }
}