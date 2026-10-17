#include <stdio.h>
#include <string.h>
typedef struct { char last_name[30], first_name[30]; unsigned id; } person;
/* official solution, verbatim */
int ordered_person_array(person* person_arr, int n)
{
    int i, cmp;
    for (i = 1; i < n; i++)
        if ( (cmp = strcmp(person_arr[i].last_name, person_arr[i - 1].last_name)) < 0 )
            return 0;
        else
            if (cmp == 0)
                if ((cmp=strcmp(person_arr[i].first_name, person_arr[i-1].first_name))<0)
                    return 0;
                else
                    if (cmp == 0)
                        if (person_arr[i].id < person_arr[i - 1].id)
                            return 0;
    return 1;
}
int main(void)
{
    person a[10] = {
        {"Asher","Mike",231567809},{"Bern","David",216578900},{"Borgman","Joseph",354678903},
        {"Cohen","Abraham",224567821},{"Cohen","Den",206666431},{"Levi","Ilan",290876441},
        {"Levi","Omri",245689432},{"Levi","Omri",245689436},{"Smith","Jack",345389010},
        {"Smith","John",311232111}};
    printf("example 1: %d\n", ordered_person_array(a, 10));
    person t = a[6]; a[6] = a[7]; a[7] = t;
    printf("example 2: %d\n", ordered_person_array(a, 10));
    return 0;
}
