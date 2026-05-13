#include <iostream>
using namespace std;
int main(){
    char a;
    cout<<"Enter a char: ";
    cin>>a;
    switch(a){ //doesnt work with strings, can use nested switches.
        case 'a': case 'e': case 'i': case 'o': case 'u':
            cout<<"It is a vowel"<<endl;
            break;
        default:
            cout<<"It is a Consonant"<<endl;
        
    }
}