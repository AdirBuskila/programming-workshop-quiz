#include <stdio.h>
#include <string.h>
typedef struct
{
    char first_name[30], last_name[30];
} name;
int ordered_name_array(name* name_arr, int n)
{
    int i;
    for (i = 1; i < n; i++)
        if (strcmp(name_arr[i].first_name, name_arr[i - 1].first_name) < 0)
        {
            for (i = 1; i < n; i++)
                if (strcmp(name_arr[i].last_name, name_arr[i - 1].last_name) < 0)
                    return 0;
            return 2;
        }
    return 1;
}
int main(void)
{
    name ex[7] = { {"Mike","Asher"}, {"David","Bern"}, {"Joseph","Borgman"}, {"Alon","Kapulski"}, {"Ilan","Mizrachi"}, {"Oren","Nodel"}, {"Abraham","Rosen"} };
    printf("example (sorted by last name only): %d\n", ordered_name_array(ex, 7));
    name byfirst[3] = { {"Alon","Zed"}, {"Ben","Bar"}, {"Carl","Aba"} };
    printf("sorted by first name only: %d\n", ordered_name_array(byfirst, 3));
    name none[3] = { {"Ben","Zed"}, {"Alon","Bar"}, {"Carl","Aba"} };
    printf("not sorted at all: %d\n", ordered_name_array(none, 3));
    name both[3] = { {"Alon","Aba"}, {"Ben","Bar"}, {"Carl","Cohen"} };
    printf("sorted by both: %d\n", ordered_name_array(both, 3));
    printf("one element: %d\n", ordered_name_array(both, 1));
    return 0;
}
