#include <stdio.h>
#include <stdlib.h>
#define COLS 6
#ifndef COND
#define COND sum%2 == 0 && odd_count>0
#endif
#ifndef OC
#define OC odd_count += A[i][j]%2;
#endif
int **even_sums_odd_numbers (int A[][COLS], int rows, int cols, int **S, int *prows)
{
    int i, j, k, sum, odd_count, **B;
    *prows = 0;
    B = (int **)calloc(rows, sizeof(int *));
    *S = (int *)calloc(rows, sizeof(int));
    for (i=0; i<rows; i++)
    {
        sum = odd_count = k = 0;
        for (j=0; j<cols; j++) { sum += A[i][j]; OC }
        if (COND)
        {
            B[*prows] = (int *)calloc(odd_count, sizeof(int));
            for (j=0; j<cols; j++) if (A[i][j]%2 == 1) B[*prows][k++] = A[i][j];
            (*S)[*prows] = odd_count;
            (*prows)++;
        }
    }
    B = (int **)realloc(B, *prows*sizeof(int *));
    *S = (int *)realloc(*S, *prows*sizeof(int));
    return B;
}
void run(int A[][COLS],int rows){int*S,np;int**B=even_sums_odd_numbers(A,rows,COLS,&S,&np);printf("prows=%d:",np);
 for(int i=0;i<np;i++){printf(" [S=%d:",S[i]);for(int j=0;j<S[i];j++)printf(" %d",B[i][j]);printf("]");}puts("");}
int main(){
 int A[5][COLS]={{20,14,10,13,33,80},{40,10,55,11,12,13},{15,16,17,18,19,21},{41,43,53,41,17,15},{10,20,30,40,50,62}};
 run(A,5);
 int N[2][COLS]={{-3,-5,2,4,6,8},{-1,-1,2,2,2,2}}; /* sums 12 and 2 (even), odd negatives */
 run(N,2);
 int Z[1][COLS]={{2,2,2,2,2,2}}; run(Z,1);
}
