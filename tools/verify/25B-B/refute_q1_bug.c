#include <stdio.h>
#include <stdlib.h>
typedef struct item{int data;struct item*next;}Item;
int List1_elements_in_List2(Item*L1,Item*L2){for(Item*a=L1;a;a=a->next){int f=0;for(Item*b=L2;b;b=b->next)if(b->data==a->data){f=1;break;}if(!f)return 0;}return 1;}
void insert_in_head(int x,Item**pl){Item*t=malloc(sizeof(Item));t->data=x;t->next=*pl;*pl=t;}
Item *lists_with_given_elements(Item** A, int n, Item* L)
{
    int i;
    Item *ind_list = NULL;
    for (i = n - 1; i > 0; i--)
        if (List1_elements_in_List2(L, A[i]))
            insert_in_head(i, &ind_list);
    return ind_list;
}
static Item* mk(int*a,int k){Item*h=NULL;for(int i=k-1;i>=0;i--){Item*t=malloc(sizeof*t);t->data=a[i];t->next=h;h=t;}return h;}
int main(){int a0[]={2,6,5,1,8},a1[]={8,3,5},a2[]={5},a3[]={1,2,8,5,3},a4[]={8,5,2,8},l[]={8,2,5};
Item*A[]={mk(a0,5),mk(a1,3),mk(a2,1),mk(a3,5),mk(a4,4)};Item*L=mk(l,3);
printf("helper(L,A2)=%d\n",List1_elements_in_List2(L,A[2]));
Item*r=lists_with_given_elements(A,5,L);for(;r;r=r->next)printf("%d ",r->data);printf("\n");return 0;}
