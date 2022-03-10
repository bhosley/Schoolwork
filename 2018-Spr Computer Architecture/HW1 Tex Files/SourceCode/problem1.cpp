/*CSC - Homework 1 - Problem 1
Author: Brandon Hosley
Date: 2018 08 28
*/

#include <iostream>  
using namespace std;

int main()
{
	int height;
	int width;
	int depth;
	cout << "Input your height(cm):";
	cin >> height;
	cout << "Input your width(cm):";
	cin >> width;
	cout << "Input your depth(cm):";
	cin >> depth;
	int volume = height * width * depth;
	cout << "Hello, Brandon Hosley" << endl;
	cout << "You require " << volume << " cubic centimeters on this Earth!\n";
	system("PAUSE");
    return 0;
}