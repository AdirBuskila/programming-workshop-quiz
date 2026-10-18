#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int **f(char *fn, int **S, int *rows){
  char line[1000]; int **A=NULL,n=0,i; FILE*fp=fopen(fn,"r"); if(!fp)exit(1);
  *S=NULL;
  while(fgets(line,sizeof line,fp)){
    int num,size,off=0,len=0,k=0,used,j;
    char*p=line;
    while(sscanf(p+off,"%d%d%n",&num,&size,&used)==2){len+=size;off+=used;}
    A=realloc(A,(n+1)*sizeof(int*)); *S=realloc(*S,(n+1)*sizeof(int));
    A[n]=calloc(len,sizeof(int)); (*S)[n]=len; off=0;
    while(sscanf(p+off,"%d%d%n",&num,&size,&used)==2){for(j=0;j<size;j++)A[n][k++]=num;off+=used;}
    n++;
  }
  fclose(fp); *rows=n; return A;}
int main(int c,char**v){int*S,r;int**A=f(v[1],&S,&r);for(int i=0;i<r;i++){printf("%d:",S[i]);for(int j=0;j<S[i];j++)printf(" %d",A[i][j]);puts("");}}
