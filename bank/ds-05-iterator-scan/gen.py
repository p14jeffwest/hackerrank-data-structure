#!/usr/bin/env python3
"""Test case generator for ds-05-iterator-scan.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Design notes
------------
This is the one problem in chapter 5 where the mistake is caught by the clock
rather than by a wrong value. The Head deliberately offers both routes through
the list -- index-based get/add/set, and a cursor -- and only one of them
finishes. Reaching position i by index walks i links from head, so a loop over
positions costs 1 + 2 + ... + n hops. At n = 200,000 that is about
2 * 10^10 and cannot run; the same pass with a cursor is 200,000 hops.

What the cases are built to catch:

  1. The index-based route. Cases 07 through 13 are large enough to time out,
     while 00 through 06 are small enough to pass, so the mistake shows as a
     partial score and the student can see that their logic was right and
     their traversal was not.

  2. Testing oddness with `x % 2 == 1`. Java's remainder keeps the sign of the
     dividend, so -3 % 2 is -1 and every negative odd value slips through.
     Case 01 is published as a sample for exactly this, and case 11 is a
     200,000-element list of negative odd values.

  3. Swapping the two branches.

Values are capped at 10^8 in absolute value so that ten times a value still
fits in an int. Raising that cap would silently introduce an overflow this
problem is not about.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20260504)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

LIM = 100_000_000          # x * 10 must still fit in an int
NMAX = 200_000


def transform(a):
    """Reference model: after each odd value insert a 0; multiply evens by 10."""
    out = []
    for x in a:
        if x % 2 != 0:     # Python's % differs from Java's on negatives, so
            out.append(x)  # compare against zero here as well
            out.append(0)
        else:
            out.append(x * 10)
    return out


def write(idx, lists):
    total = sum(len(a) for a in lists)
    assert 1 <= len(lists) <= 500, "T out of range in case %d" % idx
    assert total <= NMAX, "sum of n = %d exceeds the limit in case %d" % (total, idx)
    for a in lists:
        assert len(a) <= NMAX
        assert all(-LIM <= x <= LIM for x in a), "value out of range in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(lists))
        for a in lists:
            f.write("%d\n" % len(a))
            f.write(" ".join(map(str, a)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for a in lists:
            r = transform(a)
            f.write((" ".join(map(str, r)) if r else "(empty)") + "\n")


def rnd(n, lo=-LIM, hi=LIM):
    return [random.randint(lo, hi) for _ in range(n)]


# ---------------------------------------------------------------- hand-built

# 00 sample: the worked examples from the statement, plus an empty list
write(0, [[1, 2, 3, 4, 5], [-3, -2, 0, 7], []])

# 01 sample: negative odd values, which is where `% 2 == 1` fails.
#            Published on purpose -- it is the only place the student can see
#            that mistake before submitting.
write(1, [
    [-1, -3, -5],
    [-1, 1],
    [-7, 8, -9, 10],
    [-2, -1, 0, 1, 2],
])

# 02 sample: all odd, then all even
write(2, [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [0, 0, 0],
])

# 03: zero on its own, and zero surrounded by odd values
write(3, [[0], [1, 0, 1], [0, 1, 0], [0, 0, 1, 1]])

# 04: the ends of the value range, where x * 10 lands exactly on 10^9
write(4, [
    [LIM, -LIM],
    [LIM - 1, -(LIM - 1)],
    [99999999, -99999999, 100000000, -100000000],
])

# 05: single-element lists of each shape
write(5, [[1], [2], [-1], [-2], [0]])

# 06: many small lists
write(6, [rnd(random.randint(0, 15)) for _ in range(400)])

# ------------------------------------------------------------------ maximum

# 07: T at its maximum, sum of n at its maximum
lists = []
remaining = NMAX
for i in range(500):
    n = 1 if i == 499 else max(1, min(remaining - (500 - i - 1), random.randint(1, 700)))
    remaining -= n
    lists.append(rnd(n))
write(7, lists)

# 08: one maximum list, every value odd, so the result is twice as long
write(8, [[2 * random.randint(0, LIM // 2 - 1) + 1 for _ in range(NMAX)]])

# 09: one maximum list, every value even, so nothing is inserted and every
#     element is rewritten in place
write(9, [[2 * random.randint(-LIM // 2, LIM // 2) for _ in range(NMAX)]])

# 10: one maximum list, random
write(10, [rnd(NMAX)])

# 11: one maximum list of negative odd values. A `% 2 == 1` test treats the
#     entire list as even and multiplies all of it by ten.
write(11, [[-(2 * random.randint(0, LIM // 2 - 1) + 1) for _ in range(NMAX)]])

# 12: one maximum list alternating strictly between odd and even
write(12, [[(2 * random.randint(0, LIM // 2 - 1) + 1) if i % 2 == 0
            else 2 * random.randint(-LIM // 2, LIM // 2)
            for i in range(NMAX)]])

# 13: two large lists, one all odd and one mixed sign
half = NMAX // 2
write(13, [
    [2 * random.randint(0, LIM // 2 - 1) + 1 for _ in range(half)],
    rnd(half),
])

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    opath = "%s/output%02d.txt" % (OUT, i)
    with open(ipath) as f:
        t = f.readline().strip()
    print("  case %02d: T = %-5s in %8d B  out %8d B"
          % (i, t, os.path.getsize(ipath), os.path.getsize(opath)))
