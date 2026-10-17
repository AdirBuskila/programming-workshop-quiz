#include <stdio.h>
#include <stdlib.h>
int** triangles_to_matrix(int** tr_low, int** tr_up, int n)
{
    int i, j, ** A;
    A = (int**)calloc(n + 1, sizeof(int*));
    for (i = 0; i < n + 1; i++)
        A[i] = (int*)calloc(n + 1, sizeof(int));
    /* lower triangle */
    for (i = 1; i < n + 1; i++)
        for (j = 0; j < i; j++)
            A[i][j] = tr_low[i - 1][j];
    /* upper triangle */
    for (i = 0; i < n; i++)
        for (j = i + 1; j < n + 1; j++)
A[i][j] = tr_up[i - 1][j];
    return A;
}
int main(){int n=3;int**lo=malloc(3*sizeof(int*)),**up=malloc(3*sizeof(int*));
int l0[]={76},l1[]={98,4},l2[]={11,19,21};int u0[]={7,-3,13},u1[]={8,42},u2[]={60};
lo[0]=l0;lo[1]=l1;lo[2]=l2;up[0]=u0;up[1]=u1;up[2]=u2;
int**A=triangles_to_matrix(lo,up,n);for(int i=0;i<4;i++){for(int j=0;j<4;j++)printf("%d ",A[i][j]);printf("\n");}
printf("A21=%d A13=%d\n",A[2][1],A[1][3]);return 0;}
