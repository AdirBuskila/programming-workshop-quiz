#include <stdio.h>
int main(void)
{
	char str1[] = "hello", *str2 = "hello";
	printf("str1==str2: %d\n", str1 == str2);
	if (str1 == str2) printf("yes");
	printf("[end]\n");
	return 0;
}
