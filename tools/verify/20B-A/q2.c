#include <stdio.h>
#include <stdlib.h>
typedef struct item { int data; struct item *next; } Item;
/* official solution, verbatim */
Item *cut_cyclic_list(Item *L)
{
    Item *first;
    if (!L)
        return NULL;
    while (L->data < L->next->data)
        L = L->next;
    first = L->next;
    L->next = NULL;
    return first;
}
static Item *mk(int d){ Item *e=malloc(sizeof *e); e->data=d; e->next=NULL; return e; }
static void run(int *v, int n, int entry){
    Item **a = malloc(n*sizeof *a);
    for(int i=0;i<n;i++) a[i]=mk(v[i]);
    for(int i=0;i<n;i++) a[i]->next = a[(i+1)%n];
    Item *r = cut_cyclic_list(a[entry]);
    printf("entry %d ->", v[entry]);
    for(Item *p=r;p;p=p->next) printf(" %d", p->data);
    printf("\n");
}
int main(void)
{
    int v[4]={1,2,4,7};            /* ascending order around the cycle */
    for(int e=0;e<4;e++) run(v,4,e);
    int one[1]={9}; run(one,1,0);
    printf("NULL -> %p\n", (void*)cut_cyclic_list(NULL));
    return 0;
}
