/*CSC - Homework 1 - Problem 4
Author: Brandon Hosley
Date: 2018 08 28
*/

#include "stdafx.h"
#include <iostream> 
#include <string>
using namespace std;

string username = "Brandon Hosley";

int recursiveP(int i)
{
	if (i == 1)
	{
		return 3;
	}
	else if (i == 2)
	{
		return 4;
	}
	else 
	{
		return recursiveP(i - 1) + recursiveP(i - 2);
	}
}
int main()
{
	// variables
	int input;
	int result;
	// input
	cout << "Input for P(n):";
	cin >> input;
	// output
	result = recursiveP(input);
	cout << username 
		<< " shows P(" << input 
		<< ") has " << result 
		<< " units." << endl;
	system("PAUSE");
	return 0;
}