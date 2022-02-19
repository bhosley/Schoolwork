// Fig. 2.25 Transcribed:

#include <iostream>
using namespace std;

int list[4];

int sum (int a[], in n) {
    //returns the sum of the elements of a between a[0] and a[n].
    if (n == 0) {
        return a[0];
    }
    else {
        return a[n] + sum(a, n-1); //ra2
    }
}

int main () {
    cout << "Enter four integers: ";
    cin >> list[0] >> list[1] >> list[2] >> list[3];
    cout << "Their sum is: " << sum(list, 3) << endl; ra1
    return 0; 
}

/*
Interactive Input/Output
Enter four integers: 3 2 6 4
Their sum is: 15
*/