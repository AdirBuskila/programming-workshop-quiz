#include <stdio.h>
#include <stdlib.h>
int** triangles_to_matrix(int** tr_low, int** tr_up, int n)
{
	int i, j, ** A;
	A = (int**)calloc(n + 1, sizeof(int*));
	for (i = 0; i < n + 1; i++)
		A[i] = (int*)calloc(n + 1, sizeof(int));
	for (i = 1; i < n + 1; i++)
		for (j = 0; j < i; j++)
			A[i][j] = tr_low[i - 1][j];
	for (i = 0; i < n; i++)
		for (j = i + 1; j < n + 1; j++)
			A[i][j] = tr_up[i][j - i - 1];
	return A;
}
int main(void)
{
	int n = 3;
	int lo0[]={76}, lo1[]={98,4}, lo2[]={11,19,21}, up0[]={7,-3,13}, up1[]={8,42}, up2[]={60};
	int *lo[3]={lo0,lo1,lo2}, *up[3]={up0,up1,up2};
	int **A = triangles_to_matrix(lo, up, n);
	for (int i = 0; i <= n; i++) { for (int j = 0; j <= n; j++) printf("%d ", A[i][j]); printf("\n"); }
	return 0;
}
