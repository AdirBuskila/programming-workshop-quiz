#include <stdio.h>
#include <string.h>
int v1(char* file_name, char* word)
{
    FILE* fptr = fopen(file_name, "r");
    char str[101], *sub_str, *p;
    int count = 0, len = strlen(word);
    if (!fptr) return -1;
    while (fgets(str, 101, fptr))
    {
        sub_str = str;
        while ((p = strstr(sub_str, word)) != NULL)
        {
            if ((p == str || *(p - 1) == ' ') && (*(p + len) == ' ' || *(p + len) == '\n'))
                count++;
            sub_str = p + len + 1;
        }
    }
    fclose(fptr);
    return count;
}
int v2(char* file_name, char* word)
{
    FILE* fptr = fopen(file_name, "r");
    char str[100], *separators = " \n", *token;
    int count = 0;
    if (!fptr) return -1;
    while (fgets(str, 100, fptr))
    {
        token = strtok(str, separators);
        while (token != NULL)
        {
            if (strcmp(token, word) == 0) count++;
            token = strtok(NULL, separators);
        }
    }
    fclose(fptr);
    return count;
}
int main(void){
    FILE*f=fopen("t_ex.txt","w");
    fputs("I believe that they live here and who does not live here\nMike lives in this house\nAnd who does live here ? We live\n10 alive creatures live in this lived place\n",f); fclose(f);
    printf("v1=%d v2=%d missing=%d %d\n", v1("t_ex.txt","live"), v2("t_ex.txt","live"), v1("nofile.txt","a"), v2("nofile.txt","a"));
    return 0; }
