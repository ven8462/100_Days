#include <stdio.h>

/**
 * main - entry point
 * Given x = 1 and y = 3 write a program to print out the results of these expressions:
 *  x += y, x += -y, x -= y, x -= -y, x *= y, and x *= -y
 * Return: 0 on success
*/

int main(void)
{
	int x = 1;
	int y = 3;
	int a = x +=y;
	int b = x += -y;
	int c = x -= y;
	int d = x -= -y;
	int e = x *= y;
	int f = x *= -y;

	printf("x += y is : %d\n", a);
	printf("x += -y is : %d\n", b);
	printf("x -= y is : %d\n", c);
	printf("x -= -y is : %d\n", d);
	printf("x *= y is : %d\n", e);
	printf("x *= -y is : %d\n", f);

	return (0);
}
