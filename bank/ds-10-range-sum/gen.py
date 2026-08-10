#!/usr/bin/env python3
"""Test case generator for ds-10-range-sum.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Why there are many queries
--------------------------
The book states this with a single query, and a single query cannot punish a
full traversal: O(n) once is fine. Pruning only pays when the same tree is
asked many times, so this version gives Q queries against one tree and the
cost becomes O(nQ) without it.

The queries also have to be NARROW. A query covering most of the tree visits
most of it however it is written, so a random low/high pair over the whole key
range separates nothing. Cases 09 through 13 use windows holding a handful of
keys, which is where pruning is the difference between the height and the
whole tree.

What the cases are built to catch
---------------------------------
  1. A full traversal per query, testing each key against the range. Cases 09
     through 13 time it out; the small ones do not, so the score is partial.

  2. Accumulating in an int. With 200,000 keys of up to 10^9 a single query
     reaches 2 * 10^14. Case 02 is a small tree whose total still exceeds the
     int range, and it is published as a sample.

  3. Getting the pruning backwards -- skipping the left when the key is too
     large. Case 03 is built so that mistake loses exactly the keys it should
     have kept.

  4. Treating the range as exclusive. Both ends are inclusive, and case 01
     asks for windows that begin and end exactly on a key.

Every file is ASCII with LF line endings.
"""
import random
import os
from collections import deque

random.seed(20261003)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
NMAX = 200_000
HMAX = 5_000
QMAX = 200_000


class Tree:
    def __init__(self):
        self.key, self.left, self.right = [], [], []

    def add(self, k):
        self.key.append(k)
        self.left.append(-1)
        self.right.append(-1)
        return len(self.key) - 1

    def size(self):
        return len(self.key)


def bst_from_sorted(keys):
    """A balanced BST over sorted keys, built iteratively."""
    t = Tree()
    if not keys:
        return t
    root = t.add(0)
    stack = [(root, 0, len(keys) - 1)]
    while stack:
        node, lo, hi = stack.pop()
        mid = (lo + hi) // 2
        t.key[node] = keys[mid]
        if lo <= mid - 1:
            c = t.add(0)
            t.left[node] = c
            stack.append((c, lo, mid - 1))
        if mid + 1 <= hi:
            c = t.add(0)
            t.right[node] = c
            stack.append((c, mid + 1, hi))
    return t


def spine(keys):
    """A right spine: keys inserted in ascending order."""
    t = Tree()
    t.add(keys[0])
    for i in range(1, len(keys)):
        c = t.add(keys[i])
        t.right[i - 1] = c
    return t


def tokens_of(t):
    out = [str(t.key[0])]
    q = deque([0])
    while q:
        i = q.popleft()
        for c in (t.left[i], t.right[i]):
            if c == -1:
                out.append("#")
            else:
                out.append(str(t.key[c]))
                q.append(c)
    while len(out) > 1 and out[-1] == "#":
        out.pop()
    return out


def height_of(t):
    best, stack = 0, [(0, 1)]
    while stack:
        i, d = stack.pop()
        best = max(best, d)
        for c in (t.left[i], t.right[i]):
            if c != -1:
                stack.append((c, d + 1))
    return best


def write(idx, tree, queries):
    assert 1 <= tree.size() <= NMAX, "node count out of range in case %d" % idx
    assert height_of(tree) <= HMAX, "height cap broken in case %d" % idx
    assert 1 <= len(queries) <= QMAX, "Q out of range in case %d" % idx
    assert all(lo <= hi for lo, hi in queries), "low > high in case %d" % idx
    assert all(-VMAX <= v <= VMAX for v in tree.key)
    keys = sorted(tree.key)
    assert len(set(keys)) == len(keys), "duplicate key in case %d" % idx

    # answers computed by a plain scan of the sorted keys -- no tree involved,
    # so the model shares nothing with the solution
    import bisect
    prefix = [0]
    for k in keys:
        prefix.append(prefix[-1] + k)

    toks = tokens_of(tree)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(toks))
        f.write(" ".join(toks) + "\n")
        f.write("%d\n" % len(queries))
        for lo, hi in queries:
            f.write("%d %d\n" % (lo, hi))
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for lo, hi in queries:
            a = bisect.bisect_left(keys, lo)
            b = bisect.bisect_right(keys, hi)
            f.write("%d\n" % (prefix[b] - prefix[a]))


def narrow_queries(keys, n, width):
    """Windows holding roughly `width` keys, placed anywhere in the tree."""
    out = []
    for _ in range(n):
        i = random.randrange(len(keys))
        j = min(len(keys) - 1, i + width)
        out.append((keys[i], keys[j]))
    return out


# ---------------------------------------------------------------- hand-built

BOOK = bst_from_sorted([3, 5, 7, 10, 15, 18])
# rebuild the book's exact shape rather than a balanced one
BOOK = Tree()
for k in [10, 5, 15, 3, 7, 18]:
    BOOK.add(k)
BOOK.left[0], BOOK.right[0] = 1, 2      # 10 -> 5, 15
BOOK.left[1], BOOK.right[1] = 3, 4      # 5 -> 3, 7
BOOK.right[2] = 5                       # 15 -> 18

# 00 sample: the book's two worked queries
write(0, BOOK, [(7, 15), (6, 10)])

# 01 sample: both ends inclusive, an empty window, a window covering
#            everything, and windows that start and end exactly on a key
write(1, BOOK, [(3, 3), (18, 18), (3, 18), (11, 14), (-100, 100),
                (5, 7), (10, 10), (16, 17)])

# 02 sample: a small tree whose total exceeds the int range.
#            The keys are near 10^9 and there are six of them, so the answer
#            is about 5.5 * 10^9 -- an int accumulator returns a wrong,
#            possibly negative, number.
big = [999999995, 999999996, 999999997, 999999998, 999999999, 1000000000]
write(2, bst_from_sorted(big), [(big[0], big[-1]), (big[2], big[-1]),
                                (big[0], big[0])])

# 03: pruning in both directions. The queries sit entirely to the left of the
#     root, then entirely to the right, so a solution that skips the wrong
#     side loses precisely what it should have kept.
keys = list(range(1, 32))
t = bst_from_sorted(keys)
write(3, t, [(1, 5), (27, 31), (1, 15), (17, 31), (16, 16), (1, 31)])

# 04: negative keys and a window straddling zero
keys = list(range(-20, 21))
write(4, bst_from_sorted(keys), [(-20, -1), (0, 20), (-3, 3), (-20, 20),
                                 (-1, -1), (0, 0)])

# 05: a single node
write(5, bst_from_sorted([42]), [(42, 42), (0, 41), (43, 100), (0, 100)])

# 06: windows that fall between keys and match nothing
keys = [10, 20, 30, 40, 50]
write(6, bst_from_sorted(keys), [(11, 19), (21, 29), (51, 60), (0, 9),
                                 (10, 50)])

# 07: a right spine, where every query still has to descend the whole way to
#     reach the larger keys
keys = list(range(1, 101))
write(7, spine(keys), [(90, 100), (1, 10), (45, 55), (1, 100)])

# 08: keys at the ends of their range
keys = [-VMAX, -1, 0, 1, VMAX]
write(8, bst_from_sorted(keys), [(-VMAX, VMAX), (-1, 1), (0, VMAX),
                                 (-VMAX, -1)])

# ------------------------------------------------------------------ maximum

# 09: a balanced tree at the full node count with narrow windows. A full
#     traversal costs 200,000 per query and there are 200,000 queries.
keys = sorted(random.sample(range(-VMAX, VMAX), NMAX))
t = bst_from_sorted(keys)
write(9, t, narrow_queries(keys, QMAX, 3))

# 10: the same tree, windows of about 50 keys
write(10, t, narrow_queries(keys, QMAX // 2, 50))

# 11: the same tree, windows that match nothing at all -- the cheapest
#     possible answer with pruning, and still a full traversal without it
qs = []
for _ in range(QMAX):
    i = random.randrange(len(keys) - 1)
    lo, hi = keys[i] + 1, keys[i + 1] - 1
    if lo > hi:
        lo = hi = keys[i]
    qs.append((lo, hi))
write(11, t, qs)

# 12: a deep tree at the height cap, with narrow windows.
#     Q is 20,000 here rather than the full 200,000. On a spine every query
#     costs the height whatever it does, so 200,000 queries against a
#     5,000-deep tree is 10^9 steps for the CORRECT solution too -- it ran at
#     3.45 s. The point of this case is the depth, not the query count.
keys = sorted(random.sample(range(-VMAX, VMAX), HMAX))
write(12, spine(keys), narrow_queries(keys, 20_000, 3))

# 13: the full node count with keys near the top of the range, so the totals
#     are largest -- a whole-tree query is about 10^14
keys = sorted(random.sample(range(VMAX - 5 * NMAX, VMAX), NMAX))
t = bst_from_sorted(keys)
qs = narrow_queries(keys, QMAX - 3, 5)
qs += [(keys[0], keys[-1]), (keys[0], keys[NMAX // 2]), (keys[NMAX // 2], keys[-1])]
write(13, t, qs)

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open("%s/output%02d.txt" % (OUT, i)) as f:
        vals = [int(x) for x in f.read().split()]
    print("  case %02d: Q = %-7d largest answer %18d  in %8d B"
          % (i, len(vals), max(vals), os.path.getsize(ipath)))
