#include <stdio.h>

/**
 * main - entry point
 * prints numeric value of newline char (\n)
 * Return: 0 on success
*/

int main()
{
    char c1 = '\n';
    char c2 = '\t';
    char c3 = '\b';
    char c4 = '\0';


    printf("%d\n", c1);
    printf("%d\n", c2);
    printf("%d\n", c3);
    printf("%d\n", c4);
    return(0);
}