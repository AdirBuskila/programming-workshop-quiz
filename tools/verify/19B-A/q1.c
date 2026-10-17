#include <stdio.h>
#include <stdlib.h>
/* official solution, verbatim */
void cyclic_shift_to_file (char **str, int n, char *fileName)
{
    int i;
    FILE *fptr = fopen(fileName, "w");
    if (!fptr)
        exit(1);
    for (i=1; i<n; i++)
    {
        fputc(i+'0', fptr);
        fputs(str[i]+1, fptr);
        fputc('\n', fptr);
    }
    fputc(n+'0', fptr);
    fputs(str[0]+1, fptr);
    fputc('\n', fptr);
    fclose(fptr);
}
int main(void)
{
    char *s[4] = {"1 Bill Johns, 28", "2 Ron Smith, 367", "3 Arthur Mitchell, 84", "4 Eduard Stone, 17"};
    cyclic_shift_to_file(s, 4, "out.txt");
    FILE *f = fopen("out.txt","rb"); int c; while((c=fgetc(f))!=EOF) putchar(c); fclose(f);
    return 0;
}
