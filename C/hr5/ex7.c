#include <stdio.h>

/**
 * main - uses getchar() and putchar() to read in a character 
 * entered by the user and write the character to the screen
 * Return: O on success
*/
int main(void)
{
	int ch;
	printf("Enter a character: \n");
	ch = getchar();

	putchar(ch);
	putchar(10);

	return (0);

}