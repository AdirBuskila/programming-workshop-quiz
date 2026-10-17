#define main q_main
#include "q1.c"
#undef main
int main(void)
{
	int a0[]={2,6,5,1,8}, a1[]={8,3,5}, a2[]={5}, a3[]={1,2,8,5,3}, a4[]={8,5,2,8}, l[]={8,2,5};
	Item *A[5] = { mk(5,a0), mk(3,a1), mk(1,a2), mk(5,a3), mk(4,a4) };
	Item *L = mk(3,l);
	int cnt = 0;
	for (int i = 0; i < 5; i++) printf("contains(L, A[%d]) = %d\n", i, List1_elements_in_List2(L, A[i]));
	for (Item *p = lists_with_given_elements(A,5,L); p; p = p->next) cnt++;
	printf("result length = %d\n", cnt);
	return 0;
}
