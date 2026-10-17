#include <stdio.h>
#include <stdlib.h>
int main(void){ int* p = (int*)realloc(NULL, sizeof(int)); *p = 7; printf("p non-NULL, value %d\n", *p); free(p); return 0; }
