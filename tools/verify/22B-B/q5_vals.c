#include <stdio.h>
#include <string.h>
int main(void)
{
    int c = strcmp("&","&&");
    printf("strcmp=%d (sign only: %d)  c&c=%d  both strings nonzero (&&)=%d  (c&c)|1=%d\n", c, c < 0 ? -1 : c > 0 ? 1 : 0, c & c, ("a" && "b"), (c & c) | 1);
    return 0;
}
