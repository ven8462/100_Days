#include <stdio.h>

/**
 * main - entry point
 * Return: 0 on success 1 otherwise
*/

int add_func();

int  main(void)
{
    int result;

    result = add_func(4, 5);
    printf("%d\n", result);
    return(0);
}

/**
 * add_func() - adds 2 numbers
 * @a: int
 * @b: int
 * Return: a + b
*/

int add_func(int a, int b)
{
    return(a + b);
}