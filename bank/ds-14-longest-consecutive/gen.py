#!/usr/bin/env python3
"""Test case generator for ds-14-longest-consecutive.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

The book forbids sorting; the clock does not
--------------------------------------------
14.7 Problem 1 says "sorting would be O(n log n), so it is not allowed". That
is a statement about what the exercise is for, not something a time limit can
enforce. Measured here at n = 100,000:

    one long consecutive run : hash 197 ms, sort 228 ms
    random values, no runs   : hash 228 ms, sort 191 ms

Sorting is FASTER on random data. A HashSet of boxed Integers has a large
constant, and Arrays.sort on an int[] has a tiny one; the log factor does not
close that gap at any size this problem can carry. So the requirement is
stated in the constraints and assessed on the exam, the same position as
ds-13-counting-sort and ds-13-merge-two.

What the clock DOES enforce is the start-of-run check:

    one long consecutive run : correct 197 ms, without the check 15,717 ms
    random values            : correct 228 ms, without the check    239 ms

Without it a run of length L is walked from each of its L members. That is the
mistake the book's answer calls "the key", and cases 09 through 13 are built
around it -- long runs, shuffled.

What the cases are built to catch
---------------------------------
  1. Walking each run from every member instead of only from its start.
  2. Counting duplicates as extending a run. Case 02 is published for it.
  3. An empty array, where the answer is 0.
  4. Runs that cross zero or sit at the ends of the value range.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20261404)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
NMAX = 200_000


def solve(nums):
    values = set(nums)
    best = 0
    for v in values:
        if v - 1 in values:
            continue
        length = 1
        nxt = v + 1
        while nxt in values:
            length += 1
            nxt += 1
        best = max(best, length)
    return best


def write(idx, nums):
    n = len(nums)
    assert 0 <= n <= NMAX, "n out of range in case %d" % idx
    assert all(-VMAX <= v <= VMAX for v in nums)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % n)
        if nums:
            f.write(" ".join(map(str, nums)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("%d\n" % solve(nums))


def shuffled(values):
    v = list(values)
    random.shuffle(v)
    return v


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's two examples
write(0, [100, 4, 200, 1, 3, 2])
write(1, [0, 3, 7, 2, 5, 8, 4, 6, 0, 1])

# 02 sample: duplicates. Six values, but only three distinct ones, so the
#            longest run is 3 and not 6. 02 must be published: a solution that
#            lets a repeat extend a run answers 6.
write(2, [5, 5, 6, 6, 7, 7])

# 03: an empty array, where the answer is 0. The values line is omitted
#     entirely rather than left blank -- the Tail reads with StreamTokenizer,
#     which ignores line structure, so a blank line would carry no information
#     and could only be lost in transit.
write(3, [])

# 04: a single value
write(4, [42])

# 05: no two values adjacent, so every run has length 1
write(5, [10, 20, 30, 40, 50])

# 06: a run crossing zero
write(6, shuffled(range(-5, 6)))

# 07: values at the ends of their range, including a run at each end
write(7, [VMAX, VMAX - 1, VMAX - 2, -VMAX, -VMAX + 1, 0])

# 08: two runs of the same length, and one longer than both
write(8, shuffled([1, 2, 3] + [10, 11, 12] + [20, 21, 22, 23]))

# ------------------------------------------------------------------ maximum

# 09: one consecutive run covering everything, shuffled. This is the case the
#     start-of-run check exists for: without it the run is walked from each of
#     its 200,000 members.
write(9, shuffled(range(1, NMAX + 1)))

# 10: the same length of run, but built from many duplicates so the distinct
#     count is half the input
values = list(range(1, NMAX // 2 + 1)) * 2
write(10, shuffled(values))

# 11: a few long runs rather than one, so the walk restarts several times
values = []
for start in range(0, 5):
    values += list(range(start * 10_000_000, start * 10_000_000 + NMAX // 5))
write(11, shuffled(values))

# 12: random values over the whole range, where runs are rare and short --
#     the shape where the O(n^2) mistake survives, which keeps it partial
write(12, [random.randint(-VMAX, VMAX) for _ in range(NMAX)])

# 13: one long run with random values scattered among it
half = NMAX // 2
values = list(range(-half // 2, half - half // 2))
values += [random.randint(-VMAX, VMAX) for _ in range(NMAX - len(values))]
write(13, shuffled(values))

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open(ipath) as f:
        n = int(f.readline())
    with open("%s/output%02d.txt" % (OUT, i)) as f:
        ans = int(f.readline())
    print("  case %02d: n = %-7d longest run %-7d  in %8d B"
          % (i, n, ans, os.path.getsize(ipath)))
