#include <stdio.h>
#include <stdlib.h>
int main(){ int*p=(int*)realloc(NULL,sizeof(int)); printf("%d\n",p!=NULL); free(p); return 0;}
