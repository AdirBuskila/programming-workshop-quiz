#include <stdio.h>
#include <stdlib.h>
void freeMatrix(int** M, int rows) { int i; for (i = 0; i < rows; i++) free(M[i]); free(M); }
int** matrixToFrame(int** M, int rows, int cols)
{
    int rows2 = rows + 2, cols2 = cols + 2, ** F = (int**)calloc(rows2, sizeof(int*)), i, j;
    for (i = 0; i < rows2; i++)
        F[i] = (int*)calloc(cols2, sizeof(int));
    for (i = 0; i < rows; i++)
        for (j = 0; j < cols; j++)
            F[i + 1][j + 1] = M[i][j];
    freeMatrix(M, rows);
    return F;
}
int main(void){ int v[3][4]={{16,4,67,200},{57,2,123,-7},{11,9,34,109}}, i,j; int**M=malloc(3*sizeof(int*));
 for(i=0;i<3;i++){M[i]=malloc(4*sizeof(int));for(j=0;j<4;j++)M[i][j]=v[i][j];}
 int**F=matrixToFrame(M,3,4); for(i=0;i<5;i++){for(j=0;j<6;j++)printf("%4d",F[i][j]);puts("");} return 0; }
