#!/usr/bin/env python3
"""Test case generator for ds-12-merge-intervals.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

The boundary rule is the OPPOSITE of ds-11-meeting-rooms
--------------------------------------------------------
Both problems take a list of {start, end} intervals, and the two treat a
touching pair differently, because the questions differ:

  ds-11-meeting-rooms : a meeting ending at t and one starting at t do NOT
                        overlap -- one room takes both.
  this problem        : intervals [1,4] and [4,5] DO merge, into [1,5].

The book states each rule in its own chapter. Anyone editing one of these two
generators should check they have not carried the other's comparison across.

What the cases are built to catch
---------------------------------
  1. Not sorting by start. Overlapping intervals are only adjacent once
     sorted, and without that a single pass cannot work. Every case gives the
     intervals shuffled.

  2. Comparing with >= so touching intervals are left separate. Case 02 is
     published as a sample: a chain of intervals meeting end to start, which
     must collapse into one.

  3. Taking the new interval's end rather than the larger of the two. An
     interval wholly inside the current group -- [1,10] then [2,3] -- would
     shrink it. Case 03 is built from nested intervals.

  4. Comparing every pair, O(n^2). Cases 10 through 13 are large enough.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20261204)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

TMAX = 1_000_000_000
NMAX = 200_000


def merge(intervals):
    """Reference model: sort by start, then close a group at the first gap."""
    out = []
    for s, e in sorted(intervals):
        if out and out[-1][1] >= s:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out


def write(idx, intervals):
    n = len(intervals)
    assert 1 <= n <= NMAX, "n out of range in case %d" % idx
    for s, e in intervals:
        assert 0 <= s <= e <= TMAX, "bad interval in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % n)
        for s, e in intervals:
            f.write("%d %d\n" % (s, e))
    result = merge(intervals)
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(result))
        for s, e in result:
            f.write("%d %d\n" % (s, e))


def shuffled(intervals):
    x = [tuple(i) for i in intervals]
    random.shuffle(x)
    return x


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's first example
write(0, [(1, 3), (2, 6), (8, 10), (15, 18)])

# 01 sample: a single interval, and two that do not touch at all
write(1, [(5, 7)])
write(2, [(1, 2), (5, 6)])

# 03 sample: intervals meeting end to start. They MERGE here -- the opposite
#            of the rule in ds-11-meeting-rooms. 03 must be published: a
#            solution comparing with >= leaves all five separate.
write(3, shuffled([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]))

# 04 sample: nested intervals. [1,10] swallows [2,3] and [4,5], and a
#            solution that takes the newer end shrinks the group to [1,3].
write(4, shuffled([(1, 10), (2, 3), (4, 5), (11, 12)]))

# 05: every interval identical
write(5, [(3, 8)] * 6)

# 06: zero-length intervals, where start equals end
write(6, shuffled([(1, 1), (1, 1), (2, 2), (5, 5), (2, 5)]))

# 07: one interval covering everything, plus many inside it
write(7, shuffled([(0, 1000)] + [(i, i + 1) for i in range(0, 100, 7)]))

# 08: a chain where each interval overlaps only its neighbour, so everything
#     collapses into one
write(8, shuffled([(i, i + 2) for i in range(40)]))

# 09: nothing overlaps, so the answer is the input sorted
write(9, shuffled([(3 * i, 3 * i + 1) for i in range(40)]))

# 10: the ends of the time range
write(10, shuffled([(0, 0), (0, 1000000000), (999999999, 1000000000),
                    (500000000, 500000001)]))

# ------------------------------------------------------------------ maximum


def random_intervals(n, span, length_hi):
    out = []
    for _ in range(n):
        s = random.randint(0, span)
        out.append((s, min(TMAX, s + random.randint(0, length_hi))))
    return out


# 11: the full size, short intervals over a wide span -- almost nothing
#     merges, so the answer is nearly as long as the input
write(11, random_intervals(NMAX, TMAX, 1000))

# 12: the full size, long intervals over a narrow span -- almost everything
#     merges into one
write(12, random_intervals(NMAX, 100_000, 100_000))

# 13: the full size, laid end to start and shuffled. Every pair touches, so
#     the whole lot collapses to a single interval -- and a >= comparison
#     returns 200,000 of them.
write(13, shuffled([(i, i + 1) for i in range(NMAX)]))

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open(ipath) as f:
        n = int(f.readline())
    with open("%s/output%02d.txt" % (OUT, i)) as f:
        m = int(f.readline())
    print("  case %02d: n = %-7d merged to %-7d  in %8d B"
          % (i, n, m, os.path.getsize(ipath)))
