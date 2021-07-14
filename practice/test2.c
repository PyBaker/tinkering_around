#include<stdio.h>
#include<stdlib.h>

/**
 * main - main function
 * Description: this program does stuff
 * Return 0:Success
 */

int main()
{
	int val = 20;
	int *ptr_v;
	printf("%x \n",ptr_v);
	ptr_v = &val;
	printf("the changed = %x \n",ptr_v);
	printf("the valur ad ptr = %x \n",&ptr_v);
}
