/*
CSC - Homework 4 - Problem 4
Author: Brandon Hosley
Date: 2018 10 13
*/

#include "pch.h"
#include <iostream>  
using namespace std;

char uppercase(char ch) {
	if ((ch >= 'a') && (ch <= 'z'))
	{
		return ch - 'a' + 'A';
	}
	else
	{
		return ch;
	}
}

char increment(char ch)
{
	if (ch == 'z' || ch == 'Z')
    {
		return 'A';
    }
	else
    {
		return ++ch;
    }
}

int main()
{
	char ch;
	cout << "Please input character:" << endl;
	cin >> ch;
	ch = uppercase(ch);
	ch = increment(ch);
	cout << ch;
	return 0;
}