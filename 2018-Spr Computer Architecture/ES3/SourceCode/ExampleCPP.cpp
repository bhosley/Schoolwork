// Warford Book Example C++ program.

#include <iostream>
using namespace std;

void what (char word[], int j){
    if (j > 1){
        word[j] = word[3 - j];
        what(word, j - 1);
    } // ra2
}

int main() {
    char str[5] = "abcd";
    what(str, 3);
    cout << str << endl;
    // ra1
    return 0;
}