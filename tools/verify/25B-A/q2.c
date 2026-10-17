#include <stdio.h>
#include <stdlib.h>
#define N 4
void triangles(int A[][N], int n, int*** tr_low, int*** tr_up)
{
    int i, j, ** low, ** up;
    low = (int**)calloc(n, sizeof(int*));
    for (i = 0; i < n; i++)
    {
        low[i] = (int*)calloc(i + 1, sizeof(int));
        for (j = 0; j <= i; j++)
            low[i][j] = A[i][j];
    }
    up = (int**)calloc(n, sizeof(int*));
    for (i = 0; i < n; i++)
    {
        up[i] = (int*)calloc(n - i, sizeof(int));
        for (j = 0; j < n - i; j++)
            up[i][j] = A[i][j];
    }
    *tr_low = low;
    *tr_up = up;
}
int main(void){
    int A[N][N]={{5,7,-3,13},{76,16,8,0},{98,4,43,6},{11,19,21,2}}; int **lo,**up,i,j;
    triangles(A,N,&lo,&up);
    puts("low"); for(i=0;i<N;i++){for(j=0;j<=i;j++)printf("%d ",lo[i][j]);puts("");}
    puts("up"); for(i=0;i<N;i++){for(j=0;j<N-i;j++)printf("%d ",up[i][j]);puts("");}
    return 0; }
