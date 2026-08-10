#!/usr/bin/env python3
"""Test case generator for ds-12-sort-trace.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Why the array stays small
-------------------------
n is capped at 2,000, inherited from the Korean counterpart, and it is not a
missed chance to raise a bound. Selection sort is O(n*k), which at k = n-1 is
O(n^2); a larger n would time out the intended solution, not a wrong one.
There is nothing to gain by growing it.

What the cases are built to catch
---------------------------------
  1. Sorting the whole array and then reporting it, ignoring k. Case 01 has
     k = 0 and k = 1 on the same array, where the answer is nowhere near
     sorted.

  2. Treating a pass as "move one element" rather than "settle one position".
     The tail of the array after k passes is NOT the original order -- the
     swaps have disturbed it -- and that is the whole point of asking for an
     intermediate state. Case 02 is built so the tail is visibly scrambled.

  3. Skipping the swap when the smallest value is already in place. The array
     is unchanged either way, but the pass is used up, so a solution that
     "retries" the position runs ahead of the count. Case 03 is an already
     sorted array, where every pass is a self-swap.

  4. Modifying the caller's array. The driver passes the array it read; the
     statement asks for a copy. Nothing in the output depends on it here, so
     no case can check it -- it is recorded as an exam point instead.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20261201)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
NMAX = 2_000


def selection_passes(a, k):
    b = list(a)
    for i in range(k):
        m = i
        for j in range(i + 1, len(b)):
            if b[j] < b[m]:
                m = j
        b[i], b[m] = b[m], b[i]
    return b


def write(idx, a, k):
    n = len(a)
    assert 1 <= n <= NMAX, "n out of range in case %d" % idx
    assert 0 <= k <= n - 1, "k out of range in case %d" % idx
    assert all(-VMAX <= v <= VMAX for v in a)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d %d\n" % (n, k))
        f.write(" ".join(map(str, a)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write(" ".join(map(str, selection_passes(a, k))) + "\n")


# ---------------------------------------------------------------- hand-built

# 00 sample: the worked example, three passes
write(0, [5, 2, 4, 1, 3], 3)

# 01 sample: k = 0 on the same array. Nothing has happened yet, so the answer
#            is the input unchanged -- which a solution that just sorts gets
#            wrong immediately.
write(1, [5, 2, 4, 1, 3], 0)

# 02 sample: one pass on an array whose tail then ends up scrambled. The
#            smallest value is at the back, so after pass 1 the value that was
#            at the front is sitting at the back -- the tail is NOT the
#            original order.
write(2, [9, 3, 7, 5, 1], 1)

# 03: an already sorted array, where every pass swaps a value with itself.
#     The array never changes, but the passes are still used up.
write(3, list(range(1, 11)), 5)

# 04: a reversed array, the worst case for movement
write(4, list(range(10, 0, -1)), 4)

# 05: k at its maximum, so the array comes out fully sorted
write(5, [5, 2, 4, 1, 3], 4)

# 06: a single element, where k can only be 0
write(6, [42], 0)

# 07: two elements, both orders
write(7, [2, 1], 1)
write(8, [1, 2], 1)

# 09: repeated values, where the choice of which equal value moves matters.
#     Selection sort takes the FIRST minimum it meets.
write(9, [3, 1, 3, 1, 2], 2)

# 10: values at the ends of the range, and negatives
write(10, [1000000000, -1000000000, 0, -1, 1], 2)

# ------------------------------------------------------------------ maximum

# 11: the full size with k at its maximum -- the whole array is sorted
a = [random.randint(-VMAX, VMAX) for _ in range(NMAX)]
write(11, a, NMAX - 1)

# 12: the full size stopped halfway, so the front is sorted and the back is
#     the disturbed remainder
a = [random.randint(-VMAX, VMAX) for _ in range(NMAX)]
write(12, a, NMAX // 2)

# 13: the full size, reversed on input, stopped a third of the way through
write(13, list(range(NMAX, 0, -1)), NMAX // 3)

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        n, k = map(int, f.readline().split())
    print("  case %02d: n = %-6d k = %-6d" % (i, n, k))
