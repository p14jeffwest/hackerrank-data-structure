#!/usr/bin/env python3
"""Test case generator for ds-12-kth-largest.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What this problem can enforce
-----------------------------
Both approaches the book compares -- a full sort, O(n log n), and a size-k
min-heap, O(n log k) -- finish this comfortably. Neither is meant to be
excluded; 12.8 Problem 1 is explicitly about choosing between them.

What IS excluded is the third approach students reach for first: take the
maximum out, k times. That is O(n*k), and with k near n it does not finish.
Cases 11 through 13 have k at or near n for exactly that reason, and cases 09
and 10 keep k small so the mistake scores partially rather than not at all.

What the cases are built to catch
---------------------------------
  1. The O(n*k) repeated maximum, as above.

  2. Reading the sorted array from the wrong end -- nums[k-1] instead of
     nums[n-k]. Case 02 is published as a sample and is asymmetric, so the two
     never coincide.

  3. Counting distinct values rather than positions. In 5 5 3 the 2nd largest
     is 5, not 3. Case 03 is built from heavy duplicates.

  4. An off-by-one in k. Case 01 asks for k = 1 and k = n on the same data,
     which are the maximum and the minimum.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20261203)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
NMAX = 200_000


def write(idx, nums, k):
    n = len(nums)
    assert 1 <= n <= NMAX, "N out of range in case %d" % idx
    assert 1 <= k <= n, "K out of range in case %d" % idx
    assert all(-VMAX <= v <= VMAX for v in nums)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d %d\n" % (n, k))
        f.write(" ".join(map(str, nums)) + "\n")
    answer = sorted(nums)[n - k]
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("%d\n" % answer)


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's two examples
write(0, [3, 2, 1, 5, 6, 4], 2)
write(1, [3, 2, 3, 1, 2, 4, 5, 5, 6], 4)

# 02 sample: k = 1 and k = n on the same data -- the maximum and the minimum
write(2, [10, 40, 20, 30], 1)
write(3, [10, 40, 20, 30], 4)

# 04 sample: heavy duplicates. In 9 9 9 5 1 the 2nd largest is 9 and the 4th
#            is 5, because equal values occupy separate positions.
#            04 must be published: a solution counting DISTINCT values answers
#            5 for k = 2.
write(4, [9, 9, 9, 5, 1], 2)
write(5, [9, 9, 9, 5, 1], 4)

# 06: a single value
write(6, [42], 1)

# 07: every value identical
write(7, [7] * 10, 5)

# 08: already ascending, and already descending
write(8, list(range(1, 21)), 7)
write(9, list(range(20, 0, -1)), 7)

# 10: values at the ends of the range, and negatives
write(10, [-1000000000, 1000000000, 0, -1, 1], 2)

# ------------------------------------------------------------------ maximum

# 11: the full size with k small -- the size-k heap is at its best, and the
#     repeated-maximum mistake survives, which keeps it partial
write(11, [random.randint(-VMAX, VMAX) for _ in range(NMAX)], 5)

# 12: the full size with k in the middle -- O(n*k) is 2 * 10^10
write(12, [random.randint(-VMAX, VMAX) for _ in range(NMAX)], NMAX // 2)

# 13: the full size with k = n, so the answer is the minimum and the
#     repeated-maximum approach does its worst
write(13, [random.randint(-VMAX, VMAX) for _ in range(NMAX)], NMAX)

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        n, k = map(int, f.readline().split())
    print("  case %02d: N = %-7d K = %-7d  n*k = %14d" % (i, n, k, n * k))
