#include<iostream>
using namespace std;
class person{
    protected:
        int salary;
        string name;
    public:
        person(const string& n, int s):name(n),salary(s){}
        virtual string getname() const =0;
        virtual int getsalary() const=0;
};
class manager:public person{
    public:
    manager(string n,int s):person(n,s){}


};