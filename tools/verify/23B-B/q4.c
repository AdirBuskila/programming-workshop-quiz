#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <malloc.h>

#define SIZE 4

struct TsT {
	int val1;
	char val2[SIZE];
	char* val3;
};

void func1(struct TsT myTsT) {
	myTsT.val3[1] = 'Y';
	myTsT.val2[1] = 'Y';
	myTsT.val1 = 444;
};

void func2(struct TsT* myTsT) {
	myTsT->val3[1] = 'X';
	myTsT->val2[1] = 'X';
	myTsT->val1 = 222;
};

void main() {
	struct TsT p1, p2;

	p1.val3 = (char*)malloc(4);
	strcpy(p1.val3, "aaa");
	p1.val1 = 20;
	strcpy(p1.val2, "bbb");

	p2 = p1;
	printf("p1 Print1: %d, %s, %s \n", p1.val1, p1.val2, p1.val3);
	printf("p2 Print1: %d, %s, %s \n", p2.val1, p2.val2, p2.val3);

	p2.val2[0] = 'Z';
	p2.val3[0] = 'Z';
	printf("p1 Print2: %d, %s, %s \n", p1.val1, p1.val2, p1.val3);
	printf("p2 Print2: %d, %s, %s \n", p2.val1, p2.val2, p2.val3);

	func1(p1);
	func2(&p2);
	printf("p1 Print3: %d, %s, %s \n", p1.val1, p1.val2, p1.val3);
	printf("p2 Print3: %d, %s, %s \n", p2.val1, p2.val2, p2.val3);
}
