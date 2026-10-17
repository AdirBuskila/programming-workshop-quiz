#include <stdio.h>
void main()
{
    char *str = "hello";
    str[0] = str[4] = '\0';
    printf("survived: %p\n", (void*)str);
}
