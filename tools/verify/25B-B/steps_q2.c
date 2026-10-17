#define main q_main
#include "q2.c"
#undef main
int main(void)
{
	int n = 3;
	int lo0[]={76}, lo1[]={98,4}, lo2[]={11,19,21}, up0[]={7,-3,13}, up1[]={8,42}, up2[]={60};
	int *lo[3]={lo0,lo1,lo2}, *up[3]={up0,up1,up2};
	int **A = triangles_to_matrix(lo, up, n);
	printf("A[2][1]=%d A[1][3]=%d A[3][0]=%d A[0][3]=%d A[2][2]=%d rows=%d\n", A[2][1], A[1][3], A[3][0], A[0][3], A[2][2], n+1);
	printf("up index for A[1][3]: j-i-1=%d (tr_up[1][%d]=%d)\n", 3-1-1, 3-1-1, up[1][3-1-1]);
	return 0;
}
