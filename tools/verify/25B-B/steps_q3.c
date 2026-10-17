#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
typedef struct { char id[10]; char name[31]; double total; } clientData;
int main(void)
{
	printf("sizeof(clientData)=%d offsetof(total)=%d\n", (int)sizeof(clientData), (int)offsetof(clientData,total));
	return 0;
}
