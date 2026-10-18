#include <stdio.h>
int main(){ char c; FILE* f=fopen("refute_file.dat","w"); fputs("abc",f); fclose(f); f=fopen("refute_file.dat","r");
 while (c = fgetc(f) != EOF) printf("%d", c); fclose(f); puts(""); return 0;}
