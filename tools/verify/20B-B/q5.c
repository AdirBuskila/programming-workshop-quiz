#include <stdio.h>
#include <string.h>
#include <math.h>
void main()
{
      int n = strlen("\\\\"), m = strlen("\n\n\0\n"), k =
strlen("////");
      char *s = "Ah!", *x = s + m;
      printf("n=%d m=%d k=%d sizeof(char*)=%d\n", n, m, k, (int)sizeof(char*));
      puts( (char *)( (long long)(pow((int)x, n) - k) / (int)(x + m) )
);
}
