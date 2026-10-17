#include <stdio.h>
#include <stdlib.h>
/* official solution, verbatim */
int **sum_of_2_dim_arrays(int **A, int *SA, int **B, int *SB, int **SC,
int n)
{
      int i, j, **C;
      C = (int **)calloc(n, sizeof(int *));
      *SC = (int *)calloc(n, sizeof(int));
      for (i=0; i<n; i++) {
            (*SC)[i] = (SA[i]<SB[i])? SA[i] : SB[i];
            C[i] = (int *)calloc((*SC)[i], sizeof(int));
            for (j=0; j<(*SC)[i]; j++)
                  C[i][j] = A[i][j]+B[i][j];
      }
      return C;
}
static int *row(int k, const int *v){ int *r=malloc(k*sizeof(int)); for(int i=0;i<k;i++) r[i]=v[i]; return r; }
int main(void)
{
    int a0[]={13,33}, a1[]={15,17,19,21}, a2[]={41,43,53,41,17,15};
    int b0[]={20,19,56}, b1[]={44,11,39}, b2[]={55,50,27,14};
    int *A[3]={row(2,a0),row(4,a1),row(6,a2)}, *B[3]={row(3,b0),row(3,b1),row(4,b2)};
    int SA[3]={2,4,6}, SB[3]={3,3,4}, *SC;
    int **C = sum_of_2_dim_arrays(A,SA,B,SB,&SC,3);
    int want[3][4]={{33,52},{59,28,58},{96,93,80,55}}, ws[3]={2,3,4}, bad=0;
    for(int i=0;i<3;i++){ printf("SC[%d]=%d:",i,SC[i]); if(SC[i]!=ws[i]) bad=1;
        for(int j=0;j<SC[i];j++){ printf(" %d",C[i][j]); if(C[i][j]!=want[i][j]) bad=1; } printf("\n"); }
    printf(bad?"FAIL\n":"OK\n");
    return bad;
}
