# Learn coverage: programming-workshop

Built from the 126 banked questions (all 16 sittings, 19B-A to 25B-B). The QA re-pass of 2026-10-18 added the rows marked (QA). Briefs are in `docs/briefs/` (15 files, 14 topic briefs and one cheat sheet). Every C snippet in the briefs was compiled and, where it has `main`, run with clang; the claimed outputs match.

| Concept | Brief section | Example question ids |
|---|---|---|
| sizeof of string literal / pointer, `'\0'` inside a literal | 01 traps, 14 trap 1 | 21B-A-Q5, 25B-A-Q5a |
| String literal as an address (`"puts"+1`), `strlen` vs `sizeof` | 01 | 23B-A-Q6 |
| Operator precedence (`=` vs `!=`, `&` vs `==`), `&&` on addresses, `strcmp` sign | 01 | 22B-B-Q5, 25B-A-Q6 |
| ASCII arithmetic, integer division of chars | 01, 14 trap 12 | 25B-B-Q6, 23B-B-Q5a |
| char array vs `char*`, literal immutability, `==` on strings | 02 | 22B-A-Q4d, 22B-B-Q4d, 25B-B-Q5b |
| `string.h` / `ctype.h`, letter counters, reverse, halves of a string | 02 | 21B-A-Q1, 22B-B-Q1, 24B-B-Q3 |
| Dynamic string build (`calloc`, `strcat`, `+1`) | 02, 06 | 22B-A-Q1 |
| Word splitting by separator set without `strtok`, `strchr` on `'\0'` | 02 | 23B-A-Q3a, 23B-A-Q3c, 23B-B-Q3 |
| Static 2D array, `*a[i]`, `*(*(a+i)+i)`, `A[][N]` | 03 | 22B-B-Q4b, 25B-A-Q2 |
| Diagonal / triangle index ranges | 03, 07 | 25B-A-Q2, 25B-B-Q2 |
| Sorted row / column check | 03 | 23B-A-Q2 |
| Legal pointer operations, `p-q`, `p+q` | 04 | 23B-A-Q5b |
| Reading declarations, pointer to function, `f` vs `(*f)` | 04 | 22B-A-Q4b, 23B-B-Q5b, 25B-B-Q4 |
| Aliasing trace (`&x,&x`), by-value copy | 04 | 24B-A-Q4 |
| By reference: `T**`, `T***`, `(*p)[i]`, `Item**` head | 05 | 25B-A-Q1, 25B-A-Q2, 23B-A-Q2, 21B-A-Q3, 24B-B-Q1 |
| malloc/calloc/realloc/free semantics, `malloc(0)`, free of static | 06 | 22B-A-Q4c, 24B-A-Q5a, 24B-B-Q5b |
| Count-then-allocate, trim with realloc, free order | 06 | 22B-B-Q2, 24B-A-Q2 |
| Jagged / 2D dynamic arrays, frame, triangles back to matrix, array of struct | 07 | 22B-B-Q2, 23B-A-Q2, 24B-A-Q2, 24B-B-Q2, 25B-A-Q2, 25B-B-Q2 |
| Struct copy: array copied, pointer shared; by value vs address | 08 | 23B-B-Q4, 21B-A-Q4c |
| Union shares memory | 08 | 25B-A-Q4 |
| Struct declaration syntax; self-containing struct vs pointer | 08 | 24B-B-Q5a, 25B-B-Q5a |
| fopen modes, text read idioms, `feof` trap, `fgets`/`fgetc` traces, puts vs fputs | 09, 14 traps 2-4 | 22B-A-Q4a, 22B-B-Q4c, 23B-A-Q5a, 24B-A-Q6, 25B-A-Q6 |
| Binary records `fread`/`fwrite`, two-pass fill, text to binary | 09 | 22B-A-Q3, 23B-B-Q2, 22B-B-Q3, 25B-B-Q3 |
| `fseek`/`ftell`/`rewind`, row-wise decode, whole-word count | 09 | 21B-A-Q3, 24B-A-Q3, 25B-A-Q3, 23B-A-Q3b |
| Singly linked list ops, delete, dummy node, tail, free | 10 | 25B-A-Q1, 25B-B-Q1 |
| Circular lists (traverse, merge) | 10, 11 | 21B-A-Q2, 23B-B-Q1 |
| Digit lists (compare, add in place) | 11 | 24B-A-Q1, 22B-A-Q2 |
| Aux array accumulation (polynomial), array of lists | 11 | 23B-A-Q1, 24B-B-Q1 |
| Scope shadowing, static local, return of `&static`, reserved words, defaults | 12 | 23B-A-Q4, 24B-B-Q4, 25B-B-Q4, 21B-A-Q4d, 22B-B-Q4a, 21B-A-Q4a |
| Bit operators, shifts, XOR identities, `(long long)` shift, truncation | 13 | 21B-A-Q4b, 22B-A-Q5, 23B-B-Q6, 24B-A-Q5b, 24B-B-Q6, 25B-A-Q5b |
| MCQ strategy, justification, "none correct" options | 14 | 21B-A-Q4a, 22B-B-Q4c, 25B-B-Q5a |
| (QA) `printf` return value, escape sequences and `strlen` of literals | 01 | 21B-B-Q5, 20B-B-Q5 |
| (QA) Address cast to `long long` and back; which pointer types exist (no pointer to a bit) | 04 | 19S-A-Q5, 20B-B-Q5, 19B-B-Q4a |
| (QA) Legal and undefined struct operations, struct size >= sum of fields, struct vs union | 08 | 19S-A-Q4a, 19B-B-Q4b, 19S-B-Q4a |
| (QA) Binary file in a text editor, `fread`/`fwrite` copy between binary files | 09 | 20B-B-Q4d, 21B-B-Q4d |
| (QA) `const` on pointer-to-pointer declarations, illegal const operations, preprocessor directives | 12 | 19B-A-Q4d, 19S-B-Q4d, 20B-A-Q4c, 19S-A-Q4c, 19S-A-Q4d |

## Gaps
- All 16 sittings are now in the bank. The QA rows above close the concepts no brief taught. Left untaught on purpose: the logic item 20B-A-Q4a (which statement is not a generalisation) and the compiler-message wording of 20B-A-Q4f (compilers differ).
- Topics `c_basics_output` and `pointer_to_pointer` have no questions tagged in the bank; they are taught as foundations for others.
- Not covered: the 2019-2022 style MCQ items that are not yet transcribed, and the "american questions" scan (needs OCR).
- Sources: the image-only student summary PDF was not OCR'd; the briefs are written from the official exam solutions and standard C. Adir's C++/OOP notes and exam collection were deliberately not used.
- `25B-A-Q5a` key assumes 4-byte pointers (888 on a 64-bit compiler); brief 14 tells the student to state the assumption. `22B-B-Q5` assumes `strcmp` returns -1.
