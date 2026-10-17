#include <stdio.h>

void main()
{
     char s[]={'^','^','^'^'^','^'};
     int i;
     printf("%s",s);
     printf("\n");
     for (i = 0; i < 4; i++) printf("s[%d]=%d ", i, s[i]);
     printf("\n");
}
