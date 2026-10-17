#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int *p = (int*)malloc(5 * sizeof(int));
    int *old = p;
    p = (int*)realloc(p, 0);
    printf("p==NULL: %d (old was %s)\n", p == NULL, old ? "non-NULL" : "NULL");
    return 0;
}
