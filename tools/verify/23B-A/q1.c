#include <stdio.h>
#include <stdlib.h>
typedef struct monom { double coefficient; int power; } Monom;
typedef struct item { Monom mon; struct item * next; } Item;
Item* createPolynom(Item* L)
{
    Item* curr = L, * P = NULL;
    int max_power = 0, power;
    double *arr;
    while (curr)
    {
        if (curr->mon.power > max_power) max_power = curr->mon.power;
        curr = curr->next;
    }
    arr = (double*)calloc(max_power + 1, sizeof(double));
    curr = L;
    while (curr)
    {
        arr[curr->mon.power] += curr->mon.coefficient;
        curr = curr->next;
    }
    curr = L;
    for (power = 0; power <= max_power; power++)
        if (arr[power] != 0)
        {
            curr = (Item*)malloc(sizeof(Item));
            curr->next = P;
            P = curr;
            P->mon.coefficient = arr[power];
            P->mon.power = power;
        }
    free(arr);
    return P;
}
static Item* add(Item* h,double c,int p){ Item*n=malloc(sizeof(Item)); n->mon.coefficient=c;n->mon.power=p;n->next=NULL; if(!h)return n; Item*t=h; while(t->next)t=t->next; t->next=n; return h; }
int main(void){ Item*L=NULL; double c[]={2,-5,3,6,-8,-3,7.5}; int p[]={4,1,6,4,0,6,3}; for(int i=0;i<7;i++)L=add(L,c[i],p[i]);
 for(Item*q=createPolynom(L);q;q=q->next)printf("%g , %d\n",q->mon.coefficient,q->mon.power);
 printf("empty: %s\n", createPolynom(NULL)?"non-NULL":"NULL"); return 0; }
