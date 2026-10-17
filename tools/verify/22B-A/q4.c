/* q4a: while(!feof) loop on "1 2 3 4 5 " ; q4b: double (**q)(); q4c: malloc(0); q4d: pointer reassign */
#include <stdio.h>
#include <stdlib.h>
double one(void) { return 1.0; }
int main(void)
{
    FILE *fptr = fopen("nums.txt", "w"); fputs("1 2 3 4 5 ", fptr); fclose(fptr);
    fptr = fopen("nums.txt", "r");
    int x, iterations = 0;
    printf("4a output: ");
    while (!feof(fptr)) { fscanf(fptr, "%d", &x); printf("%d ", x); iterations++; }
    printf("\n4a iterations=%d\n", iterations);
    fclose(fptr);

    double (*p)() = one; double (**q)() = &p;
    printf("4b: (*q)() = %f, sizeof(q)=%d\n", (*q)(), (int)sizeof(q));

    int *m = (int*)malloc(0);
    printf("4c: malloc(0) -> %s\n", m ? "non-NULL" : "NULL");

    char *str = "hello"; char *before = str;
    str = "good-bye";
    printf("4d: str=%s changed_pointer=%d\n", str, str != before);
    return 0;
}
