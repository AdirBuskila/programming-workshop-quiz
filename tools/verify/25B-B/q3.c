#include <stdio.h>
#include <stdlib.h>
typedef struct { char id[10]; char name[31]; double total; } clientData;
void text_to_binary(char* text_name, char* binary_name)
{
	clientData client;
	FILE* fin = fopen(text_name, "r");
	FILE* fout = fopen(binary_name, "w");
	if (!fin)  exit(1);
	if (!fout)  exit(1);
	fscanf(fin, "%9s%30s%lf", client.id, client.name, &client.total);
	while (!feof(fin))
	{
		fwrite(&client, sizeof(clientData), 1, fout);
		fscanf(fin, "%9s%30s%lf", client.id, client.name, &client.total);
	}
	fclose(fin);
	fclose(fout);
}
static void dump(const char *bin)
{
	FILE *f = fopen(bin, "rb"); clientData c; int k = 0;
	while (fread(&c, sizeof c, 1, f) == 1) { printf("[%s|%s|%.2f]", c.id, c.name, c.total); k++; }
	printf(" records=%d size=%ld\n", k, (long)(k*sizeof c)); fclose(f);
}
int main(void)
{
	const char *txt = "06842151        Moshe    71.25\n330578795   Benjamin 1755.65\n20051546        Dina   560.10";
	FILE *f = fopen("t_nonl.txt", "w"); fputs(txt, f); fclose(f);
	f = fopen("t_nl.txt", "w"); fputs(txt, f); fputs("\n", f); fclose(f);
	text_to_binary("t_nl.txt", "t_nl.bin"); printf("trailing newline: "); dump("t_nl.bin");
	text_to_binary("t_nonl.txt", "t_nonl.bin"); printf("no trailing newline: "); dump("t_nonl.bin");
	return 0;
}
