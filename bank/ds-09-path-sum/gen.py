#!/usr/bin/env python3
"""Test case generator for ds-09-path-sum.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What the cases are built to catch
---------------------------------
  1. Returning true at a missing child. The tempting base case is "target
     reached zero, so yes", and it lets a path stop at a node that still has
     one child. Case 02 is built entirely of one-sided nodes whose partial
     sums hit the target, so that mistake says true where the answer is false.

  2. Testing `target == 0` at the leaf instead of `target == node.data`. The
     two agree only if the subtraction is done before the test rather than
     after, and mixing the two conventions is the usual slip.

  3. Pruning a branch once the remainder goes negative. That is valid only for
     positive values, and values here go down to -1,000. Case 03 has paths
     whose running total dips below zero and comes back.

  4. Answering with the total of the whole subtree rather than of one path.

Targets are chosen half from sums that exist and half from sums that do not,
so a solution that always answers one way scores about half.

Every file is ASCII with LF line endings.
"""
import random
import os
from collections import deque

random.seed(20260905)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000                 # node values, negative allowed
TARGET_LIMIT = 5_000_000
NMAX = 100_000
HMAX = 5_000
QMAX = 1_000


class Tree:
    def __init__(self):
        self.value, self.left, self.right = [], [], []

    def add(self, v):
        self.value.append(v)
        self.left.append(-1)
        self.right.append(-1)
        return len(self.value) - 1

    def size(self):
        return len(self.value)


def tokens_of(tree):
    out = [str(tree.value[0])]
    q = deque([0])
    while q:
        i = q.popleft()
        for child in (tree.left[i], tree.right[i]):
            if child == -1:
                out.append("#")
            else:
                out.append(str(tree.value[child]))
                q.append(child)
    while len(out) > 1 and out[-1] == "#":
        out.pop()
    return out


def leaf_sums(tree):
    """Every root-to-leaf sum, iteratively."""
    sums = set()
    stack = [(0, 0)]
    while stack:
        i, acc = stack.pop()
        acc += tree.value[i]
        if tree.left[i] == -1 and tree.right[i] == -1:
            sums.add(acc)
            continue
        for c in (tree.left[i], tree.right[i]):
            if c != -1:
                stack.append((c, acc))
    return sums


def height_of(tree):
    best = 0
    stack = [(0, 1)]
    while stack:
        i, d = stack.pop()
        best = max(best, d)
        for c in (tree.left[i], tree.right[i]):
            if c != -1:
                stack.append((c, d + 1))
    return best


def write(idx, tree, targets):
    assert 1 <= tree.size() <= NMAX, "node count out of range in case %d" % idx
    h = height_of(tree)
    assert h <= HMAX, "height %d exceeds the cap in case %d" % (h, idx)
    assert all(-VMAX <= v <= VMAX for v in tree.value)
    assert 1 <= len(targets) <= QMAX, "Q out of range in case %d" % idx
    assert all(-TARGET_LIMIT <= t <= TARGET_LIMIT for t in targets)
    sums = leaf_sums(tree)
    toks = tokens_of(tree)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(toks))
        f.write(" ".join(toks) + "\n")
        f.write("%d\n" % len(targets))
        f.write(" ".join(map(str, targets)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for t in targets:
            f.write("%s\n" % ("true" if t in sums else "false"))


def mixed_targets(tree, n):
    """Half hits, half misses, shuffled."""
    sums = sorted(leaf_sums(tree))
    out = []
    for i in range(n):
        if i % 2 == 0 and sums:
            out.append(random.choice(sums))
        else:
            miss = set(sums)
            while True:
                t = random.randint(-TARGET_LIMIT, TARGET_LIMIT)
                if t not in miss:
                    out.append(t)
                    break
    random.shuffle(out)
    return out


def from_shape(pairs, values):
    t = Tree()
    for v in values:
        t.add(v)
    for i, (l, r) in enumerate(pairs):
        t.left[i], t.right[i] = l, r
    return t


def random_tree(n, max_height=HMAX, lo=-VMAX, hi=VMAX):
    t = Tree()
    t.add(random.randint(lo, hi))
    depth, open_slots = [1], [0]
    for _ in range(n - 1):
        while True:
            k = random.randrange(len(open_slots))
            parent = open_slots[k]
            if depth[parent] + 1 <= max_height:
                break
            open_slots.pop(k)
            if not open_slots:
                return t
        child = t.add(random.randint(lo, hi))
        depth.append(depth[parent] + 1)
        if t.left[parent] == -1 and (t.right[parent] != -1 or random.random() < 0.5):
            t.left[parent] = child
        elif t.right[parent] == -1:
            t.right[parent] = child
        else:
            t.left[parent] = child
        if t.left[parent] != -1 and t.right[parent] != -1:
            open_slots.remove(parent)
        open_slots.append(child)
    return t


def one_sided_chain(values):
    """Every node has exactly one child, so there is exactly one leaf."""
    t = Tree()
    for v in values:
        t.add(v)
    for i in range(len(values) - 1):
        if i % 2 == 0:
            t.left[i] = i + 1
        else:
            t.right[i] = i + 1
    return t


# ---------------------------------------------------------------- hand-built

BOOK = from_shape([(1, 2), (3, 4), (-1, 5), (-1, -1), (-1, -1), (-1, -1)],
                  [5, 3, 8, 1, 4, 9])

# 00 sample: the worked example. Its three path sums are 9, 12 and 22.
write(0, BOOK, [12, 10, 9, 22, 13])

# 01 sample: a single node, which is itself a leaf
write(1, from_shape([(-1, -1)], [7]), [7, 0, -7, 6, 8])

# 02 sample: a chain of one-sided nodes, so there is exactly ONE leaf and one
#            path sum. The targets include every PARTIAL sum along the way --
#            1, 3, 6, 10 -- which are reachable only by stopping early. Only
#            the full sum, 15, is true.
#            A solution that answers true at a missing child says true to all
#            of them.
write(2, one_sided_chain([1, 2, 3, 4, 5]), [1, 3, 6, 10, 15, 14, 16])

# 03: negative values, so the running total falls and rises again. A solution
#     that abandons a branch once the remainder goes negative misses these.
write(3, from_shape([(1, 2), (3, -1), (-1, 4), (-1, -1), (-1, -1)],
                    [10, -20, -30, 25, 40]), [15, 20, -10, 0, 5])

# 04: every value zero, so every path sums to zero
write(4, from_shape([(1, 2), (3, 4), (-1, -1), (-1, -1), (-1, -1)],
                    [0, 0, 0, 0, 0]), [0, 1, -1])

# 05: two paths with the same sum by different routes
write(5, from_shape([(1, 2), (3, -1), (4, -1), (-1, -1), (-1, -1)],
                    [1, 2, 3, 4, 3]), [7, 6, 5, 4])

# 06: a left spine, one path only
t = one_sided_chain(list(range(1, 21)))
write(6, t, sorted(leaf_sums(t)) + [0, 1, 209, 211])

# 07: values at the ends of their range along a deep-ish path
write(7, from_shape([(1, 2), (3, -1), (-1, 4), (-1, -1), (-1, -1)],
                    [1000, -1000, 1000, 1000, -1000]), [1000, 0, 2000, -1000])

# 08: a small random tree with a full spread of targets
t = random_tree(200, max_height=20)
write(8, t, mixed_targets(t, 200))

# ------------------------------------------------------------------ maximum

# 09: full node count, shallow, targets half hits and half misses
t = random_tree(NMAX, max_height=40)
write(9, t, mixed_targets(t, QMAX))

# 10: full node count, all values positive, so a prune-on-negative solution is
#     correct here -- which is what keeps that mistake partial
t = random_tree(NMAX, max_height=40, lo=1, hi=VMAX)
write(10, t, mixed_targets(t, QMAX))

# 11: full node count, all values negative
t = random_tree(NMAX, max_height=40, lo=-VMAX, hi=-1)
write(11, t, mixed_targets(t, QMAX))

# 12: a chain at the height cap: one leaf, one path sum, and every partial sum
#     along it is a tempting wrong answer
t = one_sided_chain([random.randint(-VMAX, VMAX) for _ in range(HMAX)])
sums = sorted(leaf_sums(t))
partials = []
acc = 0
node = 0
while node != -1:
    acc += t.value[node]
    partials.append(acc)
    node = t.left[node] if t.left[node] != -1 else t.right[node]
targets = [sums[0]] + random.sample(partials[:-1], min(QMAX - 1, len(partials) - 1))
write(12, t, targets)

# 13: full node count at a greater height, targets drawn from real path sums
t = random_tree(NMAX, max_height=HMAX)
write(13, t, mixed_targets(t, QMAX))

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open("%s/output%02d.txt" % (OUT, i)) as f:
        answers = f.read().split()
    trues = answers.count("true")
    print("  case %02d: Q = %-5d true %5d / %-5d  in %8d B"
          % (i, len(answers), trues, len(answers), os.path.getsize(ipath)))
