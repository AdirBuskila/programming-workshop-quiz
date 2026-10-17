#include <stdio.h>
#include <stdlib.h>
int **file_to_sequences_in_rows(char* filename, int **S, int *rows)
{
    char ch;
    int **A, num, size, start_row, i, j, k;
    FILE* fptr = fopen(filename, "r");
    if (!fptr)
        exit(1);
    /* Estimation of the number of rows */
    *rows = 0;
    while ((ch = fgetc(fptr)) != EOF)
        if (ch == '\n')
            (*rows)++;
    A = (int**)calloc(*rows, sizeof(int*)); //pointer array allocation
    *S = (int*)calloc(*rows, sizeof(int)); //array of row sizes allocation
    rewind(fptr);
    for (i = 0; i < *rows; i++)
    {
        start_row = ftell(fptr);
        /* Estimation of row size */
        do
        {
            fscanf(fptr, "%d%d", &num, &size);
            (*S)[i] += size;
        } while ((ch = fgetc(fptr)) != '\n');
        A[i] = (int*)calloc((*S)[i], sizeof(int)); //row allocation
        /* File row -> array row */
        fseek(fptr, start_row, SEEK_SET);
        k = 0;
        do
        {
            fscanf(fptr, "%d%d", &num, &size);
            for (j = 1; j <= size; j++, k++)
                A[i][k] = num;
        } while ((ch = fgetc(fptr)) != '\n');
    } //for i
    fclose(fptr);
    return A;
}
int main(void)
{
    FILE *f = fopen("seq.txt", "w");
    fputs("4 2 7 4 3 3\n2 6 1 2\n9 1 12 3\n3 2 18 5 0 2\n", f); fclose(f);
    int *S, rows, **A = file_to_sequences_in_rows("seq.txt", &S, &rows);
    printf("rows=%d\n", rows);
    for (int i = 0; i < rows; i++) { printf("%d:", S[i]); for (int j = 0; j < S[i]; j++) printf(" %d", A[i][j]); printf("\n"); }
    return 0;
}
