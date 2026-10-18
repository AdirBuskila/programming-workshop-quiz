#include <stdio.h>
int main(){char *s="123";long long a=(long long)s; printf("addr=%lld\n",a); long long r=(a*a+2*a+1)/(long long)(s+1); printf("r=%lld s+1=%lld\n",r,(long long)(s+1)); return 0;}