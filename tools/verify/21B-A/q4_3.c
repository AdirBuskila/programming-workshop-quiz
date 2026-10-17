#include <stdio.h>
typedef struct { int a[3]; } S;
void by_value_array(int a[3]) { a[0] = 99; }
void by_value_struct(S s) { s.a[0] = 99; }
int main(void)
{
    int arr[3] = { 1, 2, 3 };
    by_value_array(arr);
    printf("array passed to function: arr[0]=%d (the callee wrote through the pointer)\n", arr[0]);
    S s = { {1, 2, 3} };
    by_value_struct(s);
    printf("struct containing an array passed by value: s.a[0]=%d (the callee got a copy)\n", s.a[0]);
    return 0;
}
