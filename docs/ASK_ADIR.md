# ASK_ADIR - programming-workshop

Open questions for Adir. One entry per item; the orchestrator moves it to Resolved when answered.

## Open

<!-- Entry format:
### <exam code> Q<number> - <short title>
- Path: <absolute file path>
- Page: <page number>
- Question: <what is unclear or missing>
- Needed: <what Adir must provide or decide>
- Status: hold
-->

### 25B-B Q3 - official solution loses the last record without a trailing newline
- Path: official solution of sitting 25B-B (tools/verify/25B-B/q3.c reproduces it)
- Page: 11
- Question: the official text_to_binary compiles and handles the exam example (file ending in a newline), but with no newline after the last line the feof loop drops the last record; the file is also opened with "w", not "wb". Left as official, flagged in the solution text.
- Needed: confirm whether to keep the official code as is (current), or add a corrected variant.
- Status: noted, not held

## Resolved

### 21B-B Q1 - official filesMerge fails the exam's own example
- Path: official solution of sitting 21B-B (tools/verify/21B-B/arb_q1.c)
- Page: 2-3
- Ruling (arbiter, standing ruling "official answer ... fails a check"): shipped with a minimal fix: after the merge loop only in1 is moved back, and only if not at EOF (`if (!feof(in1)) fseek(in1, -1, SEEK_CUR);`), replacing the two unconditional fseeks. Labelled "הפתרון הרשמי עם תיקון", solutionSource solved, official false. The fix passes the example plus longer-infile_2, equal-length and empty-file cases with clang.
- Status: resolved, un-held, steps ai-draft (refute pending)
