#include <stdio.h>

/**
 * main - entry point
 * Return: 0 on success
*/

int main()
{
	int i;

	for (i = 0;i <= 10; i++)
	{
		printf("*");
		if (i == 4)
		{
			printf("#");
		}
		
	}
	return (0);
}
