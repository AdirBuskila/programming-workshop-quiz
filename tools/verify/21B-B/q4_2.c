#include <stdio.h>
void main() {
    int i = 64;
    int cnt = 0;
    for (; i; i >>= 1)
        { printf("Hi \n"); cnt++; }
    printf("count=%d\n", cnt);
}
