// Figure 2.28

#include <iostream>
using namespace std;

int binCoeff ( int n, int k) {
    int y1, y2;
    if((k == 0) || (n == k)) {
        return 1;
    }
    else {
        y1 = binCoeff(n - 1, k); //ra2
        y2 = binCoeff(n - 1, k - 1); //ra3
    }
}

int main() {
    cout << "binCoeff(3, 1) = " << binCoeff(3, 1); //ra1
    cout<< endl;
    return 0;
}

// Output
// binCoeff(3, 1) = 3