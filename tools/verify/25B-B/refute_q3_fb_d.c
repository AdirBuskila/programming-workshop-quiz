#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {char id[10];char name[31];double total;} clientData;
void text_to_binary(char* text_name, char* binary_name)
{
    clientData client;
    FILE* fin = fopen(text_name, "r");
    FILE* fout = fopen(binary_name, "w");
    if (!fin)  exit(1);
    if (!fout)  exit(1);
fscanf(fin, "%9s%30s%f", client.id, client.name, &client.total);
    while (!feof(fin))
    {
        fwrite(&client, sizeof(clientData), 1, fout);
        fscanf(fin, "%9s%30s%lf", client.id, client.name, &client.total);
    }
    fclose(fin);
    fclose(fout);
}
int main(int c,char**v){text_to_binary(v[1],v[2]);FILE*f=fopen(v[2],"rb");fseek(f,0,SEEK_END);long n=ftell(f);printf("size=%ld recs=%ld sizeof=%d|",n,n/(long)sizeof(clientData),(int)sizeof(clientData));
rewind(f);clientData r;while(fread(&r,sizeof r,1,f)==1)printf("[%s|%s|%.2f]",r.id,r.name,r.total);printf("\n");return 0;}
