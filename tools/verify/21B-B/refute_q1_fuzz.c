#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
void next_number(FILE* in, FILE* out, int* num, char* ch)
{ fprintf(out, "%d ", *num); if ((*ch = fgetc(in)) != '\n') fscanf(in, "%d", num); }
void rows_merge(FILE* in1, FILE* in2, FILE* out)
{ char ch1=0,ch2=0; int num1,num2; fscanf(in1,"%d",&num1); fscanf(in2,"%d",&num2);
  while (ch1!='\n'&&ch2!='\n') if (num1<num2) next_number(in1,out,&num1,&ch1); else next_number(in2,out,&num2,&ch2);
  while (ch1!='\n') next_number(in1,out,&num1,&ch1); while (ch2!='\n') next_number(in2,out,&num2,&ch2); fputc('\n',out);}
void copy_file(FILE* in, FILE* out){ int ch; while((ch=fgetc(in))!=EOF) fputc(ch,out);}
/* mode 0 official, 1 fixed, 2 !feof(in2), 3 feof(in1), 4 while(!feof(in1)) bounded */
void fm(const char*a,const char*b,const char*o,int mode){
  FILE*in1=fopen(a,"r"),*in2=fopen(b,"r"),*out=fopen(o,"w");
  while(fgetc(in1)!=EOF&&fgetc(in2)!=EOF){fseek(in1,-1,SEEK_CUR);fseek(in2,-1,SEEK_CUR);rows_merge(in1,in2,out);}
  if(mode==0){fseek(in1,-1,SEEK_CUR);fseek(in2,-1,SEEK_CUR);}
  else if(mode==1){if(!feof(in1))fseek(in1,-1,SEEK_CUR);}
  else if(mode==2){if(!feof(in2))fseek(in1,-1,SEEK_CUR);}
  else if(mode==3){if(feof(in1))fseek(in1,-1,SEEK_CUR);}
  else if(mode==4){int n=0;while(!feof(in1)&&n<5){fseek(in1,-1,SEEK_CUR);n++;} printf("while iterations(capped5)=%d\n",n);}
  copy_file(in1,out);copy_file(in2,out);fclose(in1);fclose(in2);fclose(out);}
static char buf[100000];
const char* rd(const char*n){FILE*f=fopen(n,"rb");size_t k=fread(buf,1,sizeof buf-1,f);buf[k]=0;fclose(f);return buf;}
void w(const char*n,const char*s){FILE*f=fopen(n,"wb");fputs(s,f);fclose(f);}
/* reference: line-wise merge */
void gen(char*dst,int*lines,int nl){ dst[0]=0; }
int cmpi(const void*x,const void*y){return *(int*)x-*(int*)y;}
int main(int argc,char**argv){
  _set_fmode(_O_BINARY);
  if(argc>1&&!strcmp(argv[1],"modes")){
    w("a.txt","3 8 12 16 20\n0 2 2 6\n9 10 10 11 19 26\n4 4 4 5\n"); w("b.txt","9 17\n2 6 7 11\n5 13 14 18\n");
    for(int m=0;m<=3;m++){fm("a.txt","b.txt","o.txt",m);printf("mode %d:\n[%s]\n",m,rd("o.txt"));}
    w("a.txt","1 5\n"); w("b.txt","2 3\n7 8\n9\n");
    fm("a.txt","b.txt","o.txt",0);printf("official in2 longer:[%s]\n",rd("o.txt"));
    fm("a.txt","b.txt","o.txt",1);printf("fixed in2 longer:[%s]\n",rd("o.txt"));
    w("a.txt","4 4 4 5\n7\n"); w("b.txt","1\n");
    fm("a.txt","b.txt","o.txt",4);
    return 0;}
  srand(12345); int bad=0,N=20000;
  for(int t=0;t<N;t++){
    int n=rand()%5,m=rand()%5; char A[4000]="",B[4000]="",W[4000]=""; int pa=0,pb=0,pw=0;
    int L=n>m?n:m;
    for(int i=0;i<L;i++){
      int xa[8],xb[8],na=0,nb=0;
      if(i<n){na=1+rand()%5;for(int k=0;k<na;k++)xa[k]=rand()%12;qsort(xa,na,4,cmpi);for(int k=0;k<na;k++)pa+=sprintf(A+pa,k?" %d":"%d",xa[k]);pa+=sprintf(A+pa,"\n");}
      if(i<m){nb=1+rand()%5;for(int k=0;k<nb;k++)xb[k]=rand()%12;qsort(xb,nb,4,cmpi);for(int k=0;k<nb;k++)pb+=sprintf(B+pb,k?" %d":"%d",xb[k]);pb+=sprintf(B+pb,"\n");}
      int xs[16],ns=0;for(int k=0;k<na;k++)xs[ns++]=xa[k];for(int k=0;k<nb;k++)xs[ns++]=xb[k];qsort(xs,ns,4,cmpi);
      for(int k=0;k<ns;k++)pw+=sprintf(W+pw,k?" %d":"%d",xs[k]);pw+=sprintf(W+pw,"\n");
    }
    w("a.txt",A);w("b.txt",B);fm("a.txt","b.txt","o.txt",1);
    /* strip the space before \n */
    char g[8000];int k=0;const char*s=rd("o.txt");for(;*s;s++){if(*s==' '&&s[1]=='\n')continue;g[k++]=*s;}g[k]=0;
    if(strcmp(g,W)){bad++;if(bad<4)printf("FAIL n=%d m=%d\nA=[%s]\nB=[%s]\nW=[%s]\nG=[%s]\n",n,m,A,B,W,g);}
  }
  printf("fuzz %d cases, mismatches %d\n",N,bad);
}
