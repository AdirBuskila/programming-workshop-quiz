#include <stdio.h>
#include <stdlib.h>
/* official solution, verbatim */
typedef struct element
{
    int data;
    int col;
    struct element* ptr_next;
} element;
int** lists_to_sparse_matrix(element** list_row, int rows, int cols)
{
    int** arr, i;
    element* ptr;
    arr = (int**)calloc(rows, sizeof(int*));
    for (i = 0; i < rows; i++)
        arr[i] = (int*)calloc(cols, sizeof(int));
    for (i = 0; i < rows; i++)
    {
        ptr = list_row[i];
        while (ptr)
        {
            arr[i][ptr->col] = ptr->data;
            ptr = ptr->ptr_next;
        }
    }
    return arr;
}
static element *mk(int d, int c, element *n){ element *e=malloc(sizeof *e); e->data=d; e->col=c; e->ptr_next=n; return e; }
int main(void)
{
    element *L[4];
    L[0] = mk(4,2,mk(7,4,NULL));
    L[1] = mk(3,0,NULL);
    L[2] = mk(9,0,mk(1,1,mk(6,3,NULL)));
    L[3] = NULL;
    int **A = lists_to_sparse_matrix(L, 4, 5);
    for (int i = 0; i < 4; i++) { for (int j = 0; j < 5; j++) printf("%d ", A[i][j]); printf("\n"); }
    return 0;
}
