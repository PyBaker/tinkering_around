#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * main - main function
 * Description: to test write function
 *
 * Return: 1
 */
int main(void)
{
	FILE *fd = fopen("~/gat/tinkering_around/practice/hello_world.c", "w");
	write(fd,1,0);
	return (0);
}

