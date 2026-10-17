#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct item { char *string; struct item *next; } Item;
/* official solution, verbatim */
void insert_string_in_sort_list (char* str, Item **plist)
{
    Item *curr_point = *plist, *prev_point, *temp;

      //search place for insert into sorting list
      while ( curr_point && strcmp(str, curr_point->string)==1 )
      {
            prev_point = curr_point;
            curr_point = curr_point->next;
      }

      //check whether string is already in list
      if ( curr_point && strcmp(str, curr_point->string)==0 )
            return;

      //allocation place for new item and string
      temp = (Item *)malloc(sizeof(Item));
      temp->string = (char *)malloc(strlen(str)+1);
      strcpy(temp->string, str);

      if (curr_point != *plist) // inserting in the middle or in the end
      {
            temp->next = curr_point;
            prev_point->next = temp;
      }
      else  // inserting before first item
      {
            temp->next = *plist;
            *plist = temp;
      }
}

void insert_strings_from_array_in_sort_list (char** str, int n, Item
**plist)
{
      int i;
      for (i=0; i<n; i++)
            insert_string_in_sort_list (str[i], plist);
}
static Item *mk(const char *s, Item *n){ Item *p=malloc(sizeof(Item)); p->string=_strdup(s); p->next=n; return p; }
int main(void)
{
    printf("strcmp(b,a)=%d strcmp(zz,a)=%d\n", strcmp("b","a"), strcmp("zz","a"));
    Item *L = mk("Avi", mk("Irit", mk("Moshe", NULL)));
    char *S[4] = {"Mike","Avi","Irit","Arthur"};
    insert_strings_from_array_in_sort_list(S, 4, &L);
    const char *want[] = {"Arthur","Avi","Irit","Mike","Moshe"}; int i=0, bad=0;
    for (Item *p=L;p;p=p->next,i++){ printf("%s ",p->string); if(i>=5||strcmp(p->string,want[i])) bad=1; }
    if (i!=5) bad=1;
    printf("\n%s\n", bad?"FAIL":"OK");
    return bad;
}
