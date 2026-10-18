#include <stdio.h>
#include <stdlib.h>
typedef struct element { int data; int col; struct element* ptr_next; } element;
#ifndef BODY
#define BODY arr[i][ptr->col] = ptr->data;
#endif
#ifndef LOOP
#define LOOP while
#endif
int** lists_to_sparse_matrix(element** list_row, int rows, int cols)
{
    int** arr, i; element* ptr;
    arr = (int**)calloc(rows, sizeof(int*));
    for (i = 0; i < rows; i++) arr[i] = (int*)calloc(cols, sizeof(int));
    for (i = 0; i < rows; i++) { ptr = list_row[i]; LOOP (ptr) { BODY ptr = ptr->ptr_next; } }
    return arr;
}
element* mk(int d,int c,element*n){element*e=malloc(sizeof*e);e->data=d;e->col=c;e->ptr_next=n;return e;}
int main(){
 element* L[3]={mk(5,2,mk(7,4,NULL)),NULL,mk(3,0,NULL)};
 int**m=lists_to_sparse_matrix(L,3,5); int z=0;
 for(int i=0;i<3;i++){for(int j=0;j<5;j++){printf("%d ",m[i][j]);z+=m[i][j]==0;}puts("");}
 printf("zeros %d\n",z);
}
