#include <stdio.h>
int main(){ char *s="ab"; printf("%d\n",sizeof s[0]+sizeof s[1]-sizeof'a'-sizeof'b'); printf("%zu\n", sizeof s[0]+sizeof s[1]-sizeof'a'-sizeof'b'); printf("%zu\n",sizeof 'a'); int a[100]; printf("%d\n", (int)(sizeof a + sizeof sizeof a + sizeof sizeof sizeof a)); printf("%d\n",~0); printf("%zu %zu\n", sizeof(double*), sizeof(char*)); return 0;}
