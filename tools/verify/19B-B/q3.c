#include <stdio.h>
#include <stdlib.h>
/* official solution, verbatim */
int **array_to_array_of_sequences (int *A, int n, int **S, int *prows)
{
      int i, j=0, k, **B;
      *prows = 0;
      *S = (int *)calloc(n, sizeof(int));
      (*S)[0] = 1;
      for (i=1; i<n; i++)
            if (A[i]%2 == A[i-1]%2) //the same sequence
                  (*S)[j]++;
            else //new sequence
            {
                  j++;
                  (*S)[j] = 1;
            }
            *prows = j+1;

      B = (int **)calloc(*prows, sizeof(int *));

      i=j=0;
      while (i<n)
      {
            B[j] = (int *)calloc((*S)[j], sizeof(int));
            for (k=0; k<(*S)[j]; k++)
                  B[j][k] = A[i++];
            j++;
      }
      *S = (int *)realloc(*S, *prows*sizeof(int));
      return B;
}
int main(void)
{
    int A[] = {3,7,20,12,6,9,13,1,2,7,55,31,9}, n = 13, *S, rows;
    int **B = array_to_array_of_sequences(A, n, &S, &rows);
    int ws[5]={2,3,3,1,4}; int bad = (rows!=5);
    int k=0;
    for (int i=0;i<rows;i++){ printf("S[%d]=%d:",i,S[i]); if(S[i]!=ws[i]) bad=1;
        for(int j=0;j<S[i];j++){ printf(" %d",B[i][j]); if(B[i][j]!=A[k++]) bad=1; } printf("\n"); }
    printf("rows=%d %s\n", rows, bad?"FAIL":"OK");
    /* edge: n=1 (the official loop never sets *prows) */
    int one[] = {4}, *S1, r1; int **B1 = array_to_array_of_sequences(one, 1, &S1, &r1);
    printf("n=1: rows=%d (a correct answer is 1)\n", r1); (void)B1;
    return bad;
}
