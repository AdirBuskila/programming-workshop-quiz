#include <stdio.h>
#include <stdlib.h>
int arrSorted(int* a, int n) { int i; for (i = 1; i < n; i++) if (a[i] <= a[i - 1]) return 0; return 1; }
int columnSorted(int** ar, int m, int col) { int i; for (i = 1; i < m; i++) if (ar[i][col] >= ar[i - 1][col]) return 0; return 1; }
void sortedRowsCols(int** ar, int m, int n, int** ar_s_rows, int* num_s_rows, int** ar_s_cols, int* num_s_cols)
{
    int i, j;
    *num_s_rows = *num_s_cols = 0;
    *ar_s_rows = (int*)calloc(m, sizeof(int));
    *ar_s_cols = (int*)calloc(n, sizeof(int));
    for (i = 0; i < m; i++)
        if (arrSorted(ar[i], n)) (*ar_s_rows)[(*num_s_rows)++] = i;
    for (j = 0; j < n; j++)
        if (columnSorted(ar, m, j)) (*ar_s_cols)[(*num_s_cols)++] = j;
    *ar_s_rows = (int*)realloc(*ar_s_rows, *num_s_rows * sizeof(int));
    *ar_s_cols = (int*)realloc(*ar_s_cols, *num_s_cols * sizeof(int));
}
int main(void){ int v[5][4]={{10,13,56,99},{23,57,59,93},{36,19,74,89},{30,75,80,85},{25,73,84,84}}; int**ar=malloc(5*sizeof(int*));
 for(int i=0;i<5;i++){ar[i]=malloc(4*sizeof(int));for(int j=0;j<4;j++)ar[i][j]=v[i][j];}
 int *r,*c,nr,nc; sortedRowsCols(ar,5,4,&r,&nr,&c,&nc);
 printf("rows(%d):",nr);for(int i=0;i<nr;i++)printf(" %d",r[i]); printf("\ncols(%d):",nc);for(int i=0;i<nc;i++)printf(" %d",c[i]); puts("");
 /* empty results */ int w[2][2]={{5,1},{5,2}}; int**b=malloc(2*sizeof(int*)); for(int i=0;i<2;i++){b[i]=malloc(2*sizeof(int));for(int j=0;j<2;j++)b[i][j]=w[i][j];}
 sortedRowsCols(b,2,2,&r,&nr,&c,&nc); printf("empty: nr=%d r=%s nc=%d c=%s\n",nr,r?"non-NULL":"NULL",nc,c?"non-NULL":"NULL"); return 0; }
