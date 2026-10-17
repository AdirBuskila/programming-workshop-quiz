#include <stdio.h>
#include <stdlib.h>
typedef struct data_item { int data; struct data_item *next; } DataItem;
typedef struct ptr_item { int *ptr; struct ptr_item *next; } PtrItem;
/* official solution, verbatim */
PtrItem *array_of_lists_to_list_of_arrays (DataItem **AL, int n,
                                                  int **SIZE)
{
      PtrItem *LA, *curr_ptr;
      DataItem *data_lst;
      int i, j;

      *SIZE = (int *)calloc(n, sizeof(int));
      LA = (PtrItem *)malloc(sizeof(PtrItem)); //dummy
      curr_ptr = LA;
      for (i=0; i<n; i++)
      {
            curr_ptr->next = (PtrItem *)malloc(sizeof(PtrItem));
            curr_ptr = curr_ptr->next;

            /* Computing size of i-th list in AL (i-th array in LA) */
            (*SIZE)[i] = 0;
            if (AL[i])
            {
                  data_lst = AL[i];
                  while (data_lst)
                  {
                        (*SIZE)[i]++;
                        data_lst = data_lst->next;
                  }
                  curr_ptr->ptr = (int *)calloc((*SIZE)[i], sizeof(int));
            }
            else
                  curr_ptr->ptr = NULL;

            /* Copy i-th array of AL to i-th list in LA */
            data_lst = AL[i];
            j = 0;
            while (data_lst)
            {
                  curr_ptr->ptr[j++] = data_lst->data;
                  data_lst = data_lst->next;
            }
      }
      curr_ptr->next = NULL;

      /* deletion of dummy */
      curr_ptr = LA;
      LA = LA->next;
      free (curr_ptr);
      return LA;
}
static DataItem *mk(int *v, int k){ DataItem *h=NULL,**p=&h; for(int i=0;i<k;i++){*p=malloc(sizeof(DataItem));(*p)->data=v[i];(*p)->next=NULL;p=&(*p)->next;} return h;}
int main(void)
{
    int a0[]={3,2,5,1}, a1[]={6,4}, a2[]={9}, a3[]={0,7,2};
    DataItem *AL[5] = { mk(a0,4), mk(a1,2), mk(a2,1), mk(a3,3), NULL };
    int *SIZE; int n=5, bad=0;
    PtrItem *LA = array_of_lists_to_list_of_arrays(AL, n, &SIZE);
    int exp[5][4]={{3,2,5,1},{6,4},{9},{0,7,2},{0}}; int es[5]={4,2,1,3,0};
    PtrItem *p=LA;
    for(int i=0;i<n;i++,p=p->next){
        printf("SIZE[%d]=%d:",i,SIZE[i]);
        if(SIZE[i]!=es[i]) bad=1;
        if(es[i]==0 && p->ptr!=NULL) bad=1;
        for(int j=0;j<SIZE[i];j++){printf(" %d",p->ptr[j]); if(p->ptr[j]!=exp[i][j]) bad=1;}
        printf("\n");
    }
    if(p!=NULL) bad=1;
    printf(bad?"FAIL\n":"OK\n");
    return bad;
}
