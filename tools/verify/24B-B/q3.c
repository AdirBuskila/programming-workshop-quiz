#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
void reverseString(char* str)
{
    int i = 0, j = strlen(str) - 1; char temp;
    for (; i < j; i++, j--) { temp = str[i]; str[i] = str[j]; str[j] = temp; }
}
int hasUniqueLetters(const char* str)
{
    char temp[26] = { 0 }; int i, index;
    for (i = 0; str[i] != '\0'; i++)
    {
        if (!isalpha(str[i])) return 0;
        index = tolower(str[i]) - 'a';
        if (temp[index] > 0) return 0;
        temp[index]++;
    }
    return 1;
}
void processFiles(const char* inputFilename, const char* outputFilename)
{
    char str[101];
    FILE* fin = fopen(inputFilename, "r"), *fout = fopen(outputFilename, "w");
    if (!fin || !fout) exit(1);
    while (fgets(str, 101, fin))
    {
        str[strlen(str) - 1] = '\0';
        if (hasUniqueLetters(str)) { reverseString(str); fprintf(fout, "%s\n", str); }
    }
    fclose(fin); fclose(fout);
}
int main(void){ FILE*f=fopen("t_in.txt","w"); fputs("abc#xyz\ntable\nAlisa\nWalla\nMichael\n",f); fclose(f);
 processFiles("t_in.txt","t_out.txt"); f=fopen("t_out.txt","r"); char b[200]; while(fgets(b,200,f))fputs(b,stdout); return 0; }
