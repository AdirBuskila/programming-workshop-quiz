#include <stdio.h>
int x;
void f() {
    static int x;
    printf("%d", x);
    printf("%d", ++x);
}
void main() {
    f();
    printf("%d", x);
    printf("%d", ++x);
    f();
}
