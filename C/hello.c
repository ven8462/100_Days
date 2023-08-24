#include <stdio.h>
#include <stdlib.h>

/**
 * main - entry point
 * Return: 0 on success
*/

int main()
{
    int i = 0;
    
    for (i = 0; i < 4; i++)
        if (i == 3)
        printf("exiting the prog\n");
            /*exit(100);*/
    printf("Hello World!\n");
    return (0);
}