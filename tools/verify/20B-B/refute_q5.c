#include <stdio.h>
#include <string.h>
#include <math.h>
int main(){int n = strlen("\\\\"), m = strlen("\n\n\0\n"), k = strlen("////");
 char *s="Ah!",*x=s+m; printf("%d %d %d\n",n,m,k);
 puts((char*)((long long)(pow((int)x,n)-k)/(int)(x+m)));}
