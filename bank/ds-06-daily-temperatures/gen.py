#!/usr/bin/env python3
"""Test case generator for ds-06-daily-temperatures.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Design notes
------------
The book states this with n <= 10^5. Raised here to a sum of n up to 300,000,
which puts the naive scan out of reach.

Note what the narrow temperature range does. The book pins temperatures to
30..100, so there are only 71 distinct values and a strictly decreasing run
can be at most 71 long. That does NOT save the naive solution: when every
reading is identical, no day ever finds a warmer one, so the forward scan runs
to the end from every position and the cost is n^2/2. The same input is also
the worst case for the stack, which fills to all n indices because an equal
reading never pops anything.

What the cases are built to catch:

  1. Scanning forward from each day, O(n^2). Cases 08 through 13 are large
     enough to time out.

  2. Comparing with >= instead of >. A day of equal temperature is not warmer.
     Case 02 is published as a sample for this, and cases 01, 05 and 12 are
     built almost entirely out of ties.

  3. Pushing temperatures instead of indices, which loses the distance.

  4. Getting the distance off by one -- i - waiting, not i - waiting - 1.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20260603)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

LO, HI = 30, 100          # the book's temperature range
NMAX = 300_000


def solve(temps):
    """Reference model, computed the direct way rather than with a stack."""
    n = len(temps)
    answer = [0] * n
    stack = []
    for i in range(n):
        while stack and temps[i] > temps[stack[-1]]:
            waiting = stack.pop()
            answer[waiting] = i - waiting
        stack.append(i)
    return answer


def write(idx, cases):
    total = sum(len(a) for a in cases)
    assert 1 <= len(cases) <= 500, "T out of range in case %d" % idx
    assert total <= NMAX, "sum of n = %d exceeds the limit in case %d" % (total, idx)
    for a in cases:
        assert 1 <= len(a) <= NMAX
        assert all(LO <= x <= HI for x in a), "temperature out of range in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(cases))
        for a in cases:
            f.write("%d\n" % len(a))
            f.write(" ".join(map(str, a)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for a in cases:
            f.write(" ".join(map(str, solve(a))) + "\n")


def rnd(n):
    return [random.randint(LO, HI) for _ in range(n)]


# ---------------------------------------------------------------- hand-built

# 00 sample: the three worked examples from the book
write(0, [[73, 74, 75, 71, 69, 72, 76, 73], [30, 40, 50, 60], [30, 60, 90]])

# 01 sample: every reading identical, so nothing is ever warmer and every
#            answer is 0. A solution comparing with >= settles each day
#            against the next one and answers 1 all the way along.
write(1, [[50] * 6, [30] * 3, [100] * 5, [42, 42]])

# 02 sample: ties with a warmer day further on, which is where >= and >
#            disagree most visibly.
#            [73, 73, 74] -> [2, 1, 0]: the first day waits two days, not one.
write(2, [
    [73, 73, 74],
    [50, 50, 50, 60],
    [60, 50, 50, 70],
    [40, 40, 39, 41],
])

# 03: the smallest inputs
write(3, [[55], [30], [100], [50, 50], [50, 51], [51, 50]])

# 04: strictly increasing, then strictly decreasing
write(4, [list(range(30, 101)), list(range(100, 29, -1))])

# 05: only the two ends of the range, so the input is almost all ties
write(5, [[random.choice([LO, HI]) for _ in range(300)] for _ in range(20)])

# 06: many small random cases
write(6, [rnd(random.randint(1, 25)) for _ in range(400)])

# 07: T at its maximum, sum of n at its maximum
cases = []
remaining = NMAX
for i in range(500):
    n = 1 if i == 499 else max(1, min(remaining - (500 - i - 1), random.randint(1, 1100)))
    remaining -= n
    cases.append(rnd(n))
write(7, cases)

# ------------------------------------------------------------------ maximum

# 08: one maximum list, every reading identical. The worst case for both the
#     naive scan (n^2/2 comparisons) and the stack (it fills to all n).
write(8, [[70] * NMAX])

# 09: a long descent with a single warm day at the very end. Every day does
#     have a warmer day, but it is the last one, so the forward scan travels
#     almost the whole array from almost every position: n^2/2 comparisons.
#     Descending blocks were tried first and were not enough -- with a warmer
#     day only a block away the naive scan finished in about 0.6 s.
descent = [HI - 1 - (i * (HI - 1 - LO)) // (NMAX - 1) for i in range(NMAX - 1)]
write(9, [descent + [HI]])

# 10: one maximum list, random
write(10, [rnd(NMAX)])

# 11: one maximum list, sawtooth. Every second day settles immediately, so the
#     stack stays shallow and the answers are mostly 1.
write(11, [[LO if i % 2 == 0 else HI for i in range(NMAX)]])

# 12: one maximum list of long runs of equal values, with the runs slowly
#     climbing. Ties dominate, and only the run boundaries settle anything.
# The runs are long on purpose: the warmer day is always the start of the
# next run, so the run length is exactly how far the naive scan has to walk.
seq = []
value = LO
while len(seq) < NMAX:
    run = min(NMAX - len(seq), random.randint(20000, 40000))
    seq += [value] * run
    value += 1
    if value > HI:
        value = LO
write(12, [seq[:NMAX]])

# 13: two large lists, one descending overall and one ascending overall
half = NMAX // 2
desc = sorted(rnd(half), reverse=True)
asc = sorted(rnd(half))
write(13, [desc, asc])

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open(ipath) as f:
        t = int(f.readline())
        total = 0
        for _ in range(t):
            total += int(f.readline())
            f.readline()
    print("  case %02d: T = %-5s sum n %7d  in %8d B" % (i, t, total, os.path.getsize(ipath)))
