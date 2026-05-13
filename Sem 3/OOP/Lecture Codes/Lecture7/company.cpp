#include <iostream>
using namespace std;

// ----------------------
// Abstract Base Class
// ----------------------
class Person {
protected:
    string name;
    int salary;

public:
    Person(string n, int s) : name(n), salary(s){}

    // Pure virtual functions
    virtual int getSalary() const = 0;
    virtual string getRole() const = 0;

    // For polymorphism demo
    virtual void display() const = 0;

    virtual ~Person() {}
};

// ----------------------
// Derived Class: Manager
// ----------------------
class Manager : public Person {
public:
    Manager(string n, int s) : Person(n, s) {}

    int getSalary() const override { return salary; }
    string getRole() const override { return "MANAGER"; }

    void display() const override {
        cout << "Manager: " << name << ", Salary: " << salary << endl;
    }
};

// ----------------------
// Derived Class: Employee
// ----------------------
class Employee : public Person {
public:
    Employee(string n, int s) : Person(n, s) {}

    int getSalary() const override { return salary; }
    string getRole() const override { return "EMPLOYEE"; }

    void display() const override {
        cout << "Employee: " << name << ", Salary: " << salary << endl;
    }
};

// ----------------------
// Derived Class: Developer
// ----------------------
class Developer : public Person {
public:
    Developer(string n, int s) : Person(n, s) {}

    int getSalary() const override { return salary; }
    string getRole() const override { return "DEVELOPER"; }

    void display() const override {
        cout << "Developer: " << name << ", Salary: " << salary << endl;
    }
};

int main() {
    // ---------------------------------------------
    // Array of base-class pointers
    // ---------------------------------------------
    Person* company[5];
    company[0] = new Manager("Ali", 90000);
    company[1] = new Employee("Sara", 50000);
    company[2] = new Developer("Bilal", 80000);
    company[3] = new Developer("Hamza", 75000);
    company[4] = new Manager("Zara", 95000);

    // ---------------------------------------------
    // POLYMORPHISM Demo
    // ---------------------------------------------
    cout << "Polymorphism Output:\n";
    for (int i = 0; i < 5; i++) {
        company[i]->display();  // Calls derived version automatically
    }
    // ---------------------------------------------
    // Statistics
    // ---------------------------------------------
    int totalSalary = 0, managerCount = 0, employeeCount = 0, developerCount = 0;

    for (int i = 0; i < 5; i++) {
        totalSalary += company[i]->getSalary();

        if (company[i]->getRole() == "MANAGER") managerCount++;
        else if (company[i]->getRole() == "EMPLOYEE") employeeCount++;
        else if (company[i]->getRole() == "DEVELOPER") developerCount++;
    }

    // ---------------------------------------------
    // Final Output
    // ---------------------------------------------
    cout << "\nTotal Salary = " << totalSalary << endl;
    cout << "Total Managers = " << managerCount << endl;
    cout << "Total Employees = " << employeeCount << endl;
    cout << "Total Developers = " << developerCount << endl;

    return 0;
}
