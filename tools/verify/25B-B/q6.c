#include <stdio.h>

void main()
{
     char s[]={'/','/'/'/','/'/'/'/'/','/'};
     int i;
     for (i=0;s[i];i++) printf("%d",s[i]/'/');
}
