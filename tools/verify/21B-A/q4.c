#include <stdio.h>
#include <string.h>
enum color { RED, GREEN, BLUE };
int *fun() {
    static int x;
    x++;
    return &x;
}
int main(void)
{
    /* Q4.1 which variable is default-initialized: a local int, a local pointer, an enum constant, a loop var... */
    int local_int; int *local_ptr;
    (void)local_int; (void)local_ptr;
    printf("4.1 enum constants: %d %d %d\n", RED, GREEN, BLUE);
    /* Q4.2 right shift of a negative int vs positive int */
    int neg = -8, pos = 8;
    printf("4.2 -8>>1=%d (0x%08x)  8>>1=%d\n", neg >> 1, (unsigned)(neg >> 1), pos >> 1);
    printf("4.2 -1>>1=%d  unsigned 0x80000000>>1=0x%08x\n", -1 >> 1, 0x80000000u >> 1);
    /* Q4.4 static local: the pointer remains valid, value kept, initial 0 */
    int *p = fun(); int *q = fun();
    printf("4.4 first=%d second=%d same address=%d\n", *p, *q, p == q);
    /* Q5 */
    printf("5: %d\n", (int)sizeof"|0\0/00\0/0|");
    return 0;
}
