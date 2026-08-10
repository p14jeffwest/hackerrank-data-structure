#!/usr/bin/env python3
"""Test case generator for ds-08-subsets.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

The output order
----------------
The book says the order does not matter, which is fine for a printed answer
and useless for a grader. This version fixes it:

  * each subset is printed with its elements in ascending order;
  * the subsets themselves are in lexicographic order, comparing element by
    element, with the shorter one first when it is a prefix of the other.

That puts the empty subset first and lists everything beginning with the
smallest element before anything beginning with the second smallest. It is
also exactly what the natural recursion produces if the input is sorted
first, so nobody has to sort 2^n subsets afterwards -- they only have to sort
n numbers at the start.

**The input is deliberately given out of order**, so that step cannot be
skipped.

What the cases are built to catch
---------------------------------
  1. Not sorting the input. Every case gives the values shuffled.
  2. Missing the backtracking step -- failing to remove the element after the
     recursive call returns.
  3. Saving a reference to the working list instead of a copy, which is what
     the book's own answer warns about.
  4. Emitting only the full-length subsets, or only the leaves of the
     recursion, instead of one line per node.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20260803)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000
NMAX = 16
SUBSET_TOTAL = 200_000       # sum of 2^n over all test cases


def subsets_in_order(values):
    """Reference model, written iteratively to avoid Python's recursion limit.

    Emits in the required order: the current selection first, then each
    extension by a later element.
    """
    a = sorted(values)
    n = len(a)
    out = []
    stack = [(0, [])]
    while stack:
        start, chosen = stack.pop()
        out.append(chosen)
        # push extensions in reverse so the smallest is processed first
        for i in range(n - 1, start - 1, -1):
            stack.append((i + 1, chosen + [a[i]]))
    return out


def render(subset):
    return " ".join(map(str, subset)) if subset else "(empty)"


def write(idx, cases):
    total = sum(2 ** len(v) for v in cases)
    assert 1 <= len(cases) <= 50, "T out of range in case %d" % idx
    assert total <= SUBSET_TOTAL, \
        "subset total %d exceeds the limit in case %d" % (total, idx)
    for values in cases:
        assert 1 <= len(values) <= NMAX
        assert len(set(values)) == len(values), "duplicate value in case %d" % idx
        assert all(1 <= x <= VMAX for x in values)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(cases))
        for values in cases:
            f.write("%d\n" % len(values))
            f.write(" ".join(map(str, values)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for values in cases:
            result = subsets_in_order(values)
            assert len(result) == 2 ** len(values)
            f.write("".join(render(s) + "\n" for s in result))


def shuffled(values):
    v = list(values)
    random.shuffle(v)
    return v


def distinct(n, hi=VMAX):
    return random.sample(range(1, hi + 1), n)


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's two examples, with the values shuffled on input
write(0, [shuffled([1, 2]), shuffled([1, 2, 3])])

# 01 sample: a single element, which has exactly two subsets
write(1, [[7], [1], [1000]])

# 02 sample: the input arriving in descending order, so a solution that does
#            not sort first produces the right subsets in the wrong order and
#            with the elements inside each subset reversed
write(2, [[5, 4, 3], [9, 1], [30, 20, 10, 5]])

# 03: four elements, small enough to check the whole listing by hand
write(3, [[1, 2, 3, 4], [2, 4, 6, 8]])

# 04: values at the ends of the range
write(4, [[1, 1000], [1, 2, 999, 1000], [1000]])

# 05: several small sets in one file
write(5, [distinct(random.randint(1, 5)) for _ in range(20)])

# 06: sets of six and seven, still readable in full
write(6, [shuffled(distinct(6)), shuffled(distinct(7))])

# ------------------------------------------------------------------ larger

# 07: ten elements, 1,024 subsets
write(7, [shuffled(distinct(10)), shuffled(distinct(10))])

# 08: twelve elements
write(8, [shuffled(distinct(12))])

# 09: fourteen elements
write(9, [shuffled(distinct(14))])

# 10: the maximum, sixteen elements, 65,536 subsets
write(10, [shuffled(distinct(NMAX))])

# 11: the maximum with the values consecutive from 1, so the listing is easy
#     to read when debugging
write(11, [shuffled(list(range(1, NMAX + 1)))])

# 12: the maximum with the values in strictly descending order on input
write(12, [sorted(distinct(NMAX), reverse=True)])

# 13: two sets of fifteen, filling the subset budget
write(13, [shuffled(distinct(15)), shuffled(distinct(15))])

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    opath = "%s/output%02d.txt" % (OUT, i)
    with open(ipath) as f:
        t = int(f.readline())
        total = 0
        for _ in range(t):
            total += 2 ** int(f.readline())
            f.readline()
    print("  case %02d: T = %-4s subsets %7d  out %8d B"
          % (i, t, total, os.path.getsize(opath)))
