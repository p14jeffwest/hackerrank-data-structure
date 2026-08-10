#!/usr/bin/env python3
"""Test case generator for ds-08-climb-stairs.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

A note on the bound
-------------------
The book states n <= 45. The Korean counterpart raised it to 90 and this
version keeps that, because 45 sits on exactly the wrong side of a line:

    ways(45) = 1,836,311,903   fits in an int
    ways(46) = 2,971,215,073   does not
    ways(90) = 4,660,046,610,375,530,309   fits in a long, with room to spare

At n <= 45 an int solution is correct and the type question never arises. At
n <= 90 it is the point of the problem.

What the cases are built to catch
---------------------------------
  1. Counting in int. Everything up to n = 45 is right and everything from
     n = 46 is wrong -- silently, with no exception and no warning. Case 02
     is published as a sample and holds exactly 45 and 46.

  2. Plain recursion without memoization, O(2^n). Anything past about n = 40
     does not finish. Cases 01 and 11 keep n small on purpose so the mistake
     is a partial score.

  3. Base cases. ways(1) = 1 and ways(2) = 2, not 1 -- the two-step staircase
     has two routes, 1+1 and 2. Getting ways(2) wrong shifts every later
     answer by one position in the sequence.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20260802)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

NMAX = 90
TMAX = 1_000

ways = [0] * (NMAX + 1)
ways[1] = 1
if NMAX >= 2:
    ways[2] = 2
for i in range(3, NMAX + 1):
    ways[i] = ways[i - 1] + ways[i - 2]

assert ways[45] < 2 ** 31
assert ways[46] >= 2 ** 31
assert ways[90] < 2 ** 63


def write(idx, queries):
    assert 1 <= len(queries) <= TMAX, "T out of range in case %d" % idx
    assert all(1 <= n <= NMAX for n in queries), "N out of range in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(queries))
        f.write("\n".join(map(str, queries)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for n in queries:
            f.write("%d\n" % ways[n])


# ---------------------------------------------------------------- hand-built

# 00 sample: the worked example
write(0, [1, 2, 3, 4, 5, 90])

# 01 sample: the first ten staircases, small enough that even plain recursion
#            answers them
write(1, list(range(1, 11)))

# 02 sample: the int boundary. 45 is the last answer that fits in an int and
#            46 is the first that does not, so a solution counting in int
#            gets the first right and the second wrong -- with no error of any
#            kind. Published because nothing else reveals it.
write(2, [44, 45, 46, 47])

# 03: a wider sweep either side of the boundary
write(3, list(range(40, 51)))

# 04: the top of the range
write(4, [88, 89, 90, 90, 89, 88])

# 05: every staircase from 1 to 90, in order
write(5, list(range(1, NMAX + 1)))

# 06: every staircase from 90 down to 1
write(6, list(range(NMAX, 0, -1)))

# 07: the same query repeated, which a solution recomputing from scratch each
#     time pays for over and over
write(7, [90] * 500)

# ------------------------------------------------------------------ maximum

# 08: T at its maximum, uniformly random over the whole range
write(8, [random.randint(1, NMAX) for _ in range(TMAX)])

# 09: T at its maximum, alternating 45 and 46 -- half the answers fit in an
#     int and half do not
write(9, [45 if i % 2 == 0 else 46 for i in range(TMAX)])

# 10: T at its maximum, all at 90
write(10, [NMAX] * TMAX)

# 11: T at its maximum, all small. Plain recursion survives this one, which
#     is what keeps that mistake partial rather than total.
write(11, [random.randint(1, 20) for _ in range(TMAX)])

# 12: T at its maximum, drawn only from the upper half
write(12, [random.randint(46, NMAX) for _ in range(TMAX)])

# 13: T at its maximum, drawn only from the lower half, where an int solution
#     is still correct
write(13, [random.randint(1, 45) for _ in range(TMAX)])

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        t = int(f.readline())
        qs = [int(f.readline()) for _ in range(t)]
    over = sum(1 for n in qs if ways[n] >= 2 ** 31)
    big = sum(1 for n in qs if n > 40)
    print("  case %02d: T = %-6s beyond int %5d  n > 40 %5d" % (i, t, over, big))
