#include <stdio.h>
#include <stdlib.h>
/* official solution, verbatim */
#define COLS 5 //example
void file_to_sparse_matrix(char *filename, int A[][COLS], int
rows, int cols)
{
    int i, j, num;
    char ch;
    FILE *fptr = fopen(filename, "r");
    if (!fptr)
        exit(1);
    for (i = 0; i < rows; i++)
        for (j = 0; j < cols; j++)
            A[i][j] = 0;
    for (i = 0; i < rows; i++)
    {
        fscanf(fptr,"%d", &num); //number of row
        while ((ch = fgetc(fptr)) != '\n')
        {
            fscanf(fptr, "%d%d", &num, &j);
            A[i][j] = num;
        }
    }
    fclose(fptr);
}
int main(void)
{
    FILE *f = fopen("sparse.txt","w");
    fputs("0 4 2 7 4\n1 3 0\n2 9 0 1 1 6 3\n3\n", f); fclose(f);
    int A[4][COLS];
    file_to_sparse_matrix("sparse.txt", A, 4, COLS);
    for (int i=0;i<4;i++){ for(int j=0;j<COLS;j++) printf("%d ",A[i][j]); printf("\n"); }
    return 0;
}
