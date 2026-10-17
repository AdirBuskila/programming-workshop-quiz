#include <stdio.h>
#include <stdlib.h>
/* official solutions, verbatim */
int check_controls_in_file_rows (char *fileName)
{
      int sum=0, control_num;
      char c, control_char;
      FILE *fptr = fopen(fileName, "r");
      if( !fptr )
            return -1;
      while ( (c = fgetc(fptr)) != EOF )
      {
            if (c != ' ')
                  sum += c;
            else
            {
                  fscanf(fptr, "%d%c", &control_num, &control_char);
                  if (control_char == '\n')
      //real control char is digit that was interpreted as last digit of control number
                  {
                         control_char = control_num%10 + '0';
                         control_num /= 10;
                  }
                  else
                         fgetc(fptr); //input '/n'
                  if (control_num != sum || control_char != sum%128)
                  {
                         fclose(fptr);
                         return 0;
                  }
                  else
                        sum = 0;
            } //else
      } //while
      fclose(fptr);
      return 1;
}
int check_controls_in_file_rows_2 (char *fileName)
{
      int sum=0, control_sum;
      char c, last_char;
      FILE *fptr = fopen(fileName, "r");
      if( !fptr )
            return -1;
      while ( (c = fgetc(fptr)) != EOF )
      {
            if (c != ' ')
                  sum += c;
            else
            {
                  control_sum = fgetc(fptr)-'0'; //first digit
                  last_char = fgetc(fptr);
                  while ( (c = fgetc(fptr)) != '\n' )
                  {
                        //last_char is current digit of control_sum
                        control_sum = control_sum*10 + last_char-'0';
                        last_char = c;
                  }
                  if (control_sum != sum || last_char != sum%128)
                  {
                        fclose(fptr);
                        return 0;
                  }
                  else
                        sum = 0;
            }
      }
      fclose(fptr);
      return 1;
}
static void mk(const char *name, const char *content){ FILE*f=fopen(name,"wb"); fputs(content,f); fclose(f); }
static int bad=0;
static void chk(const char *label, const char *content, int want)
{
    mk("c.txt", content);
    int a = check_controls_in_file_rows("c.txt"), b = check_controls_in_file_rows_2("c.txt");
    printf("%-34s v1=%2d v2=%2d want=%2d %s\n", label, a, b, want, (a==want && b==want)?"ok":"MISMATCH");
    if (!(a==want && b==want)) bad=1;
}
int main(void)
{
    chk("exam example (valid)", "abc 294&\r\n3+2+1=6 351_\r\nA 65A\r\n", 1);
    chk("wrong number", "abc 295&\r\n", 0);
    chk("wrong char", "abc 294%\r\n", 0);
    chk("wrong number, 2nd row", "abc 294&\r\nA 66A\r\n", 0);
    /* row "a": sum=97, 97%128=97='a' -> "a 97a" */
    chk("one char row", "a 97a\r\n", 1);
    /* control char is a digit: row "0" sum=48 -> "0 480" */
    chk("control char is a digit", "0 480\r\n", 1);
    printf(bad ? "SOME MISMATCH\n" : "ALL ok\n");
    return 0;
}
