#include <stdio.h>
void main()
{
     char *s="ab";
     printf("%d\n",sizeof s[0]+sizeof s[1]-sizeof'a'-sizeof'b');
}
