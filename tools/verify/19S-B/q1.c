#include <stdio.h>
#include <stdlib.h>
/* official solution, verbatim */
void copy_row(FILE *in, FILE *out, int start_row, int *rows)
{
      char c;
      fseek(in, start_row, SEEK_SET); //to the beginning of row
      while ( (c = fgetc(in)) != ' ' ) //copy chars till space
            fputc(c, out);
      fputc('\n', out);
      (*rows)++;
}

void copy_true_false_file_rows (char *infile, char *outfile_true,
      char *outfile_false, int *true_rows, int *false_rows)
{
      int sum=0, control_num, start_row=0, end_row;
      char c;
      FILE *in = fopen(infile, "r"),
            *out_true = fopen(outfile_true, "w"),
            *out_false = fopen(outfile_false, "w");
      if( !in || !out_true || !out_false )
            exit(1);
      *true_rows = *false_rows = 0;
      while ( (c = fgetc(in)) != EOF )
      {
            if (c != ' ')
                  sum += c;
            else //start of control number
            {
                  fscanf(in, "%d", &control_num);
                  end_row = ftell(in); //save end of row
                  if (control_num == sum)
                        copy_row(in, out_true, start_row, true_rows);
                  else
                        copy_row(in, out_false, start_row, false_rows);
                  sum = 0;
                  start_row = end_row + 2; //start of next row ('\' and 'n' are two positions)
                  fseek(in, start_row, SEEK_SET);//to the beginning of next row
            }
      }
      fclose(in);
      fclose(out_true);
      fclose(out_false);
}
static void show(const char *n){ FILE*f=fopen(n,"r"); int c; printf("[%s]\n",n); while((c=fgetc(f))!=EOF) putchar(c); fclose(f);}
int main(void)
{
    /* Windows text file: CRLF line ends, as the official solution assumes (+2) */
    FILE *f = fopen("in.txt","wb");
    fputs("abc 294\r\n3+2+1=6 352\r\nA 65\r\n", f); fclose(f);
    int t, fl;
    copy_true_false_file_rows("in.txt","t.txt","f.txt",&t,&fl);
    printf("true_rows=%d false_rows=%d\n", t, fl);
    show("t.txt"); show("f.txt");
    return !(t==2 && fl==1);
}
