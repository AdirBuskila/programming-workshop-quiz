#include <stdio.h>
#include <ctype.h>
/* official solution, verbatim */
int group_sort(char *str)
{
    char last_capital, last_small, last_digit;
    int i;
    last_capital = last_small = last_digit = '\0';
    for (i = 0; str[i] != '\0'; i++)
        if (isupper(str[i]))
            if (str[i] < last_capital)
                return 0;
            else
                last_capital = str[i];
        else
            if (islower(str[i]))
                if (str[i] < last_small)
                    return 0;
                else
                    last_small = str[i];
            else
                if (isdigit(str[i]))
                    if (str[i] < last_digit)
                        return 0;
                    else
                        last_digit = str[i];
    return 1;
}
int main(void)
{
    printf("B4$Ca#%%ds5P8P&9zY -> %d (expect 1)\n", group_sort("B4$Ca#%ds5P8P&9zY"));
    printf("B4$Ca#%%ds5P8P&9rY -> %d (expect 0)\n", group_sort("B4$Ca#%ds5P8P&9rY"));
    printf("empty -> %d (expect 1)\n", group_sort(""));
    printf("aab -> %d (expect 1, not strict)\n", group_sort("aab"));
    printf("ba -> %d (expect 0)\n", group_sort("ba"));
    printf("9a8 -> %d (expect 0)\n", group_sort("9a8"));
    printf("A1a2B3b -> %d (expect 1)\n", group_sort("A1a2B3b"));
    return 0;
}
