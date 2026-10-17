#include <stdio.h>
#include <stdlib.h>
/* official solution, verbatim */
#define COLS 6 //example
int **even_sums_odd_numbers (int A[][COLS], int rows, int cols, int **S,
int *prows)
{
    int i, j, k, sum, odd_count, **B;
    *prows = 0;
    B = (int **)calloc(rows, sizeof(int *));
    *S = (int *)calloc(rows, sizeof(int));
    for (i=0; i<rows; i++)
    {
        sum = odd_count = k = 0;
        for (j=0; j<cols; j++)
        {
            sum += A[i][j];
            odd_count += A[i][j]%2;
        }
        if (sum%2 == 0 && odd_count>0)
        {
            B[*prows] = (int *)calloc(odd_count, sizeof(int));
            for (j=0; j<cols; j++)
                if (A[i][j]%2 == 1)
                    B[*prows][k++] = A[i][j];
            (*S)[*prows] = odd_count;
            (*prows)++;
        }
    }
    B = (int **)realloc(B, *prows*sizeof(int *));
    *S = (int *)realloc(*S, *prows*sizeof(int));
    return B;
}
int main(void)
{
    int A[5][COLS] = { {20,14,10,13,33,80}, {40,10,55,11,12,13}, {15,16,17,18,19,21}, {41,43,53,41,17,15}, {10,20,30,40,50,62} };
    int *S, rows;
    int **B = even_sums_odd_numbers(A, 5, COLS, &S, &rows);
    printf("rows=%d\n", rows);
    for (int i=0;i<rows;i++){ printf("S=%d:", S[i]); for(int j=0;j<S[i];j++) printf(" %d",B[i][j]); printf("\n"); }
    return 0;
}
