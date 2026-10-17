#include <stdio.h>
void main()
{
     char s[]={'/','/'/'/','/'/'/'/'/','/'};
     int i;
     printf("n=%d s=%d,%d,%d,%d\n",(int)sizeof s,s[0],s[1],s[2],s[3]);
     for (i=0;s[i];i++) printf("%d",s[i]/'/');
     printf("\n");
}
