#include <stdio.h>

/**
 * main - entry point
 * Return: 0 0n success
*/
int main(void)
{
	int x = 3;
	int y = 6;
	int z;
	int a;

	z = x * y;
	a = (z == 18);

	printf("%d\n", a);

	return (0);
}
