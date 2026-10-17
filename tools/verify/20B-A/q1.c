#include <stdio.h>
#include <stdlib.h>
/* official solution, verbatim */
void point_swap(void **p, void **q) {
    void *temp = *p;
    *p = *q;
    *q = temp;
}
void swap(int *p, int *q) {
    int temp = *p;
    *p = *q;
    *q = temp;
}
void row_reverse(void **A, int n, int *SIZE) {
    int row1, row2;
    for (row1=0, row2=n-1; row1<row2; row1++, row2--) {
        point_swap(A + row1, A + row2);
        swap(SIZE + row1, SIZE + row2);
    }
}
static int *mk(int k, const int *v){ int *r = malloc(k*sizeof(int)); for(int i=0;i<k;i++) r[i]=v[i]; return r; }
static void dump(int **A, int n, int *S){
    for(int i=0;i<n;i++){ printf("%d:",i); for(int j=0;j<S[i];j++) printf(" %d",A[i][j]); printf("\n"); }
    printf("SIZE:"); for(int i=0;i<n;i++) printf(" %d",S[i]); printf("\n");
}
int main(void)
{
    int r0[]={5,12,6,9}, r1[]={0,3,1,29,101}, r2[]={13,14}, r3[]={2,20,4};
    int *A[4] = { mk(4,r0), mk(5,r1), mk(2,r2), mk(3,r3) };
    int S[4] = {4,5,2,3};
    printf("before\n"); dump(A,4,S);
    row_reverse((void**)A, 4, S);
    printf("after (n even)\n"); dump(A,4,S);
    int s5[5]={3,4,2,1,5}; int *B[5]; for(int i=0;i<5;i++){ int v[8]; for(int j=0;j<s5[i];j++) v[j]=10*i+j; B[i]=mk(s5[i],v);} 
    printf("odd n before\n"); dump(B,5,s5);
    row_reverse((void**)B, 5, s5);
    printf("odd n after (middle row 2 unchanged)\n"); dump(B,5,s5);
    return 0;
}
