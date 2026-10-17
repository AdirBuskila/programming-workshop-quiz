#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char* my_strtok(char* sentence, char* separators)
{
    int i = 0;
    char* word;
    static char* start;
    if (sentence != NULL)
        start = sentence;
    word = (char*)malloc(strlen(start) + 1);
    while (*start && strchr(separators, *start)) // scan separators
        start++;
    while (*start && !strchr(separators, *start)) // scan word
    {
        word[i++] = *start;
        start++;
    }
    if (i > 0) // word was found
    {
        word[i] = '\0';
        word = (char*)realloc(word, i + 1);
        return word;
    }
    free(word);
    return NULL;
}
int main(void)
{
    char sentence[] = "   Why?! That's why.";
    char sep[] = "? !.";
    char *w = my_strtok(sentence, sep);
    while (w) { printf("\"%s\"\n", w); free(w); w = my_strtok(NULL, sep); }
    printf("last call -> NULL\n");
    char only[] = "?!.  "; w = my_strtok(only, sep); printf("only separators -> %s\n", w ? w : "NULL");
    char empty[] = ""; w = my_strtok(empty, sep); printf("empty sentence -> %s\n", w ? w : "NULL");
    char tail[] = "abc"; w = my_strtok(tail, sep); printf("\"%s\"", w); w = my_strtok(NULL, sep); printf(" then %s\n", w ? w : "NULL");
    return 0;
}
