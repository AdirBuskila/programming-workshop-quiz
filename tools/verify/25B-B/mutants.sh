#!/bin/sh
# Builds one-line mutants of the official solutions and runs them (values used in findbug explanations).
C="/c/Users/Adir/AppData/Local/Programs/Swift/Toolchains/6.1.0+Asserts/usr/bin/clang"
run() { # name file sed-expr
  sed "$3" "$2" > "mut_$1.c"; cmp -s "$2" "mut_$1.c" && echo "$1: SED DID NOT CHANGE" && return
  "$C" -w -o "mut_$1.exe" "mut_$1.c" && echo "-- $1" && "./mut_$1.exe"
}
run q1_loop q1.c 's/for (i = n - 1; i >= 0; i--)/for (i = n - 1; i > 0; i--)/'
run q2_col q2.c 's/for (j = i + 1; j < n + 1; j++)/for (j = i + 1; j < n; j++)/'
run q3_size q3.c 's/fwrite(&client, sizeof(clientData), 1, fout)/fwrite(\&client, sizeof(client.id), 1, fout)/'
# q3 mutant: raw byte size of the output file (dump() in q3.c reads 56-byte records, so it shows 0)
"$C" -w -o fsize.exe fsize.c
./fsize.exe t_nl.bin
