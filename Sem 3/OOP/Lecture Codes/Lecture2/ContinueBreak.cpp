#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 5; i++) {
        if (i == 3) {
            continue; // Skips the rest of this iteration
            cout << "This will never print\n"; // Unreachable
        }
        cout << "Value: " << i << endl;
    }
}
