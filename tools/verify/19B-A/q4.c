#include <stdio.h>
static int c;
int f1(int *a) { return *a; }
int main(void)
{
    int (*p)(int *) = f1;            /* Q1: pointer to function taking int*, returning int */
    int x = 12, y = 10;
    int z = x ^ y;                   /* Q2: XOR */
    const int v = 5;
    const int *q = &v;               /* Q4: q can change, *q cannot */
    int w = 7;
    q = &w;
    printf("p(&x)=%d  12^10=%d  static c=%d  *q=%d\n", p(&x), z, c, *q);
    return 0;
}
