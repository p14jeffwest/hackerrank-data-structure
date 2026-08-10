#!/usr/bin/env python3
"""Test case generator for ds-05-kth-from-end.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Design notes
------------
The book states this with n <= 10^4. Raised here to a sum of n up to 200,000,
which is what makes a quadratic approach -- counting the nodes that follow
each node -- fail.

What the cases are built to catch:

  1. Off-by-one on k. This is the whole difficulty of the problem, and it
     shows only at the ends: k = 1 must give the LAST node and k = n must give
     the FIRST. Cases 01 and 02 are nothing but those two, and cases 03 and 04
     sweep every k for a fixed list so a solution that is off by one anywhere
     is off everywhere.

  2. Quadratic counting. Cases 08 through 13 are large enough to time out.

  3. Reading the value rather than the position. Every list from case 05 on
     contains repeated values, so returning "a node holding the right number"
     is not the same as returning the right node.

  4. Negative values. The answer is a data value, not an index, so it can be
     negative and can be zero.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20260502)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

LIM = 1_000_000_000
NMAX = 200_000


def answer(a, k):
    """The k-th node from the end: k = 1 is the last element."""
    return a[len(a) - k]


def write(idx, cases):
    total = sum(len(a) for a, _ in cases)
    assert 1 <= len(cases) <= 500, "T out of range in case %d" % idx
    assert total <= NMAX, "sum of n = %d exceeds the limit in case %d" % (total, idx)
    for a, k in cases:
        assert 1 <= len(a) <= NMAX
        assert 1 <= k <= len(a), "k out of range in case %d" % idx
        assert all(-LIM <= x <= LIM for x in a)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(cases))
        for a, k in cases:
            f.write("%d %d\n" % (len(a), k))
            f.write(" ".join(map(str, a)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for a, k in cases:
            f.write("%d\n" % answer(a, k))


def rnd(n, lo=-LIM, hi=LIM):
    return [random.randint(lo, hi) for _ in range(n)]


# ---------------------------------------------------------------- hand-built

# 00 sample: the three worked examples from the book
write(0, [([1, 2, 3, 4, 5], 2), ([1, 2, 3], 1), ([1, 2, 3], 3)])

# 01 sample: k = 1 every time, so the answer is always the last node.
#            A solution that is one step short returns the second-to-last.
write(1, [
    ([9], 1),
    ([1, 2], 1),
    ([1, 2, 3, 4, 5, 6, 7], 1),
    ([-5, 0, 5], 1),
])

# 02 sample: k = n every time, so the answer is always the first node.
#            A solution that is one step long walks off the end and crashes.
write(2, [
    ([9], 1),
    ([1, 2], 2),
    ([1, 2, 3, 4, 5, 6, 7], 7),
    ([-5, 0, 5], 3),
])

# 03: every k from 1 to n over one fixed list. An off-by-one anywhere is an
#     off-by-one here.
base = [10, 20, 30, 40, 50, 60, 70, 80]
write(3, [(base, k) for k in range(1, len(base) + 1)])

# 04: the same sweep on a two-element and a three-element list
write(4, [([1, 2], 1), ([1, 2], 2),
          ([7, 8, 9], 1), ([7, 8, 9], 2), ([7, 8, 9], 3)])

# 05: repeated values, so the position is what matters and not the value
write(5, [
    ([4, 4, 4, 4, 4], 3),
    ([1, 1, 2, 1, 1], 3),
    ([0, 0, 0, 7, 0, 0], 3),
    ([5, 5], 2),
])

# 06: zero and negative data
write(6, [
    ([0], 1),
    ([-1, -2, -3], 2),
    ([-1000000000, 0, 1000000000], 3),
    ([1000000000, -1000000000], 1),
])

# 07: many small lists, each with its own k
cases = []
for _ in range(400):
    a = rnd(random.randint(1, 12))
    cases.append((a, random.randint(1, len(a))))
write(7, cases)

# ------------------------------------------------------------------ maximum

# 08: one maximum list, k = 1. The pointer has to reach the very end.
write(8, [(rnd(NMAX), 1)])

# 09: one maximum list, k = n. The answer is the first node, but only after
#     the whole list has been walked.
write(9, [(rnd(NMAX), NMAX)])

# 10: one maximum list, k in the middle
write(10, [(rnd(NMAX), NMAX // 2)])

# 11: T at its maximum, sum of n at its maximum
cases = []
remaining = NMAX
for i in range(500):
    n = 1 if i == 499 else max(1, min(remaining - (500 - i - 1), random.randint(1, 700)))
    remaining -= n
    a = rnd(n)
    cases.append((a, random.randint(1, n)))
write(11, cases)

# 12: a maximum list of one repeated value with a single distinct node placed
#     exactly at the answer, so only the right position gives the right value
a = [42] * NMAX
k = 12345
a[NMAX - k] = -999
write(12, [(a, k)])

# 13: two large lists, one asking for the first node and one for the last
half = NMAX // 2
write(13, [(rnd(half), half), (rnd(half), 1)])

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        t = f.readline().strip()
    print("  case %02d: T = %-5s input %8d bytes" % (i, t, os.path.getsize(path)))
