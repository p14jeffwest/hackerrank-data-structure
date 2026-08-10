#!/usr/bin/env python3
"""Test case generator for ds-13-inversions.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What the cases are built to catch
---------------------------------
  1. Checking every pair, O(n^2). At n = 200,000 that is 2 * 10^10
     comparisons. Cases 10 through 13 are large enough; the smaller ones are
     not, so the mistake shows as a partial score rather than a blank.

  2. Counting equal values as inversions. `<` instead of `<=` in the merge
     does that, and case 02 is published as a sample: an array of nothing but
     repeats, where the answer is 0 and the mistake gives a large number.

  3. Counting in an int. A reversed array of 200,000 values has about
     2 * 10^10 inversions, which overflows silently. Case 11 is exactly that
     array.

  4. Adding the wrong quantity at the merge -- 1 instead of the number of
     values left in the left half. That is right only when the halves
     interleave one for one, so case 03 alternates and case 04 does not.

The model counts inversions with a Fenwick tree over the compressed values,
which shares no reasoning with the merge-sort method.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20261303)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
NMAX = 200_000


def count_inversions(a):
    """Fenwick tree over rank order, sweeping from the right.

    For each position, count how many already-seen values (all of which are to
    its right) are strictly smaller. Deliberately a different method from the
    one the problem teaches.
    """
    order = {v: i + 1 for i, v in enumerate(sorted(set(a)))}
    size = len(order)
    tree = [0] * (size + 1)
    total = 0
    for v in reversed(a):
        r = order[v]
        # how many strictly smaller values are already to the right
        i = r - 1
        while i > 0:
            total += tree[i]
            i -= i & (-i)
        i = r
        while i <= size:
            tree[i] += 1
            i += i & (-i)
    return total


def write(idx, a):
    n = len(a)
    assert 1 <= n <= NMAX, "n out of range in case %d" % idx
    assert all(-VMAX <= v <= VMAX for v in a)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % n)
        f.write(" ".join(map(str, a)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("%d\n" % count_inversions(a))


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's three examples
write(0, [2, 4, 1, 3, 5])
write(1, [3, 2, 1])

# 02 sample: nothing but repeats, so the answer is 0. 02 must be published:
#            counting equal values as inversions gives 45 here.
write(2, [5] * 10)

# 03: alternating high and low, where the halves interleave one for one
write(3, [1, 10, 2, 11, 3, 12, 4, 13])

# 04: the second half entirely below the first, so one merge step accounts for
#     a whole block at once
write(4, [10, 11, 12, 13, 1, 2, 3, 4])

# 05: a single value, and two values each way round
write(5, [42])
write(6, [1, 2])
write(7, [2, 1])

# 08: already ascending at a size worth checking, so the answer is 0
write(8, list(range(1, 101)))

# 09: negatives and the ends of the range, with repeats
write(9, [1000000000, -1000000000, 0, -1000000000, 1000000000, 0])

# ------------------------------------------------------------------ maximum

# 10: the full size, random -- about n^2/4 inversions
write(10, [random.randint(-VMAX, VMAX) for _ in range(NMAX)])

# 11: the full size, strictly descending. Every pair is an inversion:
#     199,999 * 200,000 / 2 = 19,999,900,000, which overflows an int.
write(11, list(range(NMAX, 0, -1)))

# 12: the full size, ascending -- the answer is 0 and an O(n^2) solution still
#     has to look at every pair to find that out
write(12, list(range(1, NMAX + 1)))

# 13: the full size drawn from a tiny set of values, so most pairs are equal
#     and are not inversions
write(13, [random.randint(1, 3) for _ in range(NMAX)])

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open(ipath) as f:
        n = int(f.readline())
    with open("%s/output%02d.txt" % (OUT, i)) as f:
        ans = int(f.readline())
    print("  case %02d: n = %-7d inversions %14d%s"
          % (i, n, ans, "   (exceeds int)" if ans > 2**31 - 1 else ""))
