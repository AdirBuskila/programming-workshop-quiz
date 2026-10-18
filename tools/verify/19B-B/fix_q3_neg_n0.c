#include <stdio.h>
#include <stdlib.h>
int **f (int *A, int n, int **S, int *prows)
{
      int i, j=0, k, **B;
      *prows = 0;
      if (n == 0) { *S = NULL; return NULL; }
      *S = (int *)calloc(n, sizeof(int));
      (*S)[0] = 1;
      for (i=1; i<n; i++)
            if ((A[i]&1) == (A[i-1]&1)) (*S)[j]++;
            else { j++; (*S)[j] = 1; }
      *prows = j+1;
      B = (int **)calloc(*prows, sizeof(int *));
      i=j=0;
      while (i<n){ B[j] = (int *)calloc((*S)[j], sizeof(int)); for (k=0; k<(*S)[j]; k++) B[j][k] = A[i++]; j++; }
      *S = (int *)realloc(*S, *prows*sizeof(int));
      return B;
}
int main(){ int A[]={-3,1,-5,2}; int *S,r; f(A,4,&S,&r); printf("rows=%d S:",r); for(int i=0;i<r;i++)printf(" %d",S[i]); printf("\n");
 f(A,0,&S,&r); printf("n0 rows=%d\n",r); return 0;}
