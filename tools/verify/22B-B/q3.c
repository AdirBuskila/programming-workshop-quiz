#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {
    char model[20];
    int price;
    int year;
} car;
typedef struct item {
    int price;
    int year;
    struct item* next;
} Item;

Item* appropriateCar(char* fileName, char* desired_model, int max_price, int min_year)
{
    FILE* fptr = fopen(fileName, "rb");
    car unit;
    Item* lst, * curr;
    if (!fptr)
        return NULL;
    curr = lst = (Item*)malloc(sizeof(Item)); //dummy item
    fread(&unit, sizeof(car), 1, fptr);
    while (!feof(fptr))
    {
        if (strcmp(unit.model, desired_model) == 0 && unit.price <= max_price && unit.year >= min_year)
        {
            curr->next = (Item*)malloc(sizeof(Item));
            curr = curr->next;
            curr->price = unit.price;
            curr->year = unit.year;
        }
        fread(&unit, sizeof(car), 1, fptr);
    }
    curr->next = NULL;
    /* Deleting dummy */
    curr = lst;
    lst = lst->next;
    free(curr);
    fclose(fptr);
    return lst;
}
int main(void)
{
    car all[5] = { {"Subaru",90000,2019}, {"Mazda",95000,2020}, {"Subaru",10000,2009}, {"Toyota",200000,2022}, {"Subaru",25000,2012} };
    FILE *f = fopen("cars.bin", "wb"); fwrite(all, sizeof(car), 5, f); fclose(f);
    Item *l = appropriateCar("cars.bin", "Subaru", 100000, 2010);
    for (; l; l = l->next) printf("[%d %d] ", l->price, l->year);
    printf("\n");
    l = appropriateCar("cars.bin", "Opel", 100000, 2010); printf("none -> %s\n", l ? "non-NULL" : "NULL");
    l = appropriateCar("missing.bin", "Subaru", 100000, 2010); printf("missing -> %s\n", l ? "non-NULL" : "NULL");
    return 0;
}
