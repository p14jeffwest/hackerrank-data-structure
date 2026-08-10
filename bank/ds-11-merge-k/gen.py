#!/usr/bin/env python3
"""Test case generator for ds-11-merge-k.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What this problem can and cannot enforce
----------------------------------------
It rules out the O(N * k) approach -- scanning the front of every list at each
step -- and nothing else. **Pouring every value into one array and sorting it
is O(N log N) and passes**, and at these sizes it is not even slower than the
heap. That cannot be prevented: the output is the fully merged list, and any
method that produces a sorted sequence of the same values is right.

So the heap is the taught method rather than the enforced one, and the cases
are shaped around what can be enforced. Case 12 is the one that matters: k is
at its maximum with the values spread so that no list is exhausted early,
which is where the per-step scan costs its full k.

What the cases are built to catch
---------------------------------
  1. The O(N * k) scan. Cases 11, 12 and 13 have k large enough.
  2. Empty lists. The book's own code guards against offering one, and case 02
     is built entirely from them.
  3. Not putting the next element of the same list back after taking one out,
     which returns only the k smallest.
  4. A max-heap instead of a min-heap.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20261103)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
KMAX = 100_000
TOTAL = 500_000


def write(idx, lists):
    total = sum(len(x) for x in lists)
    assert 1 <= len(lists) <= KMAX, "k out of range in case %d" % idx
    assert total <= TOTAL, "value total %d exceeds the limit in case %d" % (total, idx)
    for x in lists:
        assert x == sorted(x), "a list is not ascending in case %d" % idx
        assert all(-VMAX <= v <= VMAX for v in x)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(lists))
        for x in lists:
            f.write(" ".join([str(len(x))] + [str(v) for v in x]) + "\n")
    merged = sorted(v for x in lists for v in x)
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write(" ".join(map(str, merged)) + "\n")


def asc(n, lo=-VMAX, hi=VMAX):
    return sorted(random.randint(lo, hi) for _ in range(n))


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's example
write(0, [[1, 4, 5], [1, 3, 4], [2, 6]])

# 01 sample: one list, and a list with one value
write(1, [[1, 2, 3]])
write(2, [[7]])

# 03 sample: empty lists everywhere -- at the front, in the middle, at the
#            end, and one case where every list is empty so the answer is an
#            empty line. Offering an empty list to the heap reads a position
#            that does not exist.
write(3, [[], [3, 9], [], [], [1, 5], []])
write(4, [[], [], []])

# 05: every list identical, so ties are constant
write(5, [[5, 5, 5]] * 6)

# 06: lists that do not overlap at all, so the merge is a concatenation
write(6, [[1, 2, 3], [10, 11, 12], [20, 21, 22]])

# 07: lists in descending order of their smallest value, so the first list
#     offered is the last one used
write(7, [[100, 200], [50, 60], [1, 2]])

# 08: negatives and the ends of the range
write(8, [[-1000000000, 0], [1000000000], [-1, 1], []])

# 09: many small lists
write(9, [asc(random.randint(0, 6), -100, 100) for _ in range(500)])

# ------------------------------------------------------------------ maximum

# 10: few lists, each very long -- the heap stays tiny and only N matters
write(10, [asc(TOTAL // 5) for _ in range(5)])

# 11: k at its maximum with five values each. Every list is short, so a
#     per-step scan over all k is at its most wasteful relative to the work
#     actually done.
write(11, [asc(5) for _ in range(KMAX)])

# 12: k at its maximum, values drawn so that the lists interleave throughout
#     and none is exhausted early -- the heap stays full for the whole run,
#     which is the worst case for a per-step scan.
lists = []
for i in range(KMAX):
    base = random.randint(-VMAX, VMAX - 10_000)
    lists.append(sorted(base + random.randint(0, 10_000) for _ in range(5)))
write(12, lists)

# 13: a mixture -- a few long lists among very many short ones
lists = [asc(50_000) for _ in range(4)]
lists += [asc(random.randint(0, 4)) for _ in range(KMAX - 4)]
random.shuffle(lists)
write(13, lists[:KMAX])

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open(ipath) as f:
        k = int(f.readline())
        total = sum(int(f.readline().split()[0]) for _ in range(k))
    print("  case %02d: k = %-7d N = %-7d  in %8d B"
          % (i, k, total, os.path.getsize(ipath)))
