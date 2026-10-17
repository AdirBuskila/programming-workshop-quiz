#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int boggle(char* file_name, char* word)
{
    char c;
    FILE* fptr = fopen(file_name, "r");
    int w = 0;
    if (!fptr) exit(1);
    while ((c = fgetc(fptr)) != EOF)
        if (c == word[0]) { w++; break; }
    if (w == 0) { fclose(fptr); return 0; }
    while (word[w] != '\0')
    {
        if ((c = fgetc(fptr)) == word[w]) w++;
        else
        {
            if (c != EOF) fseek(fptr, -1, SEEK_CUR);
            if (ftell(fptr) - 2 < 0) { fclose(fptr); return 0; }
            fseek(fptr, -2, SEEK_CUR);
            if (fgetc(fptr) == word[w]) w++;
            else { fclose(fptr); return 0; }
        }
    }
    fclose(fptr);
    return 1;
}
static int ref(const char*b,const char*w){ int n=strlen(b),s; for(s=0;s<n;s++) if(b[s]==w[0]){ int cur=s,k=1; for(;w[k];k++){ if(cur+1<n&&b[cur+1]==w[k])cur++; else if(cur>0&&b[cur-1]==w[k])cur--; else break;} if(!w[k]) return 1;} return 0; }
int main(void){
    FILE*f=fopen("t_board.txt","w"); fputs("etybag",f); fclose(f);
    printf("bag=%d byte=%d baby=%d gat=%d\n",boggle("t_board.txt","bag"),boggle("t_board.txt","byte"),boggle("t_board.txt","baby"),boggle("t_board.txt","gat"));
    srand(3); int bad=0;
    for(int t=0;t<3000;t++){ char b[9]; int n=1+rand()%8; char pool[27]; for(int i=0;i<26;i++)pool[i]='a'+i; for(int i=0;i<n;i++){int j=i+rand()%(26-i);char x=pool[i];pool[i]=pool[j];pool[j]=x;b[i]=pool[i];} b[n]=0;
        char w[9]; int lw=1+rand()%6; for(int i=0;i<lw;i++) w[i]=(rand()%4==0)?'a'+rand()%26:b[rand()%n]; w[lw]=0;
        f=fopen("t_board.txt","w"); fputs(b,f); fclose(f); if(boggle("t_board.txt",w)!=ref(b,w)){bad++; if(bad<4)printf("mismatch board=%s word=%s got=%d\n",b,w,boggle("t_board.txt",w));} }
    printf("random mismatches=%d\n",bad); return 0; }
