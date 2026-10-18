#include <stdio.h>
int main() {
    int a[3][3] = { {1,2,3},{4,5,6},{7,8,9} }, i;
    for (i = 0; i < 3; i++) printf("%d %d ", *a[i], *(*(a + i) + i));
    printf("\n"); return 0; }
