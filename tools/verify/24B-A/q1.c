#include <stdio.h>
#include <stdlib.h>
typedef struct item { int digit; struct item* next; } Item;
int numListCmp(Item* L1, Item* L2)
{
    int diff = 0;
    while (!diff && L1 && L2)
    {
        if (L1->digit < L2->digit) diff = -1;
        else if (L1->digit > L2->digit) diff = 1;
        L1 = L1->next; L2 = L2->next;
    }
    if (!diff)
    {
        if (!L1 && L2) return -1;
        else if (L1 && !L2) return 1;
        return 0;
    }
    while (L1 && L2) { L1 = L1->next; L2 = L2->next; }
    if (!L1 && L2) return -1;
    else if (L1 && !L2) return 1;
    return diff;
}
int numListCmp_2(Item* L1, Item* L2)
{
    Item* ptr1 = L1, * ptr2 = L2;
    while (ptr1 && ptr2) { ptr1 = ptr1->next; ptr2 = ptr2->next; }
    if (!ptr1 && ptr2) return -1;
    else if (ptr1 && !ptr2) return 1;
    while (L1)
    {
        if (L1->digit < L2->digit) return -1;
        else if (L1->digit > L2->digit) return 1;
        L1 = L1->next; L2 = L2->next;
    }
    return 0;
}
static Item* mk(const char* s){ Item *h=NULL,**t=&h; for(;*s;s++){ *t=malloc(sizeof(Item)); (*t)->digit=*s-'0'; (*t)->next=NULL; t=&(*t)->next;} return h; }
static int ref(const char*a,const char*b){ while(*a=='0'&&a[1])a++; while(*b=='0'&&b[1])b++; /* strip: a list is M with msd first, no leading zero unless M=0 */
  int la=0,lb=0; while(a[la])la++; while(b[lb])lb++; if(la!=lb) return la<lb?-1:1; for(int i=0;i<la;i++) if(a[i]!=b[i]) return a[i]<b[i]?-1:1; return 0; }
int main(void){
    const char* ex[][2]={{"9999","10000"},{"53701","53687"},{"23469","23469"}}; int want[]={-1,1,0}, bad=0;
    for(int i=0;i<3;i++){ int r1=numListCmp(mk(ex[i][0]),mk(ex[i][1])), r2=numListCmp_2(mk(ex[i][0]),mk(ex[i][1])); printf("%d %d (want %d)\n",r1,r2,want[i]); if(r1!=want[i]||r2!=want[i])bad++; }
    srand(1);
    for(int t=0;t<20000;t++){ char a[8],b[8]; int la=1+rand()%5, lb=1+rand()%5; for(int i=0;i<la;i++)a[i]='0'+(i==0&&la>1?1+rand()%9:rand()%10); a[la]=0; for(int i=0;i<lb;i++)b[i]='0'+(i==0&&lb>1?1+rand()%9:rand()%10); b[lb]=0;
        int r=ref(a,b); if(numListCmp(mk(a),mk(b))!=r||numListCmp_2(mk(a),mk(b))!=r) bad++; }
    printf("bad=%d\n",bad); return bad!=0; }
