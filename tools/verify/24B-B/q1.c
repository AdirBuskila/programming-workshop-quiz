#include <stdio.h>
#include <stdlib.h>
typedef struct item { int number; struct item* next; } Item;
int digitsNumber(int num)   /* the official text omits the leading "int" (implicit int) */
{
    int count = 1, abs_num = abs(num);
    while (abs_num > 9) { count++; abs_num /= 10; }
    return count;
}
void headInsert(Item** plst, int key)
{
    Item* temp = (Item*)malloc(sizeof(Item));
    temp->number = key; temp->next = *plst; *plst = temp;
}
Item** numSeparation(int* A, int sz, int* p_size)
{
    int i, max_dig_num = 1, *dig_num = (int *)calloc(sz, sizeof(int));
    Item** L;
    for (i = 0; i < sz; i++)
    {
        dig_num[i] = digitsNumber(A[i]);
        if (dig_num[i] > max_dig_num) max_dig_num = dig_num[i];
    }
    L = (Item**)calloc(max_dig_num, sizeof(Item*));
    for (i = sz - 1; i >= 0; i--)
        headInsert(L + dig_num[i] - 1, A[i]);
    free(dig_num);
    *p_size = max_dig_num;
    return L;
}
int main(void){ int A[]={23,4,-78,34578,79,-185,0,998,9,36}, n, i; Item** L=numSeparation(A,10,&n);
  printf("size=%d\n",n); for(i=0;i<n;i++){ printf("L[%d]:",i); for(Item*p=L[i];p;p=p->next)printf(" %d",p->number); puts(""); } return 0; }
