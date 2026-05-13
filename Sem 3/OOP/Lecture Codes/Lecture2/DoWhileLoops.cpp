#include <iostream>
using namespace std;
int main(){
    int age;
    do {
        cout<<"Enter Your Age: ";
        cin>>age;
        if (age<0) cout<<"Invalid Age! pLEASE tRY again: ";

    }while (age<0);
    cout<<"Your age is "<<age<<endl;

}