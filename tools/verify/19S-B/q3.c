#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* official solution, verbatim */
void cyclic_shift_of_string(char *str)
{
      int len = strlen(str), i, j, k;
      char *temp;
      for (i=len-1; i>=0 && str[i]!=' '; i--); //search of beginning last word
      if (i<0) // //only one word in str
            return;
      temp = malloc(len+1);
      for (j=0, k=i+1; k<len; j++, k++)
            temp[j] = str[k]; //copy last word to auxiliary string
      for (; str[i]==' '; j++, i--) //search of end of penultimate word
            temp[j] = ' ';
      for (k=0; k<=i; j++, k++)
            temp[j] = str[k]; //copy from first to penultimate word
      temp[j] = '\0';
      strcpy(str, temp);
      free(temp);
}
static int t(const char *in, const char *want){ char b[100]; strcpy(b,in); cyclic_shift_of_string(b); printf("'%s' -> '%s'\n",in,b); return strcmp(b,want)!=0; }
int main(void)
{
    int bad=0;
    bad|=t("one two three four","four one two three");
    bad|=t("one  two   three four","four one  two   three");
    bad|=t("one   two","two   one");
    bad|=t("alone","alone");
    bad|=t("a b","b a");
    printf(bad?"FAIL\n":"OK\n");
    return bad;
}
