#include <stdio.h>
int x;
void f(){static int x;printf("%d",x);printf("%d",++x);}
int main(){f();printf("%d",x);printf("%d",++x);f();puts("");
printf("%d",printf("%d%d",printf("%d",11),printf("%d",11)));puts("");
int i=64;int c=0;for(;i;i>>=1)c++;printf("%d\n",c);
char C[]="C++",ch;for(ch=0;ch<3;ch++)C[ch]+=!ch?'+'-'+':'-'-'+';puts(C);
for (i=0; i<sizeof"sizeof"[i]; i++) printf("%d",sizeof"sizeof"[i]);puts("");
int a=-8;printf("%d\n",a>>1);
return 0;}
