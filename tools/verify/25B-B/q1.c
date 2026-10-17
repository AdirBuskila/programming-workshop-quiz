#include <stdio.h>
#include <stdlib.h>
typedef struct item { int data; struct item *next; } Item;

int List1_elements_in_List2(Item* L1, Item* L2)
{
	Item* ptr1 = L1, * ptr2 = L2;
	int found;
	while (ptr1 && ptr2) { ptr1 = ptr1->next; ptr2 = ptr2->next; }
	if (ptr1 && !ptr2) return 0;
	ptr1 = L1;
	while (ptr1)
	{
		found = 0;
		ptr2 = L2;
		while (ptr2)
		{
			if (ptr1->data == ptr2->data) { found = 1; break; }
			ptr2 = ptr2->next;
		}
		if (!found) return 0;
		ptr1 = ptr1->next;
	}
	return 1;
}

void insert_in_head(int x, Item **pl)
{
	Item *temp = (Item *)malloc(sizeof(Item));
	temp->data = x;
	temp->next = *pl;
	*pl = temp;
}

Item *lists_with_given_elements(Item** A, int n, Item* L)
{
	int i;
	Item *ind_list = NULL;
	for (i = n - 1; i >= 0; i--)
		if (List1_elements_in_List2(L, A[i]))
			insert_in_head(i, &ind_list);
	return ind_list;
}

Item *mk(int k, const int *v) { Item *h = NULL; for (int i = k-1; i >= 0; i--) insert_in_head(v[i], &h); return h; }
int main(void)
{
	int a0[]={2,6,5,1,8}, a1[]={8,3,5}, a2[]={5}, a3[]={1,2,8,5,3}, a4[]={8,5,2,8}, l[]={8,2,5};
	Item *A[5] = { mk(5,a0), mk(3,a1), mk(1,a2), mk(5,a3), mk(4,a4) };
	Item *L = mk(3,l);
	Item *r = lists_with_given_elements(A, 5, L);
	for (Item *p = r; p; p = p->next) printf("%d ", p->data);
	printf("\n");
	/* empty result */
	int l2[]={99}; Item *L2 = mk(1,l2);
	printf("%s\n", lists_with_given_elements(A,5,L2) == NULL ? "NULL" : "not null");
	return 0;
}
