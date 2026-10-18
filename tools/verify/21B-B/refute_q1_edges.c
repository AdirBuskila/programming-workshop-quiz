#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <string.h>
void next_number(FILE* in, FILE* out, int* num, char* ch){ fprintf(out,"%d ",*num); if((*ch=fgetc(in))!='\n') fscanf(in,"%d",num);}
void rows_merge(FILE* in1, FILE* in2, FILE* out)
{ char ch1=0,ch2=0; int num1,num2; fscanf(in1,"%d",&num1); fscanf(in2,"%d",&num2);
  int g=0; while (ch1!='\n'&&ch2!='\n'){ if(++g>1000){puts("HANG(loop)");exit(3);} if (num1<num2) next_number(in1,out,&num1,&ch1); else next_number(in2,out,&num2,&ch2);}
  while (ch1!='\n'){ if(++g>1000){puts("HANG");exit(3);} next_number(in1,out,&num1,&ch1);} while (ch2!='\n'){ if(++g>1000){puts("HANG");exit(3);} next_number(in2,out,&num2,&ch2);} fputc('\n',out);}
void copy_file(FILE* in, FILE* out){ int ch; while((ch=fgetc(in))!=EOF) fputc(ch,out);}
int main(int c,char**v){
  if(!strcmp(v[1],"bin")) _set_fmode(_O_BINARY);
  FILE*in1=fopen(v[2],"r"),*in2=fopen(v[3],"r"),*out=fopen("o.txt","w");
  while(fgetc(in1)!=EOF&&fgetc(in2)!=EOF){int r1=fseek(in1,-1,SEEK_CUR),r2=fseek(in2,-1,SEEK_CUR);if(r1||r2)printf("seek fail %d %d\n",r1,r2);rows_merge(in1,in2,out);}
  if(!feof(in1))printf("post-seek rc=%d\n",fseek(in1,-1,SEEK_CUR));
  copy_file(in1,out);copy_file(in2,out);fclose(in1);fclose(in2);fclose(out);
  FILE*f=fopen("o.txt","rb");int ch;printf("OUT:[");while((ch=fgetc(f))!=EOF)putchar(ch);puts("]");}
