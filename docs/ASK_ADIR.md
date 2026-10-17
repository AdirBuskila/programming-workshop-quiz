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

### 21B-B Q1 - official filesMerge fails the exam's own example
- Path: official solution of sitting 21B-B (tools/verify/21B-B/q1.c reproduces it)
- Page: 2-3
- Question: the official filesMerge merges the common rows correctly, but when the two files differ in length the fseek(-1) on the unread or EOF file plus copy_file adds a stray newline. The exam example (4 lines vs 3) ends with an extra blank line, and with infile_2 longer the blank lines land between rows. Held per GATE1 (a solution that fails its tests).
- Needed: decide whether to ship the official code as is with the transcriber note (current text), or add a corrected variant.
- Status: hold

## Resolved
