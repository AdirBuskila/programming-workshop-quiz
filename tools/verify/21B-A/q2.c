#include <stdio.h>
#include <stdlib.h>
typedef struct item {
    int data;
    struct item *next;
} Item;

/* Auxiliary function. Search of common items.
The function gives addresses of items preceding common ones */
void addresses_of_items_preceding_common(Item *L1, Item *L2, Item **p1, Item **p2){
    Item *prev1 = L1, *prev2, *curr1 = prev1->next, *curr2;
    while (1) //external loop: scan first list
    {
        prev2 = L2;
        curr2 = prev2->next;
        do //internal loop: scan second list
        {
            if (curr2->data != curr1->data)
            {
                prev2 = curr2;
                curr2 = curr2->next;
            }
            else //common items are found
            {
                *p1 = prev1;
                *p2 = prev2;
                return;
            }
        } while (curr2 != L2->next);
        prev1 = curr1;
        curr1 = curr1->next;
    } //while (1)
}

/* Special case: list L1 has one item */
Item *one_item_list(Item *L1, Item *L2){
    int common = L1->data;
    free(L1);
    while (L2->data != common) //search of common item in L2
        L2 = L2->next;
    return L2;
}

Item *cyclic_lists_combining(Item *L1, Item *L2){
    Item *p1, *p2, *common;
    if (L1->next == L1) //L1 has one item
        return one_item_list(L1, L2);
    if (L2->next == L2) //L2 has one item
        return one_item_list(L2, L1);
    //p1 and p2 are addresses of items preceding common ones
    addresses_of_items_preceding_common(L1, L2, &p1, &p2);
    /* Combining of L1 and L2*/
    common = p1->next;
    p1->next = p2->next->next;
    free(p2->next);
    p2->next = common;
    return common;
}
static Item *cyc(const int *v, int n)
{
    Item *h = NULL, *t = NULL;
    for (int i = 0; i < n; i++) { Item *x = calloc(1, sizeof(Item)); x->data = v[i]; if (!h) h = x; else t->next = x; t = x; }
    t->next = h; return h;
}
static void show(Item *s, int expect)
{
    Item *c = s; int cnt = 0;
    printf("cycle from returned item:");
    do { printf(" %d", c->data); c = c->next; cnt++; } while (c != s && cnt < 50);
    printf("  (length %d, expected %d, closes=%d)\n", cnt, expect, c == s);
}
int main(void)
{
    int a[] = { 6, 5, 8, 2 }, b[] = { 3, 5, 9, 4, 7 };      /* the exam figure: L1 is the right-hand list (pointer at 6) */
    show(cyclic_lists_combining(cyc(a, 4), cyc(b, 5)), 8);
    int c[] = { 7 }, d[] = { 1, 2, 7, 3 };                    /* L1 has one item */
    show(cyclic_lists_combining(cyc(c, 1), cyc(d, 4)), 4);
    int e[] = { 1, 2, 7, 3 }, f[] = { 7 };                    /* L2 has one item */
    show(cyclic_lists_combining(cyc(e, 4), cyc(f, 1)), 4);
    int g[] = { 1, 2 }, h[] = { 3, 2 };                       /* common item is the last of L1 */
    show(cyclic_lists_combining(cyc(g, 2), cyc(h, 2)), 3);
    return 0;
}
