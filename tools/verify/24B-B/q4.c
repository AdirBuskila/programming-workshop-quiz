#include <stdio.h>
int* fun(int *);
int main(void)
{
    int x, y;
    x = *fun(&y); printf("%d %d\n", x, y);
    x = ++(*fun(&y)); printf("%d %d\n", x, y);
    y = ++(*fun(&x)); printf("%d %d\n", x, y);
    x = ++(*fun(&x)); printf("%d %d\n", x, y);
    y = ++(*fun(&y)); printf("%d %d\n", x, y);
    return 0;
}
int* fun(int* q) { static int x = 1; int y = 1; x++; y++; *q = y; return &x; }
