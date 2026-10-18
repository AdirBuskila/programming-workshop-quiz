#include <stdio.h>
int main(){ FILE*f=fopen("t.txt","w"); fputs("1 2 3 4 5 ",f); fclose(f);
 FILE*fptr=fopen("t.txt","r"); int x=-1,n=0;
 while (!feof(fptr)) { fscanf(fptr, "%d", &x); printf("%d ", x); n++; }
 printf("\nn=%d\n",n);
 /* variant without trailing space */
 f=fopen("t2.txt","w"); fputs("1 2 3 4 5",f); fclose(f); fptr=fopen("t2.txt","r"); n=0;
 while (!feof(fptr)) { fscanf(fptr, "%d", &x); printf("%d ", x); n++; } printf("\nn=%d\n",n);
 return 0;}
