/* Arbiter check for 21B-B Q1: official filesMerge vs the minimal fix (only in1 is moved back, and only if not at EOF).
   Build: clang -w arb_q1.c -o arb_q1.exe && arb_q1.exe   (all CASES must print "fixed OK") */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
void next_number(FILE* in, FILE* out, int* num, char* ch)
{ fprintf(out, "%d ", *num); if ((*ch = fgetc(in)) != '\n') fscanf(in, "%d", num); }
void rows_merge(FILE* in1, FILE* in2, FILE* out)
{
    char ch1=0, ch2=0; int num1, num2;
    fscanf(in1, "%d", &num1); fscanf(in2, "%d", &num2);
    while (ch1 != '\n' && ch2 != '\n')
        if (num1 < num2) next_number(in1, out, &num1, &ch1); else next_number(in2, out, &num2, &ch2);
    while (ch1 != '\n') next_number(in1, out, &num1, &ch1);
    while (ch2 != '\n') next_number(in2, out, &num2, &ch2);
    fputc('\n', out);
}
void copy_file(FILE* in, FILE* out) { char ch; while ((ch = fgetc(in)) != EOF) fputc(ch, out); }
static void merge(const char* a, const char* b, const char* o, int fixed)
{
    FILE* in1 = fopen(a, "r"); FILE* in2 = fopen(b, "r"); FILE* out = fopen(o, "w");
    if (!in1 || !in2 || !out) exit(1);
    while (fgetc(in1) != EOF && fgetc(in2) != EOF)
    { fseek(in1, -1, SEEK_CUR); fseek(in2, -1, SEEK_CUR); rows_merge(in1, in2, out); }
    if (fixed) { if (!feof(in1)) fseek(in1, -1, SEEK_CUR); }
    else { fseek(in1, -1, SEEK_CUR); fseek(in2, -1, SEEK_CUR); }
    copy_file(in1, out); copy_file(in2, out);
    fclose(in1); fclose(in2); fclose(out);
}
static void w(const char *n, const char *s){ FILE *f=fopen(n,"wb"); fputs(s,f); fclose(f); }
static char buf[4096];
static const char* rd(const char *n){ FILE *f=fopen(n,"rb"); size_t k=fread(buf,1,sizeof buf-1,f); buf[k]=0; fclose(f); return buf; }
/* compare ignoring the space the official next_number writes before '\n' */
static int same(const char* got, const char* want)
{ char g[4096]; int k=0; for (const char* p=got; *p; p++) { if (*p==' ' && p[1]=='\n') continue; g[k++]=*p; } g[k]=0; return strcmp(g,want)==0; }
static int blank_lines(const char* s){ int n=0; if (s[0]=='\n') n++; for (const char* p=s; *p; p++) if (p[0]=='\n' && p[1]=='\n') n++; return n; }
int main(void)
{
    _set_fmode(_O_BINARY); /* UCRT text-mode fseek(f,-1,SEEK_CUR) fails */
    struct { const char *name, *a, *b, *want; } C[] = {
        {"exam example (4 vs 3 lines)", "3 8 12 16 20\n0 2 2 6\n9 10 10 11 19 26\n4 4 4 5\n", "9 17\n2 6 7 11\n5 13 14 18\n",
         "3 8 9 12 16 17 20\n0 2 2 2 6 6 7 11\n5 9 10 10 11 13 14 18 19 26\n4 4 4 5\n"},
        {"infile_2 longer", "1 5\n", "2 3\n7 8\n9\n", "1 2 3 5\n7 8\n9\n"},
        {"equal length", "1 4\n2\n", "3\n1 1\n", "1 3 4\n1 1 2\n"},
        {"infile_1 empty", "", "5 6\n", "5 6\n"},
        {"infile_2 empty", "5 6\n7\n", "", "5 6\n7\n"},
    };
    int ok = 1;
    for (int i = 0; i < 5; i++) {
        w("a.txt", C[i].a); w("b.txt", C[i].b);
        merge("a.txt", "b.txt", "o.txt", 0); int ob = blank_lines(rd("o.txt")); int os = same(buf, C[i].want);
        merge("a.txt", "b.txt", "o.txt", 1); int fs = same(rd("o.txt"), C[i].want);
        printf("%-28s official: %s (blank lines %d) | fixed %s\n", C[i].name, os ? "OK " : "BAD", ob, fs ? "OK" : "BAD");
        ok &= fs;
    }
    remove("a.txt"); remove("b.txt"); remove("o.txt");
    puts(ok ? "ALL FIXED OK" : "FIX FAILS");
    return !ok;
}
