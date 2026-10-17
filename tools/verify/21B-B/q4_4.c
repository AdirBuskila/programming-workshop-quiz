#include <stdio.h>
int main(void) {
    int a = 0x12345678;
    FILE *fptr2 = fopen("q44.bin", "wb");
    fwrite(&a, sizeof(a), 1, fptr2);
    fclose(fptr2);
    int b = 0;
    FILE *fptr1 = fopen("q44.bin", "rb");
    fread(&b, sizeof(b), 1, fptr1);
    fclose(fptr1);
    printf("round trip ok: %d\n", a == b);
    return 0;
}
