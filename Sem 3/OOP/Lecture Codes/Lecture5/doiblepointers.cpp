#include<iostream>
using namespace std;
int main(){
    const char* arr[]={"Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday"};

    const char** ptr = arr;
    cout<<"First string: "<<*ptr<<endl;
    cout<<"Second string: "<<*(ptr+1)<<endl;
    cout<<"First character of second string: "<<**(ptr+1)<<endl;
    cout<<"Second character of the first string: "<<*(*ptr +1)<<endl;

}