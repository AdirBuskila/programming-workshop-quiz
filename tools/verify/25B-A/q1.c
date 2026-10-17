#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct node { char value; struct node* next; } node;
void deleteHead(node** head) { node* temp = *head; *head = temp->next; free(temp); }
void deleteNext(node* pos) { node* temp = pos->next; pos->next = temp->next; free(temp); }
void removeExtraSpaces(node** head)
{
    node* curr, *prev;
    while (*head && (*head)->value == ' ')
        deleteHead(head);
    if (*head == NULL) return;
    prev = *head;
    curr = prev->next;
    while (curr)
    {
        if (curr->value == ' ' && (!curr->next || curr->next->value == ' '))
            deleteNext(prev);
        else
            prev = curr;
        curr = prev->next;
    }
}
static node* mk(const char* s){ node *h=NULL,**t=&h; for(;*s;s++){ *t=malloc(sizeof(node)); (*t)->value=*s; (*t)->next=NULL; t=&(*t)->next;} return h; }
static void str(node* h, char* o){ while(h){*o++=h->value;h=h->next;} *o=0; }
/* reference: collapse spaces, strip leading/trailing */
static void ref(const char* in, char* out){
    int n=0, i, sp=0; char buf[256]; 
    for(i=0;in[i];i++){ if(in[i]==' '){ if(n>0) sp=1; } else { if(sp) buf[n++]=' '; sp=0; buf[n++]=in[i]; } }
    buf[n]=0; strcpy(out,buf);
}
int main(void){
    const char* t[]={"  No  way! ","    ","","x","x ","  x","a b","a   b   c  ","   a b   ",NULL};
    int i, bad=0;
    for(i=0;t[i];i++){ node* h=mk(t[i]); char o[256], r[256]; removeExtraSpaces(&h); str(h,o); ref(t[i],r);
        printf("[%s] -> [%s]\n", t[i], o); if(strcmp(o,r)) {bad++; printf("MISMATCH want [%s]\n", r);} }
    /* exhaustive over strings of {a,' '} up to len 8 */
    for(int len=0;len<=8;len++) for(int m=0;m<(1<<len);m++){ char s[16]; for(int k=0;k<len;k++) s[k]=(m>>k&1)?' ':'a'; s[len]=0;
        node* h=mk(s); char o[64],r[64]; removeExtraSpaces(&h); str(h,o); ref(s,r); if(strcmp(o,r)) bad++; }
    printf("bad=%d\n",bad); return bad!=0;
}
