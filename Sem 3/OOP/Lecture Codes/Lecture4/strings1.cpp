#include<iostream>
using namespace std;
int main(){
    const int MAX=80;
    char str[MAX];  // Always save max-1 char init self, saves the last space for /0
    cout<<"Enter your string (8 char max): ";
    cin.getline(str, MAX, '$'); // Terminate with $
    cout<<"your string is: "<<str<<endl;
    char str1[]="hello lil bro how are you? "
    "my name is sualeh";
    cout<<str1<<endl;
    cout<<9/4;

}