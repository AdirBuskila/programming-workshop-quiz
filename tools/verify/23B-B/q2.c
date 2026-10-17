#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {
    char film_code[10];
    int copies;
    int year;
} film;

film* appropriateFilm(char* fileName, int copies_limit, int last_year, int* size)
{
    int i = 0;
    FILE* fptr = fopen(fileName, "rb");
    film* approp_film_units, unit;
    *size = 0;
    if (!fptr)
        return NULL;

    /* Estimation of array size */
    fread(&unit, sizeof(film), 1, fptr);
    while (!feof(fptr))
    {
        if (unit.copies <= copies_limit && unit.year <= last_year)
            (*size)++;
        fread(&unit, sizeof(film), 1, fptr);
    }

    if (*size == 0)
    {
        fclose(fptr);
        return NULL;
    }

    approp_film_units = (film*)calloc(*size, sizeof(film)); //array allocation

    /* Filling of array */
    rewind(fptr);
    fread(&unit, sizeof(film), 1, fptr);
    while (!feof(fptr))
    {
        if (unit.copies <= copies_limit && unit.year <= last_year)
            approp_film_units[i++] = unit;
        fread(&unit, sizeof(film), 1, fptr);
    }

    fclose(fptr);
    return approp_film_units;
}
int main(void)
{
    film all[5] = { {"A346-f",2,1967}, {"D8120-fx",4,1960}, {"S516-t",1,1970}, {"R11-v",2,1972}, {"G555-xx",3,2010} };
    FILE *f = fopen("films.bin", "wb"); fwrite(all, sizeof(film), 5, f); fclose(f);
    int n; film *r = appropriateFilm("films.bin", 2, 1970, &n);
    printf("size=%d\n", n);
    for (int i = 0; i < n; i++) printf("%s %d %d\n", r[i].film_code, r[i].copies, r[i].year);
    r = appropriateFilm("films.bin", 0, 1970, &n); printf("none: size=%d ptr=%s\n", n, r ? "non-NULL" : "NULL");
    r = appropriateFilm("missing.bin", 2, 1970, &n); printf("missing: size=%d ptr=%s\n", n, r ? "non-NULL" : "NULL");
    return 0;
}
