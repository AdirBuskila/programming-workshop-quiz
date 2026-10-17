#include <stdio.h>
int main(){
char str1[] = "hello", *str2 = "hello";
printf("cmp=%d p1=%p p2=%p\n",str1==str2,(void*)str1,(void*)str2);
if (str1 == str2)   printf("yes");
return 0;}
