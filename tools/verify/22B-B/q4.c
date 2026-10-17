#include <stdio.h>
#include <stdlib.h>
int g;  /* a global variable: "global" is not a C keyword */
int main(void)
{
    int a[3][3] = { {1,2,3},{4,5,6},{7,8,9} }, i;
    printf("4b: ");
    for (i = 0; i < 3; i++)
        printf("%d %d ", *a[i], *(*(a + i) + i));
    printf("\n");
    FILE *f;
    f = fopen("t.txt", "w"); fputs("x", f); fclose(f);
    f = fopen("t.txt", "r");  printf("4c r write: %d\n", fputc('y', f) == EOF);  fclose(f);
    f = fopen("t.txt", "w");  printf("4c w read: %d\n", fgetc(f) == EOF);  fclose(f);
    f = fopen("t.txt", "r+"); printf("4c r+ both: %d %d\n", fgetc(f) == EOF, fseek(f, 0, SEEK_SET) == 0); fclose(f);
    f = fopen("t.txt", "w+"); printf("4c w+ both: %d\n", fputc('z', f) != EOF); fclose(f);
    return 0;
}
