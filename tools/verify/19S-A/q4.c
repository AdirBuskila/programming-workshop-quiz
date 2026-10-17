#include <stdio.h>
/* item 3: the invalid assignment is (3) ptr1 = &y (discards const) */
int main(void)
{
    int x = 7, *ptr1; const int y = 5, *ptr2;
    ptr1 = &x; ptr2 = &y; ptr2 = &x;        /* (1), (2), (4): fine */
    ptr1 = &y;                              /* (3): discards const -> diagnostic */
    printf("%d %d\n", y, *ptr2);
    return 0;
}
