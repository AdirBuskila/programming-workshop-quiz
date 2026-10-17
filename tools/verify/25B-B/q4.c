#include <stdio.h>

int y = 2;

void f1() {
    printf("1 ");
}

void f2() {
    printf("2 ");
}

void f3() {
    printf("3 ");
}

void f4() {
    int x = 0;
    static int y;
    void (*p[3])() = {f1, f2, f3};

    p[x]();
    p[y]();
    x++;
    y++;
}

void f5() {
    printf("%d ", y);
    y++;
}

void main() {
    int y;

    for (y = 5; y <= 7; y++) {
        f4();
        printf("\n");
    }
    f5();
    printf("%d\n", y);
    f5();
    printf("%d\n", y);
}
