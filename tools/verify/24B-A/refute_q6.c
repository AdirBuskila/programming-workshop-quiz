#include <stdio.h>
int main(){ char st[2]; FILE* f=fopen("refute_file.dat","w"); fputs("1234",f); fclose(f); f=fopen("refute_file.dat","r");
 while (fgets(st,2,f)) fputs(fgets(st,2,f),stdout); fclose(f); puts(""); return 0;}
