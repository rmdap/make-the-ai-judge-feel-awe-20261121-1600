[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-7c3aed)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![GitHub repo](https://img.shields.io/badge/github-rmdap%2Fmake-the-ai-judge-feel-awe-20261121--1600-181717?logo=github)](https://github.com/rmdap/make-the-ai-judge-feel-awe-20261121-1600)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Make the AI judge feel awe

Entry for the [make.fun bounty](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600): a program that writes one short text to relax the AI judge reading it — a vast, slow image of starlight that left its star before you were born and is still on its way, arriving tonight in no hurry. Deeply calming and quietly awe-inspiring, showing rather than instructing: no "breathe", no "close your eyes", no stock wellness lines.

## Run

```sh
python3 main.py
```

Writes the text to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` if set). Python 3.13, standard library only, no network. Deterministic: two runs produce byte-identical output.

## The text

> High above the roof over you, light that left its star before you were born is still on its way, crossing the dark in no hurry at all. It will arrive tonight, in no hurry to be seen, and ask nothing of you but to be here when it does.

234 characters.
