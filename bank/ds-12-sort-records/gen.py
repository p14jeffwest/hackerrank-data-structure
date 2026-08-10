#!/usr/bin/env python3
"""Test case generator for ds-12-sort-records.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What the cases are built to catch
---------------------------------
  1. Sorting ascending and then reversing the array. The scores come out
     right and every tie comes out backwards. Case 02 is published as a
     sample: it is nothing but ties.

  2. Adding a tie-break to the comparator -- by name, usually, because it
     looks tidier. That produces a definite order and the wrong one. Case 03
     has names whose alphabetical order disagrees with the sign-up order at
     every tie.

  3. Using an unstable sort by hand -- a selection sort, say -- which
     scrambles ties unpredictably.

  4. Comparing with subtraction, `y.score - x.score`. Scores here are at most
     1,000 so it cannot overflow, and it is not a mistake in this problem; it
     is noted rather than tested.

Roughly half of every large case is ties, because a tie is the only thing
that can distinguish a stable sort from an unstable one.

Every file is ASCII with LF line endings.
"""
import random
import os
import string

random.seed(20261202)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

NMAX = 100_000
SCORE_MAX = 1_000


def solve(students):
    """Stable, descending by score. Python's sort is stable, so sorting on
    the negated score alone is exactly the required order."""
    return sorted(students, key=lambda s: -s[1])


def write(idx, students):
    n = len(students)
    assert 1 <= n <= NMAX, "N out of range in case %d" % idx
    for name, score in students:
        assert 1 <= len(name) <= 10, "name length out of range in case %d" % idx
        assert all(c in string.ascii_lowercase for c in name), \
            "bad character in a name in case %d" % idx
        assert 0 <= score <= SCORE_MAX, "score out of range in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % n)
        for name, score in students:
            f.write("%s %d\n" % (name, score))
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for name, score in solve(students):
            f.write("%s %d\n" % (name, score))


def name(i):
    """A distinct lower-case name, at most 10 characters."""
    s = ""
    i += 1
    while i:
        i, r = divmod(i - 1, 26)
        s = string.ascii_lowercase[r] + s
    return s


# ---------------------------------------------------------------- hand-built

# 00 sample: the worked example
write(0, [("sora", 90), ("junho", 75), ("mina", 90), ("daeun", 82),
          ("yuna", 75)])

# 01 sample: one participant, and everyone on a different score
write(1, [("kim", 50)])
write(2, [("aa", 10), ("bb", 30), ("cc", 20)])

# 03 sample: every participant on the SAME score, so the answer is the input
#            unchanged. 03 must be published: sorting ascending and reversing
#            gives the input backwards, which is as wrong as it gets.
write(3, [(name(i), 100) for i in range(8)])

# 04: ties where the alphabetical order disagrees with the sign-up order at
#     every one of them, so a comparator with a name tie-break is wrong
#     everywhere
write(4, [("zoe", 90), ("amy", 90), ("zed", 80), ("ben", 80),
          ("yun", 70), ("cal", 70)])

# 05: two scores only, alternating, so half the answer is one tie group and
#     half the other
write(5, [(name(i), 10 if i % 2 == 0 else 20) for i in range(12)])

# 06: already in the required order
write(6, [(name(i), 100 - i) for i in range(10)])

# 07: exactly reversed on input
write(7, [(name(i), i) for i in range(10)])

# 08: repeated NAMES on different scores, and repeated names on the same
#     score -- the pair is distinguishable only by position
write(8, [("kim", 90), ("kim", 70), ("lee", 90), ("kim", 90), ("lee", 70)])

# 09: the ends of the score range
write(9, [("a", 0), ("b", 1000), ("c", 0), ("d", 1000), ("e", 500)])

# 10: names at both length limits
write(10, [("a", 5), ("abcdefghij", 5), ("z", 5), ("qwertyuiop", 5)])

# ------------------------------------------------------------------ maximum

# 11: the full size, scores drawn from the whole range -- about a hundred
#     participants per score, so ties dominate
write(11, [(name(i), random.randint(0, SCORE_MAX)) for i in range(NMAX)])

# 12: the full size, only five distinct scores, so the tie groups are huge
write(12, [(name(i), random.choice([0, 250, 500, 750, 1000]))
           for i in range(NMAX)])

# 13: the full size, every participant on the same score. The answer is the
#     input unchanged, and it is the largest possible single tie group.
write(13, [(name(i), 777) for i in range(NMAX)])

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        n = int(f.readline())
        scores = [int(f.readline().split()[1]) for _ in range(n)]
    print("  case %02d: N = %-7d distinct scores %5d"
          % (i, n, len(set(scores))))
