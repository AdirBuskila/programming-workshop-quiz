# STATUS - programming-workshop

Resume here: phase 7 - ship (awaiting Adir). QA done 2026-10-18; open items are in docs/ASK_ADIR.md and the QA notes below.
Opus sessions: 0 of 2
Engine: open   Format: mixed (code + American)   Cutoff: 2019 (sittings 19B-A to 25B-B)

Triage material (private, names students, never copied into this repo): C:\Users\Adir\Desktop\Coding\Dev\course-factory\courses\programming-workshop\format_triage.md

Gates 1, 2 and 7 always stop for Adir. A tick below means an artifact in this repo or the factory backs it (named in brackets); ticks with no artifact were left empty.

- [x] Phase 0 - intake
  - [x] registry entry exists [course-factory/courses.json, slug programming-workshop]
  - [x] source folder exists and is non-empty [course.config.json sourceFolder]
- [ ] Phase 1 - triage  (GATE 1: Adir approves format, cutoff, topics)
  - [x] triager run per subfolder [course-factory/courses/programming-workshop/triage/]
  - [x] format_triage.md merged [course-factory/courses/programming-workshop/format_triage.md, GATE1.md]
  - [ ] Adir approved (no recorded approval artifact; registry status is still "triaged")
  - [x] config.overlay.json written, app repo scaffolded [course-factory/.../config.overlay.json, this repo]
- [ ] Phase 2 - flagship  (GATE 2: Adir tries it in the browser)
  - [x] topic taxonomy chosen [course.config.json topics, 14 topics]
  - [x] flagship sitting transcribed + validated [tools/raw/25B-B.json, tools/gen/gen_25B-B.py]
  - [x] steps (if open questions) + refuter pass [tools/raw/_verify_25B-B.json]
  - [x] smoke / verify_dom green, running locally [verify_dom.js: all ok]
  - [ ] Adir tried it
- [x] Phase 3 - bank
  - [x] all in-scope sittings transcribed [16 files in tools/raw, tools/gen/gen_*.py]
  - [x] validate.py clean [126 questions, 0 problems]
  - [x] solver run for questions with no trustworthy solution [1 non-official item: 21B-B-Q1, shipped solved + official:false]
  - [x] refuter: non-official all; official 20% sample [tools/raw/_verify_*.json, one per sitting]
  - [x] arbiter / ASK_ADIR for disagreements [ASK_ADIR.md Resolved section]
  - [ ] completeness check per exam (no completeness artifact in the repo)
- [x] Phase 4 - steps
  - [x] step-author batches done for every open question [72 code questions, all with steps]
  - [x] rubricSource / stepsSource labeled [ai-verified on every open question]
  - [x] refuter on every steps block [tools/raw/_verify_*.json]
- [x] Phase 5 - learn
  - [x] learn-writer per topic [docs/briefs/, 15 files]
  - [x] coverage report: no gaps [docs/learn_coverage.md, QA re-pass added 5 concept rows]
- [x] Phase 5b - need help
  - [x] 4 course areas in course.config.json needHelp [linked_lists, dyn_2d, files_strings, c_traps]
  - [x] lessons + coverage, step-author questions [courses/*/C0*.js, 33 levels, 177 questions]
  - [x] course_lint.js --strict clean, refuter clean [tools/verify/needhelp/*/refute.json, check.py: 0 failures]
  - [x] tools/redact.txt filled, validate.py clean [redact.txt 4 names, 0 hits in shipped files]
- [ ] Phase 6 - QA
  - [x] validate, build_questions, build_learn, verify_dom, verify_learn, course_lint, test_aiprompt, test_normalize green
  - [x] shoot.js screenshots taken [tools/raw/shots, 64 shots; gitignored]
  - [ ] render-checker sweep clean (bidi punctuation issues remain, see Notes)
- [ ] Phase 7 - ship  (GATE 3: Adir OKs going public)
  - [ ] deck redesign done (else stop and tell Adir)
  - [x] .gitignore excludes raw PNGs, favicon, GoatCounter, .nojekyll [.gitignore, favicon.svg, index.html, .nojekyll]
  - [ ] year range checked against data
  - [ ] Adir OK to go public
  - [ ] GitHub repo + Pages live
  - [ ] deck tile added
  - [ ] registry status = live

## Notes
- QA 2026-10-18: UB wording fixed in 4 guided questions (linked_lists C03-Q2, C03-Q5, C06-Q1; dyn_2d C02-Q2); trap emoji U+1FAA4 (no glyph on Windows Chrome, showed as an empty box) replaced by U+1F6A7 everywhere; learn pager "14 / 15" was displayed reversed (RTL), now an LTR isolate.
- Remaining visual issue: plain-text punctuation next to Latin/digits renders in the wrong place in RTL (leading period, "typedef-ש", "Item**" goals, "80%." etc.). Being fixed by another agent in normalize.js.
- The 4 re-authored guided questions are machine-checked with clang at -O0 and -O2 but have not been through a fresh blind refuter pass.
