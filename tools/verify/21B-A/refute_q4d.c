#include <stdio.h>
int *fun(){ static int x; x++; return &x;}
int main(){ printf("%d %d\n",*fun(),*fun()); return 0;}
