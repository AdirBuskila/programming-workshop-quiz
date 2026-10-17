#include <stdio.h>
int main() { char st[2]; FILE* fptr = fopen("file.dat", "r"); if (!fptr) return 1;
 while (fgets(st, 2, fptr)) fputs(fgets(st, 2, fptr),stdout); fclose(fptr); puts(""); return 0; }
