#include <stdio.h>
void main()
{
  char *s="123";
  puts( (char *)( ((long long)s*(long long)s+2*(long long)s+1)/(long long)(s+1) ) );
}
