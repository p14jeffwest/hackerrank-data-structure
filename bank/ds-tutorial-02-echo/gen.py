#!/usr/bin/env python3
"""Test case generator for ds-tutorial-02-echo.

The case list is fixed, so rerunning this produces identical files.

    python3 gen.py

Design notes
------------
The point of this problem is the difference between Scanner.next(), which
stops at the first space, and Scanner.nextLine(), which takes the whole line.
So the set is deliberately split:

  * single-token lines  -> a next() solution passes these
  * lines with spaces   -> a next() solution fails these

That split is what turns the intended mistake into a partial score instead of
a zero, which is the lesson. Case 01 is published as a sample precisely so a
student can discover the problem before submitting.

Everything written here is ASCII, and every file uses LF line endings.
"""
import os

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

# A line of exactly 1000 characters, the maximum the constraints allow.
# "abcdefghij " is 11 characters; 90 repeats give 990, plus 10 more.
MAX_LINE = ("abcdefghij " * 90) + "abcdefghij"
assert len(MAX_LINE) == 1000, len(MAX_LINE)

cases = [
    # 00 sample: a single token, so a next() solution also passes this one
    "Hello",
    # 01 sample: contains spaces. Published on purpose -- this is the case
    #            that exposes next() before the student submits.
    "Data Structure is a 15-week course",
    # 02: shortest possible input, one character
    "A",
    # 03: a long line of ordinary words
    "Seoul National University of Science and Technology",
    # 04: digits only, single token
    "12345",
    # 05: a sentence ending in a period
    "Java 17 is the version this course uses.",
    # 06: runs of consecutive spaces must survive unchanged
    "spaces   between   words",
    # 07: mixed case must not be altered
    "MiXeD CaSe LeTtErS",
    # 08: punctuation and symbols
    "Symbols: !@#$%^&*()_+-=[]{};',.<>/?",
    # 09: the lesson of this problem, spelled out in the data
    "next() reads one token, nextLine() reads the whole line",
    # 10: a single zero, single token
    "0",
    # 11: every letter of the alphabet plus digits
    "The quick brown fox jumps over the lazy dog 0123456789",
    # 12: maximum length
    MAX_LINE,
]

for i, line in enumerate(cases):
    assert line.isascii(), "non-ASCII in case %d" % i
    assert 1 <= len(line) <= 1000, "length out of range in case %d" % i
    assert line == line.strip(), "leading/trailing space in case %d" % i
    with open("%s/input%02d.txt" % (IN, i), "w", newline="\n") as f:
        f.write(line + "\n")
    with open("%s/output%02d.txt" % (OUT, i), "w", newline="\n") as f:
        f.write(line + "\n")

single_token = sum(1 for c in cases if " " not in c)
print("generated %d cases" % len(cases))
print("%d of them are single tokens, so a next() solution scores %d/%d"
      % (single_token, single_token, len(cases)))
