#include <stdlib.h>
#include <stdio.h>
int main(void){ int a[5], ** p = (int **)malloc(sizeof(int*)); *p = a; puts("before free"); fflush(stdout); free(*p); puts("after free"); return 0; }
