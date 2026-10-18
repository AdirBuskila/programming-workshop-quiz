#include <stdio.h>
#include <stdlib.h>
#ifndef FP
#define FP fputs(str[i]+1, fptr);
#endif
#ifndef LASTN
#define LASTN fputc(n+'0', fptr);
#endif
void cyclic_shift_to_file (char **str, int n, char *fileName)
{
    int i; FILE *fptr = fopen(fileName, "w"); if (!fptr) exit(1);
    for (i=1; i<n; i++) { fputc(i+'0', fptr); FP fputc('\n', fptr); }
    LASTN fputs(str[0]+1, fptr); fputc('\n', fptr); fclose(fptr);
}
int main(){ char*s[]={"1 Bill Johns, 28","2 Ron Smith, 367","3 Arthur Mitchell, 84","4 Eduard Stone, 17"};
 cyclic_shift_to_file(s,4,"o.txt"); FILE*f=fopen("o.txt","rb");int c;while((c=fgetc(f))!=EOF)printf(c<32&&c!='\n'?"<%d>":"%c",c);
 cyclic_shift_to_file(s,1,"o.txt"); f=fopen("o.txt","rb");printf("--n1:");while((c=fgetc(f))!=EOF)printf(c<32&&c!='\n'?"<%d>":"%c",c);}
