#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
static int g;
static char sbuf[4] = {'a', 'b'};
int main(void)
{
    static int s;
    static char st[3] = {'x'};
    int *d = (int*)calloc(3, sizeof(int));
    unsigned u = 0x80000000u;
    printf("static int=%d global=%d last-of-partially-initialised static array=%d calloc=%d\n", s, g, sbuf[3], d[0]);
    printf("last element of static char array st[3]={'x'} = %d\n", st[2]);
    printf("unsigned 0x80000000 >> 4 = 0x%08x (zero-filled)\n", u >> 4);
    {
        long long diff = "abcd" - "xyz";   /* pointer difference, ptrdiff_t */
        (void)diff;
        printf("\"abcd\" - \"xyz\" compiles; type is ptrdiff_t: sizeof=%zu\n", sizeof("abcd" - "xyz"));
    }
    FILE *f = fopen("q4.bin","wb"); int v = 1000000; char ch[4] = {'a','b','c','d'}; fwrite(&v,sizeof v,1,f); fwrite(ch,1,4,f); fclose(f);
    f = fopen("q4.bin","rb"); unsigned char b[8]; fread(b,1,8,f); fclose(f);
    printf("binary file bytes:"); for(int i=0;i<8;i++) printf(" %02x",b[i]); printf("\n");
    return 0;
}
