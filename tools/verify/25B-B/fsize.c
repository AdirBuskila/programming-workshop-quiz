#include <stdio.h>
int main(int argc, char **argv)
{
	FILE *f = fopen(argv[1], "rb"); fseek(f, 0, SEEK_END);
	printf("%s bytes=%ld\n", argv[1], ftell(f)); return 0;
}
