/* The bonus relies on pointers fitting in int (32-bit). On a 64-bit build the (int) casts truncate the address,
   so this harness replays the same arithmetic with a made-up 32-bit address to check the algebra. */
#include <stdio.h>
#include <math.h>
int main(void)
{
    int n = 2, m = 2, k = 4;
    long long addrs[] = { 0x00403000LL, 0x1000LL, 123456LL };
    for (int i = 0; i < 3; i++) {
        int s = (int)addrs[i];
        int x = s + m;
        long long r = (long long)(pow(x, n) - k) / (x + m);
        printf("s=%d -> result=%lld (equals s: %d)\n", s, r, r == s);
    }
    return 0;
}
