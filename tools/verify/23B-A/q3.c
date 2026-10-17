#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char* nextWord(char* sentence, char* separators, char* word)
{
    int i = 0;
    while ( sentence[i] && !strchr(separators, sentence[i]) )
        word[i++] = sentence[i];
    word[i] = '\0';
    while (sentence[i] && strchr(separators, sentence[i]))
        i++;
    return sentence[i] ? sentence + i : NULL;
}
int breakSentence(char* sentence, char* separators, char* file_name)
{
    FILE* fptr = fopen(file_name, "w");
    char* word;
    int count = 0;
    if (!fptr) return -1;
    word = (char*)malloc(strlen(sentence) + 1);
    while ( (sentence = nextWord(sentence, separators, word)) != NULL )
    {
        fprintf(fptr, "%s\n", word);
        count++;
    }
    if (*word)
    {
        fprintf(fptr, "%s\n", word);
        count++;
    }
    free(word);
    fclose(fptr);
    return count;
}
int countWordOccur(char* sentence, char* separators, char* query)
{
    char* word;
    int count = 0;
    word = (char*)malloc(strlen(sentence) + 1);
    while ( (sentence = nextWord(sentence, separators, word)) != NULL )
        if (strcmp(word, query) == 0) count++;
    if (strcmp(word, query) == 0) count++;
    free(word);
    return count;
}
int main(void){
    char sep[]="? !.", s1[]="Why?! That's why.", w[64];
    char* r=nextWord(s1,sep,w); printf("word=[%s] rest=[%s]\n",w,r?r:"NULL");
    char s2[]="But why?! That's why."; int n=breakSentence(s2,sep,"t_out.txt"); printf("count=%d\n",n);
    FILE*f=fopen("t_out.txt","r"); char b[100]; while(fgets(b,100,f))fputs(b,stdout); fclose(f);
    char s3[]="But why?! That's why. And don't ask me why."; printf("occur=%d\n",countWordOccur(s3,sep,"why"));
    char s4[]="why"; printf("single=%d, empty=%d\n",countWordOccur(s4,sep,"why"), countWordOccur((char*)"",sep,"why"));
    char s5[]=""; printf("empty break=%d\n",breakSentence(s5,sep,"t_out.txt"));
    char s6[]="a!!b?"; printf("trailing sep break=%d\n",breakSentence(s6,sep,"t_out.txt"));
    return 0; }
