#include <stdio.h>
#include <string.h>
#include <ctype.h>
int nums_in_halves(char* str, int* num1, int* num2)
{
    int len = strlen(str), i;
    *num1 = *num2 = 0;
    for (i = 0; i < len / 2; i++)
        if ( islower(str[i]) )
            (*num1)++;
    for (i = (len + 1) / 2; str[i] != '\0'; i++)
        if ( isupper(str[i]) )
            (*num2)++;
    if (len % 2 == 0)
        return 0;
    if ( isdigit(str[len / 2]) )
        return 1;
    return -1;
}
int main(void)
{
    const char *t[] = { "t&u5Y%as3k$R", "t&u5Y%4as3k$R", "t&u5Y%&as3k$R", "", "a", "7", "aB", "Ab" };
    for (int k = 0; k < 8; k++)
    {
        int a, b, r = nums_in_halves((char*)t[k], &a, &b);
        printf("\"%s\" -> num1=%d num2=%d return=%d\n", t[k], a, b, r);
    }
    return 0;
}
