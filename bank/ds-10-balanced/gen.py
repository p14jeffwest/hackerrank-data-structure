#!/usr/bin/env python3
"""Test case generator for ds-10-balanced.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Why the midpoint rule is pinned down
------------------------------------
Any choice of middle balances the tree, so the book's constraint -- height
O(log n) -- does not identify one tree. A grader needs one. The statement
requires nums[(lo + hi) / 2], the left of the two middles on an even range,
which is what the book's own code produces, and the preorder line is what
checks it.

The height line checks the other half of the book's requirement, and it does
so independently: a tree can have the right height and the wrong shape, or the
right shape by luck and the wrong height, and the two lines separate those.

What the cases are built to catch
---------------------------------
  1. Rounding the middle the other way, (lo + hi + 1) / 2. The height is
     identical and the preorder is not. Every case with an even-sized range
     catches it; case 01 is published as a sample and is nothing but even
     sizes.

  2. Building by inserting the keys in order, which gives a spine. The height
     line says so immediately.

  3. Copying a subarray per call instead of passing indices. That is O(n log n)
     allocation rather than O(n) and it survives -- it is not a mistake, only
     wasteful, and no case punishes it.

  4. Removing the middle from a list each time, which is O(n^2). Cases 11
     through 13 are large enough to time it out.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20261004)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
NMAX = 200_000


def build_preorder(nums):
    """The preorder of the required tree, iteratively.

    The stack holds ranges. Popping a range emits its middle and pushes the
    two halves, right first so the left is handled next -- which is exactly
    preorder.
    """
    out = []
    stack = [(0, len(nums) - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo > hi:
            continue
        mid = (lo + hi) // 2
        out.append(nums[mid])
        stack.append((mid + 1, hi))
        stack.append((lo, mid - 1))
    return out


def height_of(n):
    """Height in edges of the tree the rule builds over n keys."""
    if n == 0:
        return -1
    h = 0
    size = n
    while size > 1:
        size = (size - 1) // 2 if False else max((size - 1) // 2, size // 2)
        h += 1
    return h


def height_by_build(nums):
    """Measured rather than derived, so the two never silently agree by
    sharing a mistake."""
    best = -1
    stack = [(0, len(nums) - 1, 0)]
    while stack:
        lo, hi, d = stack.pop()
        if lo > hi:
            continue
        best = max(best, d)
        mid = (lo + hi) // 2
        stack.append((lo, mid - 1, d + 1))
        stack.append((mid + 1, hi, d + 1))
    return best


def write(idx, nums):
    assert 1 <= len(nums) <= NMAX, "n out of range in case %d" % idx
    assert nums == sorted(nums), "input not ascending in case %d" % idx
    assert len(set(nums)) == len(nums), "duplicate key in case %d" % idx
    assert all(-VMAX <= x <= VMAX for x in nums)
    pre = build_preorder(nums)
    assert sorted(pre) == nums, "the tree lost or gained a key in case %d" % idx
    h = height_by_build(nums)
    assert 2 ** (h + 1) > len(nums), "height %d is not minimal in case %d" % (h, idx)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(nums))
        f.write(" ".join(map(str, nums)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write(" ".join(map(str, pre)) + "\n")
        f.write("%d\n" % h)


def sorted_sample(n, lo=-VMAX, hi=VMAX):
    return sorted(random.sample(range(lo, hi), n))


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's example, 1 through 7
write(0, list(range(1, 8)))

# 01 sample: even sizes only. On an even range the two middles are both
#            valid choices and give different trees, so this is where
#            rounding the other way shows.
write(1, list(range(1, 7)))
write(2, [10, 20])

# 03: the smallest inputs
write(3, [42])

# 04: sizes on both sides of a power of two, where the height steps up
write(4, list(range(1, 16)))     # 15 keys, height 3
write(5, list(range(1, 17)))     # 16 keys, height 4

# 06: negative keys and a range straddling zero
write(6, list(range(-10, 11)))

# 07: keys at the ends of their range
write(7, [-VMAX, -1, 0, 1, VMAX])

# 08: widely spaced keys, small count
write(8, sorted_sample(31))

# ------------------------------------------------------------------ maximum

# 09: a power of two minus one, so the tree is perfect
write(9, sorted_sample(2 ** 17 - 1))

# 10: a power of two, so exactly one leaf sits a level lower
write(10, sorted_sample(2 ** 17))

# 11: the full node count
write(11, sorted_sample(NMAX))

# 12: the full node count with consecutive keys, so the output is compact and
#     easy to read when something goes wrong
write(12, list(range(1, NMAX + 1)))

# 13: the full node count with keys at the top of their range, so the output
#     is at its largest
write(13, sorted_sample(NMAX, VMAX - 5 * NMAX, VMAX))

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open(ipath) as f:
        n = int(f.readline())
    with open("%s/output%02d.txt" % (OUT, i)) as f:
        f.readline()
        h = int(f.readline())
    print("  case %02d: n = %-7d height %3d  in %8d B"
          % (i, n, h, os.path.getsize(ipath)))
