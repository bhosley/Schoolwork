// 2-sum.c
// Addition program
#include <stdio.h>

int main ( void )
{
    int integer1;
    int integer2;
    int sum;

    printf("Enter first integer:\n"); // prompt
    scanf("%d", &integer1); // read int

    printf("Enter second integer:\n");
    scanf("%d", &integer2);

    sum = integer1 + integer2;

    printf("Sum is %d\n", sum);
} // end main