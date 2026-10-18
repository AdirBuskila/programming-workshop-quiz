#include <stdio.h>
int main(){ printf("%d\n", (int)(((long long)1 << (1 << ((1 << (1 << 1)) + 1))) - 1)); printf("%lld\n", (((long long)1 << (1 << ((1 << (1 << 1)) + 1))) - 1)); return 0;}
