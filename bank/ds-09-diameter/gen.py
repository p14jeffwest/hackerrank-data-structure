#!/usr/bin/env python3
"""Test case generator for ds-09-diameter.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What the cases are built to catch
---------------------------------
  1. The quadratic version: at every node, call height(left) + height(right)
     and take the largest. It is correct and it recomputes every height once
     per ancestor. On a skewed tree that is 100,000 walks of up to 100,000
     nodes. Cases 09 through 13 are large enough to time out; the small ones
     are not, so the mistake shows as a partial score.

  2. Assuming the longest path runs through the root. Case 02 is a tree whose
     diameter lies entirely inside one subtree, so a root-only answer is short
     by a wide margin.

  3. Counting nodes rather than edges. The book defines the diameter in EDGES,
     and 9.5 measures depth in NODES a page later, so the confusion is
     supplied by the material itself. Case 01 is a single node, where the
     answer is 0 and a node count gives 1.

  4. Forgetting that a one-sided node still has a path through it. With an
     empty subtree reporting -1, the arithmetic works out on its own; with 0
     it does not.

The height cap of 5,000 is inherited from ds-09-traversal, for the same
reason: the solution is recursive and the stack depth is the tree's height.

Every file is ASCII with LF line endings.
"""
import random
import os
from collections import deque

random.seed(20260904)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
NMAX = 500_000
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


def post_order(tree):
    """Node indices, children before parents, without recursion."""
    order, stack = [], [0]
    while stack:
        i = stack.pop()
        order.append(i)
        for c in (tree.left[i], tree.right[i]):
            if c != -1:
                stack.append(c)
    order.reverse()
    return order


def measure(tree):
    """Height in edges (empty = -1) and the diameter in edges."""
    n = tree.size()
    h = [-1] * n
    best = 0
    for i in post_order(tree):
        lh = h[tree.left[i]] if tree.left[i] != -1 else -1
        rh = h[tree.right[i]] if tree.right[i] != -1 else -1
        best = max(best, lh + rh + 2)
        h[i] = 1 + max(lh, rh)
    return h[0], best


def write(idx, tree):
    assert 1 <= tree.size() <= NMAX, "node count out of range in case %d" % idx
    height, diameter = measure(tree)
    assert height + 1 <= HMAX, \
        "height %d exceeds the cap in case %d" % (height + 1, idx)
    assert 0 <= diameter <= 2 * height, "diameter out of range in case %d" % idx
    assert all(-VMAX <= v <= VMAX for v in tree.value)
    toks = tokens_of(tree)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(toks))
        f.write(" ".join(toks) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("%d\n" % diameter)


def from_shape(pairs, values):
    t = Tree()
    for v in values:
        t.add(v)
    for i, (l, r) in enumerate(pairs):
        t.left[i], t.right[i] = l, r
    return t


def complete(n):
    t = Tree()
    for _ in range(n):
        t.add(random.randint(-VMAX, VMAX))
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


def two_spines(total, height):
    """A root whose LEFT subtree holds two long spines and whose right is a
    single node. The diameter runs between the two spine tips and never comes
    near the root, which is what a root-only answer misses."""
    t = Tree()
    root = t.add(random.randint(-VMAX, VMAX))
    hub = t.add(random.randint(-VMAX, VMAX))
    t.left[root] = hub
    t.right[root] = t.add(random.randint(-VMAX, VMAX))
    arm = (height - 2)
    for side in ("left", "right"):
        prev = hub
        for _ in range(arm):
            if t.size() >= total:
                break
            node = t.add(random.randint(-VMAX, VMAX))
            if side == "left":
                t.left[prev] = node
            else:
                t.right[prev] = node
            prev = node
            side = "left"          # continue straight down after the first step
    return t


def random_tree(n, max_height=HMAX):
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


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's example. Diameter 3, along 4-2-1-3.
write(0, from_shape([(1, 2), (3, 4), (-1, -1), (-1, -1), (-1, -1)],
                    [1, 2, 3, 4, 5]))

# 01 sample: a single node. The diameter is 0 -- counting NODES would give 1.
write(1, from_shape([(-1, -1)], [7]))

# 02 sample: the longest path does not touch the root. The root's right side
#            is one node; its left side holds a V whose two arms are long.
#            A solution that only measures through the root answers 4 instead
#            of 6.
#                     1
#                    / \
#                   2   9
#                  / \
#                 3   6
#                /     \
#               4       7
#              /         \
#             5           8
write(2, from_shape([(1, 8), (2, 5), (3, -1), (4, -1), (-1, -1),
                     (-1, 6), (-1, 7), (-1, -1), (-1, -1)],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 03: the book's skewed example, 1->(2->(3), null), diameter 2
write(3, from_shape([(1, -1), (2, -1), (-1, -1)], [1, 2, 3]))

# 04: two nodes, each way round. Diameter 1.
write(4, from_shape([(1, -1), (-1, -1)], [1, 2]))
write(5, from_shape([(-1, 1), (-1, -1)], [1, 2]))

# 06: a perfect tree of 15 nodes. Height 3, so the diameter is 6, through the
#     root.
write(6, complete(15))

# 07: one-sided nodes all the way down one arm, so the empty-subtree value
#     has to be right for the arithmetic to work
write(7, from_shape([(1, 4), (2, -1), (3, -1), (-1, -1), (5, -1),
                     (-1, -1)],
                    [1, 2, 3, 4, 5, 6]))

# 08: a small V hanging off a long spine, so the diameter is set deep down
write(8, two_spines(40, 18))

# ------------------------------------------------------------------ maximum

# 09: a left spine at the height cap. The diameter is the spine itself, and
#     this is the worst case for the quadratic version: every height call
#     walks the rest of the spine.
write(9, skewed(HMAX, "left"))

# 10: a right spine at the height cap
write(10, skewed(HMAX, "right"))

# 11: a complete tree at the full node count. Shallow, so the quadratic
#     version survives it -- which is what keeps that mistake partial.
write(11, complete(NMAX))

# 12: two long arms meeting well below the root, at the full node count
write(12, two_spines(NMAX, HMAX - 1))

# 13: a caterpillar with bushes -- the case the quadratic version cannot
#     afford. A spine of 4,900 nodes, each carrying a small SHALLOW bush on
#     its right, filling the tree to the full node count while the height
#     stays just under the cap.
#
#     The shape matters more than the size. Cases 09 and 10 are deep but
#     small, and case 11 is large but shallow; the quadratic version survives
#     both, because its cost is roughly (number of nodes) x (height) and each
#     of those cases keeps one factor down. Only a tree that is large AND
#     deep at once pays the full bill.
t = Tree()
t.add(random.randint(-VMAX, VMAX))
spine = [0]
for _ in range(4899):
    c = t.add(random.randint(-VMAX, VMAX))
    t.left[spine[-1]] = c
    spine.append(c)
BUSH = (NMAX - len(spine)) // len(spine)     # fill to NMAX, whatever NMAX is
for s_node in spine:
    if t.size() >= NMAX:
        break
    r = t.add(random.randint(-VMAX, VMAX))
    t.right[s_node] = r
    bush = deque([r])
    grown = 1
    while bush and t.size() < NMAX and grown < BUSH:
        node = bush.popleft()
        for side in ("left", "right"):
            if t.size() >= NMAX or grown >= BUSH:
                break
            c = t.add(random.randint(-VMAX, VMAX))
            if side == "left":
                t.left[node] = c
            else:
                t.right[node] = c
            bush.append(c)
            grown += 1
write(13, t)

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open(ipath) as f:
        m = int(f.readline())
    with open("%s/output%02d.txt" % (OUT, i)) as f:
        d = int(f.readline())
    print("  case %02d: tokens %7d  diameter %5d  in %8d B"
          % (i, m, d, os.path.getsize(ipath)))
