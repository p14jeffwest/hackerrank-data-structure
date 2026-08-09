#!/usr/bin/env python3
"""Test case generator for ds-04-rotate.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Design notes
------------
The book states this problem with n and k both at most 10^4. At that size
every approach passes, including rotating one slot at a time, so the problem
separates nobody. The bounds here are raised to n <= 200,000 and k <= 10^9,
which turns the book's own hint ("compute k % n first") into the thing the
problem actually tests.

Three mistakes are meant to show up as a partial score:

  1. Rotating one slot at a time, k times. O(n*k), and with k near 10^9 it
     cannot finish however small n is. Cases 06 and 10 carry large k.

  2. Rotating left instead of right. Fails everywhere except where the two
     directions coincide, which is why case 02 deliberately includes k % n
     equal to 0 -- a left-rotation solution passes exactly those and nothing
     else.

  3. Building the output by string concatenation. O(n^2) on the 200,000
     element cases.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20260410)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

BIG = 1_000_000_000
NMAX = 200_000


def rotate(a, k):
    """Reference model: k slots to the right."""
    n = len(a)
    k %= n
    return a[n - k:] + a[:n - k]


def write(idx, cases):
    total = sum(len(a) for a, _ in cases)
    assert 1 <= len(cases) <= 500, "T out of range in case %d" % idx
    assert total <= NMAX, "sum of n = %d exceeds the limit in case %d" % (total, idx)
    for a, k in cases:
        assert 1 <= len(a) <= NMAX
        assert 1 <= k <= BIG, "k out of range in case %d" % idx
        assert all(1 <= x <= BIG for x in a)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(cases))
        for a, k in cases:
            f.write("%d %d\n" % (len(a), k))
            f.write(" ".join(map(str, a)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for a, k in cases:
            f.write(" ".join(map(str, rotate(a, k))) + "\n")


def rnd(n, hi=BIG):
    return [random.randint(1, hi) for _ in range(n)]


# ---------------------------------------------------------------- hand-built

# 00 sample: the two worked examples from the statement
write(0, [([1, 2, 3, 4, 5], 2), ([1, 2, 3], 4)])

# 01 sample: the shapes that break a careless split point.
#            n = 1 (any k leaves it alone), k equal to n, k one less than n,
#            k = 1, and a k far larger than n.
write(1, [
    ([7], 1),
    ([7], 1_000_000_000),
    ([1, 2, 3, 4], 4),
    ([1, 2, 3, 4], 3),
    ([1, 2, 3, 4], 1),
    ([1, 2, 3, 4], 999_999_999),
])

# 02 sample: k % n == 0 every time, so the list comes back unchanged.
#            A left-rotation solution passes this case and only this case,
#            which is what makes it worth publishing.
write(2, [
    ([1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 4, 5], 10),
    ([9, 9, 9], 3),
    ([4, 1, 3, 2], 8),
    ([5], 12345),
])

# 03: two elements, where rotating left and rotating right agree on odd k
#     and disagree on even k
write(3, [([1, 2], k) for k in [1, 2, 3, 4, 5, 6, 999_999_999, 1_000_000_000]])

# 04: repeated values, so an off-by-one in the split point is still visible
write(4, [
    ([5, 5, 5, 5, 1], 1),
    ([5, 5, 5, 5, 1], 4),
    ([1, 5, 5, 5, 5], 1),
    ([2, 2, 3, 3, 2, 2], 3),
])

# 05: many small lists
write(5, [(rnd(random.randint(1, 8), 50), random.randint(1, 20))
          for _ in range(200)])

# 06: k pinned near the top of its range against small lists.
#     This is the case a one-slot-at-a-time solution cannot survive: it has
#     to run about 10^9 steps even though the lists are tiny.
write(6, [(rnd(random.randint(1, 5)), random.randint(999_000_000, BIG))
          for _ in range(300)])

# 07: T at its maximum, sum of n at its maximum
cases = []
remaining = NMAX
for i in range(500):
    n = 1 if i == 499 else min(remaining - (500 - i - 1), random.randint(1, 700))
    n = max(1, n)
    remaining -= n
    cases.append((rnd(n), random.randint(1, BIG)))
write(7, cases)

# ------------------------------------------------------------------ maximum

# 08: a single maximum list, k = 1 (the last element alone moves to the front)
write(8, [(rnd(NMAX), 1)])

# 09: a single maximum list, k = n - 1 (everything but the first moves up)
write(9, [(rnd(NMAX), NMAX - 1)])

# 10: a single maximum list with k at the top of its range.
#     BIG itself is an exact multiple of NMAX, which would reduce to k % n = 0
#     and quietly turn this into a no-rotation case. BIG - 1 gives the largest
#     k that still forces a real split (k % n = 199,999).
write(10, [(rnd(NMAX), BIG - 1)])

# 11: a single maximum list, k a multiple of n, so the answer is the input
write(11, [(rnd(NMAX), NMAX * 5)])

# 12: two large lists, all values at the ceiling, to push the output size
half = NMAX // 2
write(12, [([BIG] * half, 7), (rnd(half), half // 2)])

# 13: maximum-size list of a single repeated value, plus one distinct value
#     at the end, so only a correct split point shows the difference
a = [42] * (NMAX - 1) + [77]
write(13, [(a, 1)])

print("generated 14 cases")
for i in range(14):
    with open("%s/input%02d.txt" % (IN, i)) as f:
        t = f.readline().strip()
    size = os.path.getsize("%s/input%02d.txt" % (IN, i))
    print("  case %02d: T = %-5s input %8d bytes" % (i, t, size))
