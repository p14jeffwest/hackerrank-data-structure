#!/usr/bin/env python3
"""Test case generator for ds-13-merge-two.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What this problem can and cannot enforce
----------------------------------------
It cannot exclude concatenating the two arrays and calling Arrays.sort. That
is O((n+m) log(n+m)) against the merge's O(n+m), and on 400,000 ints the
difference is tens of milliseconds -- nowhere near a time limit. The book asks
for the merge because it is the step merge sort is built from, not because
sorting would be too slow here.

What the cases DO enforce is that the merge itself is right, which is where
the mistakes are: a tail left uncopied, or the wrong array taken on a tie.

What the cases are built to catch
---------------------------------
  1. Copying only one of the two tails. Whichever array runs out first
     decides which tail loop matters, so cases 03 and 04 put all the large
     values in one array and then the other.

  2. An empty array on either side. Case 02 is published as a sample.

  3. Ties handled by dropping one of the two equal values. Case 05 is two
     arrays of identical values.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20261301)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
TOTAL = 400_000


def write(idx, a, b):
    assert a == sorted(a), "a is not ascending in case %d" % idx
    assert b == sorted(b), "b is not ascending in case %d" % idx
    assert len(a) + len(b) <= TOTAL, "too many values in case %d" % idx
    assert len(a) + len(b) >= 1, "both arrays empty in case %d" % idx
    assert all(-VMAX <= v <= VMAX for v in a + b)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        # An empty array writes its length and NO values line at all, rather
        # than a blank one. The Tail reads with StreamTokenizer, which ignores
        # line structure entirely, so a blank line would carry no information
        # and would only be something an editor or an archive could strip.
        for x in (a, b):
            f.write("%d\n" % len(x))
            if x:
                f.write(" ".join(map(str, x)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write(" ".join(map(str, sorted(a + b))) + "\n")


def asc(n, lo=-VMAX, hi=VMAX):
    return sorted(random.randint(lo, hi) for _ in range(n))


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's two examples
write(0, [1, 3, 5, 7], [2, 4, 6])
write(1, [1, 1, 2], [1, 3])

# 02 sample: an empty array on each side. 02 must be published: with nothing
#            to compare against, one of the two tail loops does all the work
#            and the other must not run.
write(2, [], [1, 2, 3])

# 03: every value of `a` below every value of `b`, so `a` runs out first
write(3, [1, 2, 3, 4], [10, 20, 30])

# 04: the reverse, so `b` runs out first
write(4, [10, 20, 30], [1, 2, 3, 4])

# 05: both arrays entirely made of the same value, so every comparison is a
#     tie and nothing may be dropped
write(5, [7] * 6, [7] * 5)

# 06: one array of a single value, the other long
write(6, [50], list(range(1, 20)))

# 07: interleaving exactly, one from each in turn
write(7, list(range(0, 20, 2)), list(range(1, 20, 2)))

# 08: values at the ends of the range, and negatives
write(8, [-1000000000, 0, 1000000000], [-1, 1])

# 09: many duplicates spread across both
write(9, sorted([1, 1, 2, 2, 3] * 3), sorted([2, 3, 3, 4] * 3))

# ------------------------------------------------------------------ maximum

# 10: both arrays at half the budget, random values -- they interleave
write(10, asc(TOTAL // 2), asc(TOTAL // 2))

# 11: the budget almost all in one array
write(11, asc(TOTAL - 10), asc(10))

# 12: the two ranges disjoint at full size, so one tail loop copies 200,000
#     values in one go
write(12, asc(TOTAL // 2, -VMAX, -1), asc(TOTAL // 2, 0, VMAX))

# 13: full size, every value the same
write(13, [42] * (TOTAL // 2), [42] * (TOTAL // 2))

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    # read as a token stream, the same way the Tail does -- reading by line
    # breaks on the cases where an empty array writes no values line
    with open(ipath) as f:
        toks = f.read().split()
    n = int(toks[0])
    m = int(toks[1 + n])
    print("  case %02d: n = %-7d m = %-7d  in %8d B"
          % (i, n, m, os.path.getsize(ipath)))
