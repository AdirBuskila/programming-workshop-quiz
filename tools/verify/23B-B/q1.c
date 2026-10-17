#include <stdio.h>
#include <stdlib.h>
typedef struct node {
    int value;
    struct node* next;
} node;
node* JosephusPermutation(node* lst, int m)
{
    int i;
    node* head = NULL;
    node* tail = NULL;
    node* tmp;
    while (lst != NULL)
    {
        for (i = 0; i < m - 2; i++)
            lst = lst->next;
        tmp = lst->next;
        lst->next = tmp->next;
        tmp->next = NULL;
        if (head == NULL)
            head = tail = tmp;
        else
        {
            tail->next = tmp;
            tail = tail->next;
        }
        lst = lst->next;
    }
    return head;
}
static node *cyc(int n)
{
    node *h = NULL, *t = NULL;
    for (int i = 1; i <= n; i++) { node *x = calloc(1, sizeof(node)); x->value = i; if (!h) h = x; else t->next = x; t = x; }
    t->next = h; return h;
}
int main(void)
{
    int ms[] = { 3, 2, 5, 10 }, ns[] = { 8, 8, 1, 4 };
    for (int t = 0; t < 4; t++)
    {
        node *r = JosephusPermutation(cyc(ns[t]), ms[t]);
        printf("n=%d m=%d:", ns[t], ms[t]);
        for (; r; r = r->next) printf(" %d", r->value);
        printf("\n");
    }
    node *e = JosephusPermutation(NULL, 3); printf("empty -> %s\n", e ? "non-NULL" : "NULL");
    return 0;
}
