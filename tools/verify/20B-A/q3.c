#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
/* official solution, verbatim */
typedef struct pair
{
    int num_text_rows;
    int num_bin_records;
} Pair;
int NumOfRows(char *fname) {
    FILE *f = fopen(fname, "r");
    int count = 0;
    char c;
    if (!f) return 0;
    while ( (c=fgetc(f))!=EOF )
        if (c == '\n') count++;
    fclose(f);
    return count;
}
int NumOfRecords(char *fname, int rec_size) {
    char c;
    FILE *f = fopen(fname, "rb");
    int count = 0;
    if (!f) return 0;
    while (fread(&c, 1, 1, f))
        count++;
    fclose(f);
    return count/rec_size;
}
int getNumber(char *str) {
    int i = 0, dec = 1, num = 0;
    while (str[i] != '.') i++;
    i--;
    while (isdigit(str[i])) {
        num += (str[i--] - '0') * dec;
        dec *= 10;
    }
    return num;
}
Pair *numRowsRecords(char **Infiles, int n) {
    Pair *Results = (Pair *)malloc(n * sizeof(Pair));
    int i;
    for (i = 0; i < n; i++) {
        if (Infiles[i][0] == 'b' || Infiles[i][0] == 'B') {
            int rec = getNumber(Infiles[i]);
            Results[i].num_bin_records = NumOfRecords(Infiles[i], rec);
            Results[i].num_text_rows = -1;
        }
        else {
            Results[i].num_text_rows = NumOfRows(Infiles[i]);
            Results[i].num_bin_records = -1;
        }
    }
    return Results;
}
static void wtxt(const char *n, const char *s){ FILE *f=fopen(n,"w"); fputs(s,f); fclose(f); }
static void wbin(const char *n, int bytes){ FILE *f=fopen(n,"wb"); for(int i=0;i<bytes;i++) fputc(i%251,f); fclose(f); }
int main(void)
{
    wtxt("MyFile.dat", "Name: Moshe\nDate: 24.05.2012\n");
    wbin("binFile120.doc", 5*120);
    wtxt("Students.txt", "Amir Shai\nDoron Levi\nTomer Cohen\n");
    wbin("B_Numbers68.xr", 4*68);
    remove("Letters.dat");   /* a file that cannot be opened */
    char *names[5] = {"MyFile.dat","binFile120.doc","Students.txt","B_Numbers68.xr","Letters.dat"};
    Pair *R = numRowsRecords(names, 5);
    for (int i=0;i<5;i++) printf("%s: %d %d\n", names[i], R[i].num_text_rows, R[i].num_bin_records);
    return 0;
}
