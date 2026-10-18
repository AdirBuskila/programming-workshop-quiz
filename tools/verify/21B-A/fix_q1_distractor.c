#include <stdio.h>
#include <string.h>
typedef struct{char first_name[30],last_name[30];}name;
#define F(COND) int f##COND(name*a,int n){int i;for(i=1;i<n;i++)if(strcmp(a[i].first_name,a[i-1].first_name)<0){for(i=1;i<n;i++)if(COND)return 0;return 2;}return 1;}
#define C0 (strcmp(a[i].last_name,a[i-1].last_name)<0)
#define C1 (strcmp(a[i-1].last_name,a[i].last_name)<0)
#define C2 (strcmp(a[i].last_name,a[i].first_name)<0)
int g0(name*a,int n){int i;for(i=1;i<n;i++)if(strcmp(a[i].first_name,a[i-1].first_name)<0){for(i=1;i<n;i++)if C0 return 0;return 2;}return 1;}
int g1(name*a,int n){int i;for(i=1;i<n;i++)if(strcmp(a[i].first_name,a[i-1].first_name)<0){for(i=1;i<n;i++)if C1 return 0;return 2;}return 1;}
int main(){name a[7]={{"Mike","Asher"},{"David","Bern"},{"Joseph","Borgman"},{"Alon","Kapulski"},{"Ilan","Mizrachi"},{"Oren","Nodel"},{"Abraham","Rosen"}};
printf("%d %d\n",g0(a,7),g1(a,7));}
