#include <stdio.h>
#include <stdlib.h>
typedef struct { int size; int * ptr; } dyn_array;
dyn_array* divNumbers(int* A, int sz, int n)
{
    int i, j, k;
    dyn_array* B = (dyn_array*)calloc(n - 1, sizeof(dyn_array));
    for (i = 2; i <= n; i++)
    {
        k = 0;
        B[i - 2].ptr = (int*)calloc(sz, sizeof(int));
        for (j = 0; j < sz; j++)
            if (A[j] % i == 0)
                B[i - 2].ptr[k++] = A[j];
        B[i - 2].ptr = (int*)realloc(B[i - 2].ptr, k * sizeof(int));
        B[i - 2].size = k;
    }
    return B;
}
int main(void){ int A[]={15,49,-8,6,-25,9,10,-58,1,77}; dyn_array*B=divNumbers(A,10,5);
  for(int i=0;i<4;i++){ printf("B[%d] size=%d ptr=%s:",i,B[i].size,B[i].ptr?"set":"NULL"); for(int j=0;j<B[i].size;j++)printf(" %d",B[i].ptr[j]); puts(""); }
  int C[]={1,7}; B=divNumbers(C,2,3); for(int i=0;i<2;i++) printf("empty case B[%d] size=%d ptr=%s\n",i,B[i].size,B[i].ptr?"non-NULL":"NULL");
  return 0; }
