#include <stdio.h>
#include <math.h>
int main(){int z='z'-1; putchar(z-(int)pow((int)pow(z,1)-z,z<<1)); putchar('\n');
putchar(z-(int)pow((z^1)-z,z<<1)); putchar('\n');
/* sign slip: (z^1)-z taken as +1 */ putchar(z-(int)pow(1,z<<1));putchar('\n');return 0;}
