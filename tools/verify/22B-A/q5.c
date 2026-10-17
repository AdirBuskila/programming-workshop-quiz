#include <stdio.h>
#include <math.h>
void main()
{
    int z='z'-1;
    printf("z=%d (z^1)-z=%d z<<1=%d pow=%d\n", z, (z^1)-z, z<<1, (int)pow((z^1)-z,z<<1));
    putchar(z-(int)pow((z^1)-z,z<<1));
    putchar('\n');
}
