#include <stdio.h>
void main()
{
  char C[]="C++", c;
  for (c=0; c<3; c++)
       C[c]+=!c?'+'-'+':'-'-'+';
  puts(C);
}
