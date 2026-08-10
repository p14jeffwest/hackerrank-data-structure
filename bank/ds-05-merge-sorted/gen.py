#!/usr/bin/env python3
"""Test case generator for ds-05-merge-sorted.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Design notes
------------
The book states this with n, m <= 10^4 and forbids creating new nodes. Two
things are different here.

  * The bound is raised to a sum of n+m up to 200,000, which is what makes an
    insert-each-node-by-scanning approach, O(n*m), fail.

  * The no-new-nodes rule is actually checked. The driver registers every node
    it hands over and, after the call, walks the merged list confirming that
    every node in it was one of those and that none appears twice. Reading
    both lists into an array, sorting, and rebuilding produces a perfectly
    correct sequence of values and is still reported as `invalid`.

What the cases are built to catch:

  1. Dropping the leftover tail. Forgetting to attach whatever remains when
     one list runs out loses nodes, and the driver reports `invalid` because
     the count no longer matches. Cases 03 and 05 have very lopsided lengths,
     which makes the loss large and certain.

  2. Mishandling an empty input list. Cases 02 and 06 cover n = 0, m = 0, and
     both at once.

  3. Quadratic merging. Cases 09 through 13 are large enough to time out.

  4. Building new nodes. Every case catches it.

Equal values across the two lists are common on purpose, though note that
choosing `<` rather than `<=` cannot be detected: it swaps two nodes carrying
the same number, so the printed values are identical either way.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20260503)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

LIM = 1_000_000_000
TOTAL = 200_000


def write(idx, cases):
    total = sum(len(a) + len(b) for a, b in cases)
    assert 1 <= len(cases) <= 500, "T out of range in case %d" % idx
    assert total <= TOTAL, "sum of n+m = %d exceeds the limit in case %d" % (total, idx)
    for a, b in cases:
        assert a == sorted(a), "list A not sorted in case %d" % idx
        assert b == sorted(b), "list B not sorted in case %d" % idx
        assert all(-LIM <= x <= LIM for x in a + b)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(cases))
        for a, b in cases:
            f.write("%d %d\n" % (len(a), len(b)))
            f.write(" ".join(map(str, a)) + "\n")
            f.write(" ".join(map(str, b)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for a, b in cases:
            merged = sorted(a + b)
            f.write((" ".join(map(str, merged)) if merged else "(empty)") + "\n")


def srt(n, lo=-LIM, hi=LIM):
    return sorted(random.randint(lo, hi) for _ in range(n))


# ---------------------------------------------------------------- hand-built

# 00 sample: the three worked examples from the book
write(0, [([1, 3, 5], [2, 4]), ([1, 2], [3, 4, 5]), ([], [1, 2])])

# 01 sample: values shared between the two lists, and runs of equal values
write(1, [
    ([1, 2, 3], [1, 2, 3]),
    ([5, 5, 5], [5, 5]),
    ([1, 1, 4], [1, 4, 4]),
    ([2], [2]),
])

# 02 sample: the empty cases, including both lists empty at once
write(2, [
    ([], []),
    ([], [7]),
    ([7], []),
    ([], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], []),
])

# 03: one list far longer than the other, in both directions. Dropping the
#     leftover tail loses most of the answer here.
write(3, [
    (list(range(1, 51)), [100]),
    ([-100], list(range(1, 51))),
    (list(range(1, 51)), [0]),
    ([0], list(range(1, 51))),
])

# 04: fully disjoint ranges, so one list is exhausted before the other starts
write(4, [
    ([1, 2, 3], [10, 20, 30]),
    ([10, 20, 30], [1, 2, 3]),
    ([-5, -4], [-3, -2]),
])

# 05: single-element lists in every arrangement
write(5, [([1], [2]), ([2], [1]), ([1], [1]),
          ([-1000000000], [1000000000]), ([1000000000], [-1000000000])])

# 06: many small cases, some with an empty side
cases = []
for _ in range(300):
    n = random.choice([0, 0, 1, 2, 3, 5, 8])
    m = random.choice([0, 1, 2, 3, 5, 8])
    cases.append((srt(n, -50, 50), srt(m, -50, 50)))
write(6, cases)

# 07: zero and negative values, with the two lists interleaving tightly
write(7, [
    ([-3, -1, 0, 2], [-2, 0, 1, 3]),
    ([0, 0, 0], [0, 0, 0]),
    ([-1000000000, 0], [0, 1000000000]),
])

# 08: T at its maximum with a moderate total
cases = []
remaining = TOTAL // 3
for i in range(500):
    take = max(2, min(remaining - 2 * (500 - i - 1), random.randint(2, 200)))
    remaining -= take
    n = random.randint(0, take)
    cases.append((srt(n), srt(take - n)))
write(8, cases)

# ------------------------------------------------------------------ maximum

half = TOTAL // 2

# 09: two maximum lists of equal length, interleaving throughout
a = srt(half)
b = srt(half)
write(9, [(a, b)])

# 10: two maximum lists over disjoint ranges, so the whole of one is attached
#     in a single step at the end
write(10, [(srt(half, -LIM, -1), srt(half, 1, LIM))])

# 11: the extreme of case 03 at full size -- one node against everything else
write(11, [([LIM], srt(TOTAL - 1)), ])

# 12: one maximum list against an empty one, in both directions
write(12, [(srt(half), []), ([], srt(half))])

# 13: two maximum lists of the same repeated value, so every comparison is a
#     tie and the merge never gets to skip ahead
write(13, [([7] * half, [7] * half)])

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        t = f.readline().strip()
    print("  case %02d: T = %-5s input %8d bytes" % (i, t, os.path.getsize(path)))
