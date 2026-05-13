#include<iostream>
using namespace std;
class MathUtils{
    public:
        static int add(int a , int b){
            return a+b;
        }
        static int subtract(int a, int b){
            return a-b;
        }

};
int main(){
    int result= MathUtils::add(5, 3);
    int result1=MathUtils::subtract(9,3);
    cout<< result<< result1;
}