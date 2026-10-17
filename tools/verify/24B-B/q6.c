#include <stdio.h>
int main(void){ printf("%d\n", (int)(((long long)1 << (1 << ((1 << (1 << 1)) + 1))) - 1)); return 0; }
