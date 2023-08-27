#include <stdio.h>

/**
 * main - entry point
 * Return 0 on success
*/

int main(void)
{
	int c;
	int ch = 'A';

	printf("Enter the first character of your name: \n");
	c = getc(stdin);
	printf("%cavender\n", c);

	putc(ch, stdout);
	return(0);
}