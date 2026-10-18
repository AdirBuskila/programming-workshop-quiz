#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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

void w(const char*t){FILE*f=fopen("a1in.txt","wb");fputs(t,f);fclose(f);}
int main(){
 const char*T[]={"abc 294&\n3+2+1=6 351_\nA 65A\n","abc 294&\nA 65B\n","ab 195C\n","0 480\n","AI 138\n\n","ab 195\x01\n","\n"};
 for(int i=0;i<7;i++){w(T[i]);printf("case%d v1=%d v2=%d\n",i,check_controls_in_file_rows("a1in.txt"),check_controls_in_file_rows_2("a1in.txt"));}
 /* empty orig line: ' 0\0\n' */
 FILE*f=fopen("a1in.txt","wb");fwrite("x 120x\n y\n",1,0,f);fclose(f);
 return 0;}