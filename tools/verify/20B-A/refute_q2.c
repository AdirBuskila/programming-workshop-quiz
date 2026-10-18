#include <stdio.h>
#include <stdlib.h>
typedef struct item { int data; struct item *next; } Item;
#ifndef WC
#define WC <
#endif
#ifndef FIRST
#define FIRST L->next
#endif
Item *cut_cyclic_list(Item *L)
{
    Item *first;
    if (!L) return NULL;
    while (L->data WC L->next->data) L = L->next;
    first = FIRST;
    L->next = NULL;
    return first;
}
int main(){
 for(int n=0;n<=5;n++) for(int st=0;st<(n?n:1);st++){
  Item *a=malloc(n*sizeof(Item)+1); for(int i=0;i<n;i++){a[i].data=i*3+2;a[i].next=&a[(i+1)%n];}
  Item *r=cut_cyclic_list(n?&a[st]:NULL);
  int cnt=0; for(Item*p=r;p;p=p->next)cnt++;
  printf("n=%d st=%d ret=%s cnt=%d ok=%d\n",n,st, r?"x":"NULL",cnt,(n==0&&!r)||(r==&a[0]&&cnt==n&&a[n-1].next==NULL));
 }
}
