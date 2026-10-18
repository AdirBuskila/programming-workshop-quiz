#include <stdio.h>
#include <stdlib.h>
typedef struct data_item { int data; struct data_item *next; } DataItem;
typedef struct ptr_item { DataItem *ptr; struct ptr_item *next; } PtrItem;
#ifndef INIT
#define INIT curr_ptr->data = 0;
#endif
#ifndef ACC
#define ACC +=
#endif
DataItem *list_of_lists_to_list (PtrItem *L)
{
    DataItem *data_item_list, *curr_ptr, *lst = (DataItem *)malloc(sizeof(DataItem));
    PtrItem *temp = L;
    curr_ptr = lst;
    while (temp)
    {
        data_item_list = temp->ptr;
        curr_ptr->next = (DataItem *)malloc(sizeof(DataItem));
        curr_ptr = curr_ptr->next;
        INIT
        while (data_item_list) { curr_ptr->data ACC data_item_list->data; data_item_list = data_item_list->next; }
        temp = temp->next;
    }
    curr_ptr->next = NULL;
    curr_ptr = lst; lst = lst->next; free (curr_ptr);
    return lst;
}
DataItem*mkd(int*v,int n){DataItem*h=NULL;for(int i=n-1;i>=0;i--){DataItem*d=malloc(sizeof*d);d->data=v[i];d->next=h;h=d;}return h;}
int main(){int a[]={3,2,4},b[]={6},c[]={1,7};
 DataItem*ls[4]={mkd(a,3),mkd(b,1),NULL,mkd(c,2)}; PtrItem*L=NULL;
 for(int i=3;i>=0;i--){PtrItem*p=malloc(sizeof*p);p->ptr=ls[i];p->next=L;L=p;}
 for(DataItem*r=list_of_lists_to_list(L);r;r=r->next)printf("%d ",r->data);puts("");
 printf("empty:%p\n",(void*)list_of_lists_to_list(NULL));}
