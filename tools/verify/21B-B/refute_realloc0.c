#include <stdio.h>
#include <stdlib.h>
int main(){int*p=malloc(40);int*q=realloc(p,0);printf("%p %p\n",(void*)p,(void*)q);
char*a="abcd",*b="xyz";printf("%lld\n",(long long)(a-b));}
