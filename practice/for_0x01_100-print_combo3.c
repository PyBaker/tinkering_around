#include <stdio.h>
#include <stdlib.h>

/**
 * main - main function
 * Description: to test write function
 *
 * Return: 1
 */
int main(void)
{
	int i, j;

	for (i = 0 ; i < 10 ; i++)
	{
		for (j = 0 ; j < 10 ; j++)
		{
			if (i == j)
				continue;
			putchar('0' + i);
			putchar('0' + j);
			putchar(' ');
		}
	}
	return (0);
}

