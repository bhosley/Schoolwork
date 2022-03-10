/*CSC - Homework 1 - Problem 2
Author: Brandon Hosley
Date: 2018 08 28
*/

#include "stdafx.h"
#include <iostream> 
#include <string>
using namespace std;

string username = "Brandon Hosley";

int rectArea(int len, int wid)
{
	return len * wid;
}

int main()
{
	int houseLength;
	int houseWidth;
	int garageLength;
	int garageWidth;
	int houseArea;
	int garageArea;
	double percent;
	cout << "Length of House (ft):";
	cin >> houseLength;
	cout << "Width of House (ft):";
	cin >> houseWidth;
	cout << "Length of Garage (ft):";
	cin >> garageLength;
	cout << "Width of Garage (ft):";
	cin >> garageWidth;

	houseArea = rectArea(houseLength, houseWidth);
	garageArea = rectArea(garageLength, garageWidth);
	percent = ( 1.0 * garageArea / (garageArea + houseArea)) * 100; // 1.0 necessary because double != int

	cout << "The house is " << houseArea << " square feet." << endl;
	cout << "The garage is " << garageArea << " square feet." << endl;
	cout << username << "'s garage is " << percent << " percent of their house." << endl;
	system("PAUSE");
	return 0;
}