#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {
    char address[30];
    int rooms;
    int price;
} apartment;

apartment* appropriateAppartment(char* fileName, int room_number, int max_price,
    int* count)
{
    int i=0;
    FILE* fptr = fopen(fileName, "rb");
    apartment* approp_apart_units, unit;
    *count = 0;
    if (!fptr)
        return NULL;

    /* Estimation of array size */
    fread(&unit, sizeof(apartment), 1, fptr);
    while (!feof(fptr))
    {
        if (unit.rooms == room_number && unit.price <= max_price)
            (*count)++;
        fread(&unit, sizeof(apartment), 1, fptr);
    }

    if (*count == 0)
    {
        fclose(fptr);
        return NULL;
    }

    approp_apart_units = (apartment*)calloc(*count, sizeof(apartment)); //array allocation

    /* Filling of array */
    rewind(fptr);
    fread(&unit, sizeof(apartment), 1, fptr);
    while (!feof(fptr))
    {
        if (unit.rooms == room_number && unit.price <= max_price)
            approp_apart_units[i++] = unit;
        fread(&unit, sizeof(apartment), 1, fptr);
    }

    fclose(fptr);
    return approp_apart_units;
}
int main(void)
{
    apartment all[5] = { {"Begin 7",3,700000}, {"Reznik 4",4,1000000}, {"Ben-Gurion 27",5,4000000}, {"Dubnov 13",3,1100000}, {"Cohen 66",3,900000} };
    FILE *f = fopen("apts.bin", "wb"); fwrite(all, sizeof(apartment), 5, f); fclose(f);
    int cnt; apartment *r = appropriateAppartment("apts.bin", 3, 1000000, &cnt);
    printf("count=%d\n", cnt);
    for (int i = 0; i < cnt; i++) printf("%s %d %d\n", r[i].address, r[i].rooms, r[i].price);
    r = appropriateAppartment("apts.bin", 9, 1000000, &cnt); printf("none: count=%d ptr=%s\n", cnt, r ? "non-null" : "NULL");
    r = appropriateAppartment("missing.bin", 3, 1000000, &cnt); printf("missing: count=%d ptr=%s\n", cnt, r ? "non-null" : "NULL");
    return 0;
}
