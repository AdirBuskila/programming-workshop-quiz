#include <stdio.h>
#include <stdlib.h>
void point_swap(void **p, void **q) { void *temp = *p; *p = *q; *q = temp; }
void swap(int *p, int *q) { int temp = *p; *p = *q; *q = temp; }
#ifndef COND
#define COND row1<row2
#endif
#ifndef SZ
#define SZ SIZE + row2
#endif
void row_reverse(void **A, int n, int *SIZE) {
    int row1, row2;
    for (row1=0, row2=n-1; COND; row1++, row2--) {
        point_swap(A + row1, A + row2);
        swap(SIZE + row1, SZ);
    }
}
int main(){
 for(int n=1;n<=8;n++){
  int **A=malloc(n*sizeof(int*)); int *S=malloc(n*sizeof(int));
  for(int i=0;i<n;i++){S[i]=i+1;A[i]=malloc(S[i]*sizeof(int));for(int j=0;j<S[i];j++)A[i][j]=i*10+j;}
  row_reverse((void**)A,n,S);
  int ok=1; for(int i=0;i<n;i++){ if(S[i]!=n-i || A[i][0]!=(n-1-i)*10) ok=0;}
  printf("n=%d ok=%d S=",n,ok);for(int i=0;i<n;i++)printf("%d ",S[i]);puts("");
 }
}
