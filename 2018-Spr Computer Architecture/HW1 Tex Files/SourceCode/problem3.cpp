/*CSC - Homework 1 - Problem 3
Author: Brandon Hosley
Date: 2018 08 28
*/

#include "stdafx.h"
#include <iostream> 
#include <string>
using namespace std;

string username = "Brandon Hosley";

void calculate(int& ar, int& vol, int len, int wid, int hgt)
{
	ar = len * wid;
	vol = len * wid * hgt;
}
int main()
{
	// variables
	int area;
	int volume;
	int length;
	int width;
	int height;
	// input
	cout << "Length of House (ft):";
	cin >> length;
	cout << "Width of House (ft):";
	cin >> width;
	cout << "Height of House (ft):";
	cin >> height;
	//output
	calculate(area, volume, length, width, height);
	cout << username 
		<< " has a house with " << area
		<< " square feet that contains " << volume 
		<< " cubic feet." << endl;
	system("PAUSE");
	return 0;
}