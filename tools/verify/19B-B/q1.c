#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* official solution, verbatim */
void add_controls_in_file_rows (char *infile, char *outfile)
{
      int sum=0;
      char c;
      FILE *in = fopen(infile, "r"),
             *out = fopen(outfile, "w");
      if( !in || !out )
            exit(1);
      while ( (c = fgetc(in)) != EOF )
            if (c != '\n')
            {
                  fputc(c, out);
                  sum += c;
            }
            else
            {
                  fprintf(out, " %d%c\n", sum, sum%128);
                  sum = 0;
            }
      fclose(in);
      fclose(out);
}
int main(void)
{
    FILE *f = fopen("in.txt","wb"); fputs("abc\r\n3+2+1=6\r\nA\r\n", f); fclose(f);
    add_controls_in_file_rows("in.txt","out.txt");
    f = fopen("out.txt","rb"); int c, k=0; char buf[200];
    while((c=fgetc(f))!=EOF) buf[k++]=c;
    buf[k]=0; fclose(f);
    const char *want = "abc 294&\r\n3+2+1=6 351_\r\nA 65A\r\n";   /* text-mode output on Windows = CRLF */
    printf("%s", buf);
    int ok = strcmp(buf,want)==0; printf(ok?"OK\n":"FAIL\n"); return !ok;
}
