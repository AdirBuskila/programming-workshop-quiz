#include <stdio.h>
int size (double arr[])
{
     return sizeof(arr);
}
int x;
struct padded { char c; int i; char d; };
int main(void)
{
    double arr[10];
    printf("size(arr)=%d (sizeof a pointer)\n", size(arr));
    x++;
    printf("global x=%d (static storage starts at 0)\n", x);
    printf("sizeof(struct padded)=%d, sum of fields=%d\n", (int)sizeof(struct padded), (int)(sizeof(char)+sizeof(int)+sizeof(char)));
    return 0;
}
