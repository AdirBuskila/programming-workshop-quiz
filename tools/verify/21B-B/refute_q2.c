#include <stdio.h>
#include <string.h>
#include <stdlib.h>
typedef struct { char last_name[30], first_name[30]; unsigned id; } person;
#ifndef LASTCMP
#define LASTCMP <0
#endif
#ifndef IDCMP
#define IDCMP <
#endif
int ordered_person_array(person* person_arr, int n)
{
    int i, cmp;
    for (i = 1; i < n; i++)
        if ( (cmp = strcmp(person_arr[i].last_name, person_arr[i - 1].last_name)) LASTCMP )
            return i*0+ (printf("viol at %d\n",i),0);
        else
            if (cmp == 0)
                if ((cmp=strcmp(person_arr[i].first_name, person_arr[i-1].first_name))<0)
                    return (printf("viol at %d\n",i),0);
                else
                    if (cmp == 0)
                        if (person_arr[i].id IDCMP person_arr[i - 1].id)
                            return (printf("viol at %d\n",i),0);
    return 1;
}
int main(){
 person a[10]={{"Asher","Mike",231567809},{"Bern","David",216578900},{"Borgman","Joseph",354678903},{"Cohen","Abraham",224567821},{"Cohen","Den",206666431},{"Levi","Ilan",290876441},{"Levi","Omri",245689432},{"Levi","Omri",245689436},{"Smith","Jack",345389010},{"Smith","John",311232111}};
 printf("ex1 %d\n",ordered_person_array(a,10));
 person b[10]; memcpy(b,a,sizeof a); b[6].id=245689436;b[7].id=245689432;
 printf("ex2 %d\n",ordered_person_array(b,10));
 person c[2]={{"A","B",5},{"A","B",5}}; printf("dup %d\n",ordered_person_array(c,2));
 person d[2]={{"A","B",5},{"A","C",1}}; printf("firstdiff %d\n",ordered_person_array(d,2));
 person e[2]={{"A","C",5},{"A","B",9}}; printf("firstbad %d\n",ordered_person_array(e,2));
 printf("n0 %d n1 %d\n",ordered_person_array(a,0),ordered_person_array(a,1));
}
