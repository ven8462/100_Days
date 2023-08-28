#include <stdio.h>

/**
 * main - post and pre increament and decrement operator
 * Return: 0 on success otherwise 1 on failure
*/

int main(void)
{
	int i = 0;
	int x = i++;
	int y = i;
	printf("%d\n", x);
	printf("%d\n", y);
	return (0);
}
