#include <stdio.h>

/**
 * main - entry point
 * Return: 0 on success 1 otherwise
*/
int mul_nums(int a, int b);

int main()
{ 
    int result;

    result = mul_nums(3, 5);
    printf("%d\n", result);
    return (0);
}

/**
 * mul_nums - multiply 2 integers
 * @a: int a
 * @b: int b
 * Return: a * b
*/

int mul_nums(int a, int b)
{
    return (a * b);
}