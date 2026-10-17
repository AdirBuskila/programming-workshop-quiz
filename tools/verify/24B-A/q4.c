#include <stdio.h>
void swap(int* a, int b) { int temp; temp = *a; *a = b; b = temp; }
int blabla(int* p1, int* p2) { int y = 300, x = 1; *p2 = 400; x = x + 300; return (*p1 + 200); }
int main() {
    int x, y = 100;
    x = 200; y = blabla(&x, &y); printf("%d %d\n", x, y);
    x = y; y = 300; swap(&x, y); printf("%d %d\n", x, y);
    y = 200; x = blabla(&y, &x); printf("%d %d\n", x, y);
    x = 500; printf("%d\n", blabla(&x, &x));
    return 0; }
