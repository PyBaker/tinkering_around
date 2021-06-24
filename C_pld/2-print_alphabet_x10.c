#include "holberton.h"
/**
 * print_alphabet_x10 -  print_alphabet_x10 alphabet 10 times
 * Description: to print alphabet 10x
 * Return: Nothing.
 */
void print_alphabet_x10(void)
{
	char c;
	int i;

	for (i = 1; i < 11; i++)
	{
		for (c = 'a'; c <= 'z'; c++)
		{
			_putchar(c);
		}
		_putchar('\n');
	}
}
int main()
{
	print_alphabet_x10();
	return 0;
}
