#include <stdio.h>
#include <stdlib.h>
typedef struct item { int data; struct item *next; } Item;
/* official solution, verbatim */
int is_prefix(Item *L1, Item *L2)
{
    while (L1 && L2)
    {
        if (L1->data != L2->data)
            return 0;
        L1 = L1->next;
        L2 = L2->next;
    }
    if (L1)
        return 0;
    return 1;
}
void insert_in_head(int x, Item **pl)
{
    Item *temp = (Item *)malloc(sizeof(Item));
    temp->data = x;
    temp->next = *pl;
    *pl = temp;
}
Item *arr_of_lists_to_list_of_prefixes(Item **A, int n, Item *L)
{
    int i;
    Item *pref_list = NULL;
    for (i = n - 1; i >= 0; i--)
        if (is_prefix(L, A[i]))
            insert_in_head(i, &pref_list);
    return pref_list;
}
static Item *mk(const int *v, int n){ Item *h=NULL; for(int i=n-1;i>=0;i--){ Item *e=malloc(sizeof *e); e->data=v[i]; e->next=h; h=e; } return h; }
int main(void)
{
    int a0[]={8,2,5,1,6}, a1[]={8,2,5}, a2[]={8}, a3[]={1,8,2,5,3}, a4[]={8,2,5,9}, l[]={8,2,5};
    Item *A[5] = { mk(a0,5), mk(a1,3), mk(a2,1), mk(a3,5), mk(a4,4) };
    Item *R = arr_of_lists_to_list_of_prefixes(A, 5, mk(l,3));
    printf("example:"); for(Item *p=R;p;p=p->next) printf(" %d",p->data); printf("\n");
    R = arr_of_lists_to_list_of_prefixes(A, 5, NULL);
    printf("empty L:"); for(Item *p=R;p;p=p->next) printf(" %d",p->data); printf("\n");
    int none[]={7}; R = arr_of_lists_to_list_of_prefixes(A, 5, mk(none,1));
    printf("no match -> %p\n", (void*)R);
    return 0;
}
