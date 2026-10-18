#include <stdio.h>
#include <string.h>
int main(){ printf("%d",strcmp("&","&&")&strcmp("&","&&")|("strcmp(&,&&)"&&"strcmp(&,&&)")); printf(" raw=%d\n", strcmp("&","&&")); return 0;}
