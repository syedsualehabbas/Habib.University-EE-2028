#include <iostream>
using namespace std;

// ----------------------
// Abstract Base Class
// ----------------------
class Question {
protected:
    int marks;

public:
    Question(int m) : marks(m){}

    // These are virtual -> used for polymorphism
    virtual int getMarks() const = 0;
    virtual string getType() const = 0;

    virtual void display() const = 0;   // POLYMORPHISM DEMO FUNCTION

    virtual ~Question() {}
};

// ----------------------
// Derived: MCQ
// ----------------------
class MCQ : public Question {
public:
    MCQ(int m) : Question(m) {}

    int getMarks() const override { return marks; }
    string getType() const override { return "MCQ"; }

    void display() const override {
        cout << "This is an MCQ (" << marks << " marks)\n";
    }
};

// ----------------------
// Derived: Short Question
// ----------------------
class ShortQuestion : public Question {
public:
    ShortQuestion(int m) : Question(m) {}

    int getMarks() const override { return marks; }
    string getType() const override { return "SHORT"; }

    void display() const override {
        cout << "This is a Short Question (" << marks << " marks)\n";
    }
};

// ----------------------
// Derived: Long Question
// ----------------------
class LongQuestion : public Question {
public:
    LongQuestion(int m) : Question(m) {}

    int getMarks() const override { return marks; }
    string getType() const override { return "LONG"; }

    void display() const override {
        cout << "This is a Long Question (" << marks << " marks)\n";
    }
};

int main() {

    // -----------------------------
    // Array of base-class pointers
    // -----------------------------
    Question* quiz[4];

    quiz[0] = new MCQ(1);
    quiz[1] = new ShortQuestion(5);
    quiz[2] = new LongQuestion(10);
    quiz[3] = new MCQ(1);

    // -----------------------------
    // POLYMORPHISM in action
    // -----------------------------
    cout << "Polymorphism Demo:\n";
    for (int i = 0; i < 4; i++) {
        quiz[i]->display();  // Calls different function for each object!
    }

    // -----------------------------
    // Statistics
    // -----------------------------
    int totalMarks = 0, mcqCount = 0, shortCount = 0, longCount = 0;

    for (int i = 0; i < 4; i++) {
        totalMarks += quiz[i]->getMarks();

        if (quiz[i]->getType() == "MCQ") mcqCount++;
        else if (quiz[i]->getType() == "SHORT") shortCount++;
        else if (quiz[i]->getType() == "LONG") longCount++;
    }

    cout << "\nTotal Marks = " << totalMarks << endl;
    cout << "Total MCQs = " << mcqCount << endl;
    cout << "Total Short Questions = " << shortCount << endl;
    cout << "Total Long Questions = " << longCount << endl;

    return 0;
}
