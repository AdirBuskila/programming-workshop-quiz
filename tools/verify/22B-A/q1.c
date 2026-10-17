#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char* duplicateString(char* base, char* middle, int times)
{
    // zeroed dynamic array
    char* str = calloc(times * strlen(base) + (times - 1) * strlen(middle) + 1, sizeof(char));
    int i;

    for (i = 1; i <= times - 1; i++)
    {
        strcat(str, base);
        strcat(str, middle);
    }
    strcat(str, base);
    return str;
}
int main(void)
{
    char *s = duplicateString("base", "middle", 3);
    printf("%s\n", s);
    if (strcmp(s, "basemiddlebasemiddlebase")) { printf("FAIL\n"); return 1; }
    free(s);
    s = duplicateString("ab", "-", 1); printf("%s\n", s); if (strcmp(s, "ab")) return 1; free(s);
    s = duplicateString("ab", "", 2); printf("%s\n", s); if (strcmp(s, "abab")) return 1; free(s);
    printf("OK\n");
    return 0;
}
