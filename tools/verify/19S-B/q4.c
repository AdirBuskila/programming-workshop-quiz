#include <stdio.h>
/* item 3: ~0 ; item 2: pointer sizes; item 1: struct vs union overlap; item 4: int *const *q */
struct S { int a; double b; };
union U { int a; double b; };
int main(void)
{
    printf("~0 = %d\n", ~0);
    printf("sizeof(double*)=%d sizeof(char*)=%d\n", (int)sizeof(double*), (int)sizeof(char*));
    struct S s; union U u;
    printf("struct: &a!=&b %d ; union: &a==&b %d\n", (void*)&s.a != (void*)&s.b, (void*)&u.a == (void*)&u.b);
    int v = 1, *const p = &v; int *const *q = &p;   /* q: pointer to a const pointer to int */
    **q = 5;                                         /* the int itself is changeable */
    printf("v=%d\n", v);
    return 0;
}
