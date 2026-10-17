#include <stdio.h>
#include <stdlib.h>
typedef struct
{
    int i, j;
} pair;

pair* indirect_friends(int** M, int size, int* new_size)
{
    int i, j, k, count = 0;
    pair* arr;
    *new_size = (size * size - size) / 2; //upper bound of possible number of pairs
    arr = (pair*)calloc(*new_size, sizeof(pair));
    for (i = 0; i < size; i++)
        for (j = 0; j < i; j++)
            if (M[i][j] == 0)
                for (k = 0; k < size; k++)
                    if (M[i][k] == 1 && M[k][j] == 1)
                    {
                        arr[count].i = i;
                        arr[count++].j = j;
                        break; //search for common friends of i and j has been terminated
                    }
    *new_size = count;
    arr = (pair*)realloc(arr, *new_size * sizeof(pair));
    return arr;
}
int main(void)
{
    int D[8][8] = {
        {0,1,0,0,0,1,0,0},
        {1,0,1,0,0,0,1,0},
        {0,1,0,0,1,0,0,1},
        {0,0,0,0,0,1,0,1},
        {0,0,1,0,0,1,0,0},
        {1,0,0,1,1,0,1,0},
        {0,1,0,0,0,1,0,1},
        {0,0,1,1,0,0,1,0} };
    int *M[8]; for (int r = 0; r < 8; r++) M[r] = D[r];
    int n; pair *a = indirect_friends(M, 8, &n);
    printf("pairs=%d:", n);
    for (int r = 0; r < n; r++) printf(" {%d,%d}", a[r].i, a[r].j);
    printf("\n");
    /* the exam's textual example: friends 1 and 4 are indirect friends via 2 or 5? */
    return 0;
}
