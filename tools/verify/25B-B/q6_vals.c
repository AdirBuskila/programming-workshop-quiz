#include <stdio.h>
int main(void)
{
	char s[]={'/','/'/'/','/'/'/'/'/','/'};
	printf("'/'=%d s[0]=%d s[1]=%d s[2]=%d s[3]=%d\n", '/', s[0], s[1], s[2], s[3]);
	for (int i=0;s[i];i++) printf("iter %d prints %d\n", i, s[i]/'/');
	return 0;
}
