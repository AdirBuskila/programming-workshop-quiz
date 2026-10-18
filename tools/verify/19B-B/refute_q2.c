#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct item{char*string;struct item*next;}Item;
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

int main(){Item*L=0;char*S0[]={"cat","ant","cat","dog","bee","bee","zed","a"};insert_strings_from_array_in_sort_list(S0,8,&L);for(;L;L=L->next)printf("%s ",L->string);printf("\n");return 0;}