#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
typedef struct pair { int num_text_rows; int num_bin_records; } Pair;
#ifndef DECUP
#define DECUP dec *= 10;
#endif
#ifndef RET
#define RET return count/rec_size;
#endif
int NumOfRows(char *fname) {
    FILE *f = fopen(fname, "r"); int count = 0; char c;
    if (!f) return 0;
    while ( (c=fgetc(f))!=EOF ) if (c == '\n') count++;
    fclose(f); return count;
}
int NumOfRecords(char *fname, int rec_size) {
    char c; FILE *f = fopen(fname, "rb"); int count = 0;
    if (!f) return 0;
    while (fread(&c, 1, 1, f)) count++;
    fclose(f);
    RET
}
int getNumber(char *str) {
    int i = 0, dec = 1, num = 0;
    while (str[i] != '.') i++;
    i--;
    while (isdigit(str[i])) { num += (str[i--] - '0') * dec; DECUP }
    return num;
}
Pair *numRowsRecords(char **Infiles, int n) {
    Pair *Results = (Pair *)malloc(n * sizeof(Pair)); int i;
    for (i = 0; i < n; i++) {
        if (Infiles[i][0] == 'b' || Infiles[i][0] == 'B') {
            int rec = getNumber(Infiles[i]);
            Results[i].num_bin_records = NumOfRecords(Infiles[i], rec);
            Results[i].num_text_rows = -1;
        } else {
            Results[i].num_text_rows = NumOfRows(Infiles[i]);
            Results[i].num_bin_records = -1;
        }
    }
    return Results;
}
int main(){
 FILE*f=fopen("MyFile.dat","w");fputs("Name: Moshe\nDate: 24.05.2012\n",f);fclose(f);
 f=fopen("binFile120.doc","wb");for(int i=0;i<600;i++)fputc(i%251,f);fclose(f);
 f=fopen("Students.txt","w");fputs("Amir Shai\nDoron Levi\nTomer Cohen\n",f);fclose(f);
 f=fopen("B_Numbers68.xr","wb");for(int i=0;i<68*4;i++)fputc(i%7,f);fclose(f);
 char*names[]={"MyFile.dat","binFile120.doc","Students.txt","B_Numbers68.xr","Letters.dat","bmissing5.bin"};
 Pair*r=numRowsRecords(names,6);for(int i=0;i<6;i++)printf("%d %d\n",r[i].num_text_rows,r[i].num_bin_records);
 printf("gn %d\n",getNumber("binFile120.doc"));
}
