#include <stdio.h>
#include <stdlib.h>
typedef struct data_item { int data; struct data_item *next; } DataItem;
typedef struct ptr_item { DataItem *ptr; struct ptr_item *next; } PtrItem;
/* official solution, verbatim */
DataItem *list_of_lists_to_list (PtrItem *L)
{
    DataItem *data_item_list, *curr_ptr,
        *lst = (DataItem *)malloc(sizeof(DataItem)); //dummy
    PtrItem *temp = L;
    curr_ptr = lst;
    while (temp) // scan list of lists
    {
        data_item_list = temp->ptr;
        curr_ptr->next = (DataItem *)malloc(sizeof(DataItem));
        curr_ptr = curr_ptr->next;
        curr_ptr->data = 0;
        while (data_item_list) // scan internal list
        {
            curr_ptr->data += data_item_list->data;
            data_item_list = data_item_list->next;
        }
        temp = temp->next;
    }
    curr_ptr->next = NULL;
    /* deletion of dummy */
    curr_ptr = lst;
    lst = lst->next;
    free (curr_ptr);
    return lst;
}
static DataItem *mk(const int *v, int n){ DataItem *h=NULL; for(int i=n-1;i>=0;i--){ DataItem *e=malloc(sizeof *e); e->data=v[i]; e->next=h; h=e; } return h; }
int main(void)
{
    int a[]={3,2,4}, b[]={6}, d[]={1,7};
    DataItem *rows[4] = { mk(a,3), mk(b,1), NULL, mk(d,2) };
    PtrItem *L = NULL;
    for (int i = 3; i >= 0; i--) { PtrItem *p = malloc(sizeof *p); p->ptr = rows[i]; p->next = L; L = p; }
    DataItem *R = list_of_lists_to_list(L);
    printf("example R:"); for(DataItem *p=R;p;p=p->next) printf(" %d",p->data); printf("\n");
    printf("empty L -> %p\n", (void*)list_of_lists_to_list(NULL));
    return 0;
}
