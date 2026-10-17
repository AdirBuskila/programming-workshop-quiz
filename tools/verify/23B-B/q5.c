#include <stdio.h>
#include <stdlib.h>
int f(int n) {
    int m = 2 * n;
    return m;
}
int main(void)
{
    int k = 3;
    printf("(1) %d\n", 0);
    printf("(2) %.0lf\n", 0.0);
    printf("(3) %d\n", NULL);
    printf("(4) %d\n", '0');
    printf("(5) %d\n", '\0');
    printf("(6) %d\n", EOF + 1);
    printf("b: %d\n", f(k));
    printf("b: %d\n", (*f)(k));
    return 0;
}
