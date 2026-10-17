#include <stdio.h>
#include <stdlib.h>
typedef struct item{int data;struct item*next;}Item;
static Item* mk(int*a,int k){Item*h=NULL;for(int i=k-1;i>=0;i--){Item*t=malloc(sizeof*t);t->data=a[i];t->next=h;h=t;}return h;}
/* my own independent solution: hash by presence marks */
static int has(Item*l,int v){for(;l;l=l->next)if(l->data==v)return 1;return 0;}
Item* mine(Item**A,int n,Item*L){Item*h=NULL,**tail=&h;for(int i=0;i<n;i++){int ok=1;for(Item*p=L;p;p=p->next)if(!has(A[i],p->data)){ok=0;break;}
 if(ok){Item*t=malloc(sizeof*t);t->data=i;t->next=NULL;*tail=t;tail=&t->next;}}return h;}
#include "q1_author_snip.h"
int main(){int a0[]={2,6,5,1,8},a1[]={8,3,5},a2[]={5},a3[]={1,2,8,5,3},a4[]={8,5,2,8},l[]={8,2,5};
Item*A[]={mk(a0,5),mk(a1,3),mk(a2,1),mk(a3,5),mk(a4,4)};Item*L=mk(l,3);
Item*r=mine(A,5,L);for(;r;r=r->next)printf("%d ",r->data);printf("\n");
r=lists_with_given_elements(A,5,L);for(;r;r=r->next)printf("%d ",r->data);printf("\n");
/* bug version */
return 0;}
