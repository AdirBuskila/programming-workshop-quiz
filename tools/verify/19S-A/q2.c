#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct item { char *string; struct item *next; } Item;
/* official solution, verbatim */
Item *array_of_strings_to_list (char **S, int n)
{
      Item *lst, *curr_ptr;
      int i, j;
      lst = (Item *)malloc(sizeof(Item)); //dummy
      curr_ptr = lst;
      for (j=0; j<n; j++)
      {
            curr_ptr->next = (Item *)malloc(sizeof(Item));
            curr_ptr = curr_ptr->next;
            //initial allocation - for all the string with '\0'
            curr_ptr->string = (char *)malloc(strlen(S[j])+1);
            for (i=0; S[j][i]!='\0' && S[j][i]!=' '; i++)
                  curr_ptr->string[i] = S[j][i];
            curr_ptr->string[i] = '\0';
            //reallocation for the first word in a string with '\0'
            curr_ptr->string = (char *)realloc(curr_ptr->string, i+1);
      }
      curr_ptr->next = NULL;
      /* deletion of dummy */
      curr_ptr = lst;
      lst = lst->next;
      free (curr_ptr);
      return lst;
}
int main(void)
{
    char *S[4] = {"Moshe lives in Tel Aviv", "Irit was the first", "Avi has two children", "Dan"};
    const char *want[4] = {"Moshe","Irit","Avi","Dan"};
    Item *L = array_of_strings_to_list(S, 4), *p = L; int i, bad=0;
    for (i=0;i<4;i++,p=p->next){ printf("[%s]\n", p->string); if(strcmp(p->string,want[i])) bad=1; }
    if (p) bad=1;
    printf(bad?"FAIL\n":"OK\n");
    return bad;
}
