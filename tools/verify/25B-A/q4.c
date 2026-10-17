#include <stdio.h>
typedef struct { int x; int y; } type1;
typedef union { int x; int y; } type2;
void fun(type2 b) { b.x++; printf("%d %d\n", b.x, b.y); }
int main() {
    type1 a; type2 b;
    a.x = b.x = 3; a.y = b.y = 5;
    printf("%d %d\n", a.x, a.y);
    printf("%d %d\n", b.x, b.y);
    b.x = 8; b.y = 4; a.x = b.x; a.y = b.y;
    printf("%d %d\n", a.x, a.y);
    b.x = 15; b.y = 18; fun(b);
    printf("%d %d\n", b.x, b.y);
    return 0; }
