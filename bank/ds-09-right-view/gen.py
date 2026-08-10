#!/usr/bin/env python3
"""Test case generator for ds-09-right-view.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What the cases are built to catch
---------------------------------
  1. Walking down the right children only. That is the shape most students
     picture, and it is wrong the moment a right child is missing while a left
     one is not. Case 02 is the book's own left-leaning example, where every
     visible node is a LEFT child.

  2. Level-order without separating the levels -- no `levelSize` -- so the
     result is either the whole traversal or only its last node. Case 01 is a
     single node, where those two happen to be right, which keeps the mistake
     partial.

  3. Taking the FIRST node of each level instead of the last, which is the
     left side view. Case 03 is a tree symmetric in shape but not in value, so
     the two views differ everywhere.

  4. Recursion. A depth-first solution that visits right before left and
     records the first node seen at each new depth is correct and welcome;
     one that records the LAST is the left view. Both are covered by the cases
     above.

The height cap of 5,000 is inherited from ds-09-traversal. It matters less
here -- the reference solution is iterative -- but a recursive solution is a
legitimate answer and the cap keeps it safe.

Every file is ASCII with LF line endings.
"""
import random
import os
from collections import deque

random.seed(20260903)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
NMAX = 100_000
HMAX = 5_000


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


def right_view(tree):
    out = []
    q = deque([0])
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i == size - 1:
                out.append(tree.value[node])
            if tree.left[node] != -1:
                q.append(tree.left[node])
            if tree.right[node] != -1:
                q.append(tree.right[node])
    return out


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


def write(idx, tree):
    assert 1 <= tree.size() <= NMAX, "node count out of range in case %d" % idx
    h = height_of(tree)
    assert h <= HMAX, "height %d exceeds the cap in case %d" % (h, idx)
    assert all(-VMAX <= v <= VMAX for v in tree.value)
    view = right_view(tree)
    assert len(view) == h, "the view must have one entry per level"
    toks = tokens_of(tree)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(toks))
        f.write(" ".join(toks) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write(" ".join(map(str, view)) + "\n")


def from_shape(pairs, values):
    t = Tree()
    for v in values:
        t.add(v)
    for i, (l, r) in enumerate(pairs):
        t.left[i], t.right[i] = l, r
    return t


def complete(n, values=None):
    t = Tree()
    for i in range(n):
        t.add(values[i] if values else random.randint(-VMAX, VMAX))
    for i in range(n):
        if 2 * i + 1 < n:
            t.left[i] = 2 * i + 1
        if 2 * i + 2 < n:
            t.right[i] = 2 * i + 2
    return t


def skewed(n, direction):
    t = Tree()
    for _ in range(n):
        t.add(random.randint(-VMAX, VMAX))
    for i in range(n - 1):
        if direction == "left":
            t.left[i] = i + 1
        else:
            t.right[i] = i + 1
    return t


def random_tree(n, max_height=HMAX, left_bias=0.5):
    t = Tree()
    t.add(random.randint(-VMAX, VMAX))
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
        child = t.add(random.randint(-VMAX, VMAX))
        depth.append(depth[parent] + 1)
        if t.left[parent] == -1 and (t.right[parent] != -1
                                     or random.random() < left_bias):
            t.left[parent] = child
        elif t.right[parent] == -1:
            t.right[parent] = child
        else:
            t.left[parent] = child
        if t.left[parent] != -1 and t.right[parent] != -1:
            open_slots.remove(parent)
        open_slots.append(child)
    return t


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's first example. View is 1, 3, 4.
#            Note that 5 is invisible: it is at the same level as 4 but to
#            its left.
write(0, from_shape([(1, 2), (-1, 3), (-1, 4), (-1, -1), (-1, -1)],
                    [1, 2, 3, 5, 4]))

# 01 sample: a single node, and a two-node tree each way round
write(1, from_shape([(-1, -1)], [42]))

# 02 sample: the book's second example -- a tree that leans LEFT. Every
#            visible node is a left child, so walking down the right children
#            reports only the root.
write(2, from_shape([(1, -1), (2, -1), (-1, -1)], [1, 2, 3]))

# 03: a shape that is symmetric but whose values are not, so the right view
#     and the left view differ at every level
write(3, complete(7, [1, 2, 3, 4, 5, 6, 7]))

# 04: right children missing at alternate levels, so the visible node keeps
#     switching sides
write(4, from_shape([(1, 2), (3, -1), (-1, 4), (-1, 5), (6, -1),
                     (-1, -1), (-1, -1)],
                    [10, 20, 30, 40, 50, 60, 70]))

# 05: a left spine and a right spine of the same length. Both views are the
#     whole tree, but only one of them is reachable by following right links.
write(5, skewed(30, "left"))
write(6, skewed(30, "right"))

# 07: one deep left branch beside a shallow right one, so the lower levels are
#     supplied entirely by the left side
write(7, from_shape([(1, 6), (2, -1), (3, -1), (4, -1), (5, -1),
                     (-1, -1), (-1, -1)],
                    [1, 2, 3, 4, 5, 6, 7]))

# 08: negative values and repeats
write(8, from_shape([(1, 2), (-1, 3), (4, -1), (-1, -1), (-1, -1)],
                    [-5, 0, -5, 1000000000, -1000000000]))

# ------------------------------------------------------------------ maximum

# 09: a complete tree at the full node count. The last level holds 50,000
#     nodes, so the queue is at its widest -- the case that punishes anything
#     holding more than one level at a time.
write(9, complete(NMAX))

# 10: a random tree at the full node count
write(10, random_tree(NMAX))

# 11: a random tree biased hard to the LEFT, so most visible nodes are left
#     children even though the tree is large and bushy
write(11, random_tree(NMAX, left_bias=0.9))

# 12: a left spine at the height cap: 5,000 levels, one node each, and not one
#     of them reachable by following a right link
write(12, skewed(HMAX, "left"))

# 13: a bushy random tree with the height held to 40
write(13, random_tree(NMAX, max_height=40))

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open("%s/output%02d.txt" % (OUT, i)) as f:
        levels = len(f.readline().split())
    with open(ipath) as f:
        m = int(f.readline())
    print("  case %02d: tokens %7d  levels %5d  in %8d B"
          % (i, m, levels, os.path.getsize(ipath)))
