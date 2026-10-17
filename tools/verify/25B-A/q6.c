#include <stdio.h>
int main() { char c; FILE* fptr = fopen("file.dat", "r"); if (!fptr) return 1;
 while (c = fgetc(fptr) != EOF) printf("%d", c); fclose(fptr); puts(""); return 0; }
