#include <stdio.h>
#include <stdlib.h>
typedef struct item{int data;struct item*next;}Item;
#include "q1_author_snip.h"
static Item* mk(int*a,int k){Item*h=NULL;for(int i=k-1;i>=0;i--){Item*t=malloc(sizeof*t);t->data=a[i];t->next=h;h=t;}return h;}
int main(){srand(7);int bad=0;for(int it=0;it<20000;it++){int n=rand()%6;Item*A[6];int arr[6][8],len[6];
 int lk=rand()%5;int l[5];for(int i=0;i<lk;i++){again:l[i]=rand()%7;for(int j=0;j<i;j++)if(l[j]==l[i])goto again;}
 for(int i=0;i<n;i++){len[i]=rand()%8;for(int j=0;j<len[i];j++)arr[i][j]=rand()%7;A[i]=mk(arr[i],len[i]);}
 Item*L=mk(l,lk);Item*r=lists_with_given_elements(A,n,L);
 for(int i=0;i<n;i++){int ok=1;for(int x=0;x<lk;x++){int f=0;for(int j=0;j<len[i];j++)if(arr[i][j]==l[x])f=1;if(!f)ok=0;}
  if(ok){if(!r||r->data!=i){bad++;break;}r=r->next;}}
 if(r)bad++;}
printf("bad=%d\n",bad);return 0;}
