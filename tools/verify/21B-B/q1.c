#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <stdlib.h>
/* official solution, verbatim */
void next_number(FILE* in, FILE* out, int* num, char* ch)
{
    fprintf(out, "%d ", *num);
    if ((*ch = fgetc(in)) != '\n')
        fscanf(in, "%d", num);
}
void rows_merge(FILE* in1, FILE* in2, FILE* out)
{
    char ch1=0, ch2=0;
    int num1, num2;
    fscanf(in1, "%d", &num1);
    fscanf(in2, "%d", &num2);
    while (ch1 != '\n' && ch2 != '\n')
        if (num1 < num2)
            next_number(in1, out, &num1, &ch1);
        else
            next_number(in2, out, &num2, &ch2);
    while (ch1 != '\n')
        next_number(in1, out, &num1, &ch1);
    while (ch2 != '\n')
        next_number(in2, out, &num2, &ch2);
    fputc('\n', out);
}
void copy_file(FILE* in, FILE* out)
{
    char ch;
    while ((ch = fgetc(in)) != EOF)
        fputc(ch, out);
}
void filesMerge(char* infile1, char* infile2, char* outfile)
{
    FILE* in1 = fopen(infile1, "r");
    FILE* in2 = fopen(infile2, "r");
    FILE* out = fopen(outfile, "w");
    if (!in1 || !in2 || !out)
        exit(1);
    while (fgetc(in1) != EOF && fgetc(in2) != EOF)
    {
        fseek(in1, -1, SEEK_CUR);
        fseek(in2, -1, SEEK_CUR);
        rows_merge(in1, in2, out);
    }
    fseek(in1, -1, SEEK_CUR);
    fseek(in2, -1, SEEK_CUR);
    copy_file(in1, out);
    copy_file(in2, out);
    fclose(in1);
    fclose(in2);
    fclose(out);
}
/* harness: the exam example, then a case with infile_2 longer */
static void w(const char *n, const char *s){ FILE *f=fopen(n,"wb"); fputs(s,f); fclose(f); }
static void show(const char *n){ FILE *f=fopen(n,"rb"); int c; while((c=fgetc(f))!=EOF) putchar(c); fclose(f); }
int main(void)
{
    _set_fmode(_O_BINARY); /* UCRT text-mode fseek(f,-1,SEEK_CUR) fails; binary mode behaves like the POSIX/classic CRT the solution assumes */
    w("i1.txt", "3 8 12 16 20\n0 2 2 6\n9 10 10 11 19 26\n4 4 4 5\n");
    w("i2.txt", "9 17\n2 6 7 11\n5 13 14 18\n");
    filesMerge("i1.txt","i2.txt","o.txt");
    printf("--- example (infile_1 has 4 lines, infile_2 has 3)\n"); show("o.txt");
    w("i3.txt", "1 5\n");
    w("i4.txt", "2 3\n7 8\n");
    filesMerge("i3.txt","i4.txt","o2.txt");
    printf("--- infile_2 longer\n"); show("o2.txt");
    return 0;
}
