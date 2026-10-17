#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef struct item {
    int data;
    struct item* next;
}Item;

/* Auxiliary function: estimation of the size of a number */
int countDigit(int number)
{
    int j = 0;
    while (number)
    {
        ++j;
        number /= 10;
    }
    return j;
}

void List_num_add_1(Item* head, int N)
{
    int i, p, k, new_size, number = 0;
    Item* node = head;

    /* Creating a number from the list */
    while (node)
    {
        number = number * 10 + node->data;
        node = node->next;
    }

    number += N; //new number
    new_size = countDigit(number); //the size of a new number

    /* List transformation for a new number */
    p = (int)pow(10, new_size);
    node = head;
    for (i = 0; i < new_size; ++i)
    {
        p /= 10;
        k = number / p;
        node->data = k;
        number = number - k * p;
        if (!node->next && i < new_size - 1)  //additional element
            node->next = (Item*)calloc(1, sizeof(Item));
        node = node->next;
    } //for
}

void List_num_add(Item* head, int N)
{
    int i, p, k, size = 0, new_size, number = 0, diff;
    Item* node = head;

    /* Creating a number from the list */
    while (node)
    {
        number = number * 10 + node->data;
        node = node->next;
        size++;
    }

    number += N; //new number
    new_size = countDigit(number); //the size of a new number
    diff = new_size - size;

    /* Addition of new elements for a new number */
    if (diff > 0)
    {
        node = head;
        while (node->next) //search of a last element
            node = node->next;
        for (i = 1; i <= diff; i++) //diff new elements
        {
            node->next = (Item*)malloc(sizeof(Item));
            node = node->next;
        }
        node->next = NULL;
    }

    /* List filling for a new number */
    p = (int)pow(10, new_size);
    node = head;
    while (node)
    {
        p /= 10;
        k = number / p % 10;
        node->data = k;
        node = node->next;
    }
}
static Item *mk(const char *digits)
{
    Item *h = NULL, **t = &h;
    for (; *digits; digits++) { *t = calloc(1, sizeof(Item)); (*t)->data = *digits - '0'; t = &(*t)->next; }
    return h;
}
static void show(Item *h) { for (; h; h = h->next) printf("%d", h->data); printf("\n"); }
int main(void)
{
    const char *in[] = { "9994", "12", "99", "5", "1000", "999999" };
    int add[] = { 18, 3, 1, 5, 7, 1 };
    for (int t = 0; t < 6; t++)
    {
        Item *a = mk(in[t]), *b = mk(in[t]);
        List_num_add_1(a, add[t]);
        List_num_add(b, add[t]);
        printf("%s + %d: v1=", in[t], add[t]); show(a);
        printf("%s + %d: v2=", in[t], add[t]); show(b);
    }
    return 0;
}
