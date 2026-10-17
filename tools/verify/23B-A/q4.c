#include <stdio.h>
int x = 30, y = 0;
void f1(int x) { printf("x=%d,y=%d\n", x, y); x = y = 10; }
void f2(int y) { printf("x=%d,y=%d\n", x, y); x = y = 15; }
int main() { y = 5; f1(20); f2(y); printf("x=%d,y=%d\n", x, y); return 0; }
