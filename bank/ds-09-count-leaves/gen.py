#!/usr/bin/env python3
"""Test case generator for ds-09-count-leaves.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Why three answers and not two
-----------------------------
The Korean counterpart asks for the leaf count and the height in EDGES. This
book uses both conventions and says so: 9.1 defines height in edges, 9.5
Problem 1 defines maximum depth in NODES, and the answer page adds "It differs
by 1 from the edge-count height of 9.1, so you should check the problem's
definition."

Asking for both makes that warning something a student has to act on rather
than read past. It also keeps the Korean answer -- the edge count -- present,
so the two courses still share a number.

What the cases are built to catch
---------------------------------
  1. Treating a node with ONE child as a leaf. Case 02 is nothing but
     one-sided nodes, and it is published as a sample.

  2. The empty case of `height`. It has to be -1, not 0, or every height comes
     out one too large. A single-node tree (case 01) shows it at once.

  3. Confusing the two conventions, which shows as the two numbers being equal
     or differing by two rather than exactly one.

The height cap of 5,000 is inherited from ds-09-traversal, and for the same
reason: all three methods are recursive, so the stack depth is the height of
the tree.

Every file is ASCII with LF line endings.
"""
import random
import os
from collections import deque

random.seed(20260902)

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


def measure(tree):
    """Leaves, height in edges, depth in nodes -- all iteratively."""
    n = tree.size()
    leaves = sum(1 for i in range(n)
                 if tree.left[i] == -1 and tree.right[i] == -1)
    best = 0
    stack = [(0, 1)]
    while stack:
        i, d = stack.pop()
        if d > best:
            best = d
        for c in (tree.left[i], tree.right[i]):
            if c != -1:
                stack.append((c, d + 1))
    return leaves, best - 1, best      # edges, nodes


def write(idx, tree):
    assert 1 <= tree.size() <= NMAX, "node count out of range in case %d" % idx
    leaves, h_edges, h_nodes = measure(tree)
    assert h_nodes <= HMAX, "height %d exceeds the cap in case %d" % (h_nodes, idx)
    assert h_nodes - h_edges == 1, "the two conventions must differ by one"
    assert all(-VMAX <= v <= VMAX for v in tree.value)
    toks = tokens_of(tree)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(toks))
        f.write(" ".join(toks) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("%d\n%d\n%d\n" % (leaves, h_edges, h_nodes))


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


def skewed(n, direction="left"):
    t = Tree()
    for _ in range(n):
        t.add(random.randint(-VMAX, VMAX))
    for i in range(n - 1):
        if direction == "left":
            t.left[i] = i + 1
        else:
            t.right[i] = i + 1
    return t


def zigzag(n):
    """Alternating left and right, so every node has exactly one child."""
    t = Tree()
    for _ in range(n):
        t.add(random.randint(-VMAX, VMAX))
    for i in range(n - 1):
        if i % 2 == 0:
            t.left[i] = i + 1
        else:
            t.right[i] = i + 1
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

# 00 sample: the worked example. Leaves 1, 4 and 9; node 8 has a right child
#            so it is not a leaf.
write(0, from_shape([(1, 2), (3, 4), (-1, 5), (-1, -1), (-1, -1), (-1, -1)],
                    [5, 3, 8, 1, 4, 9]))

# 01 sample: a single node. One leaf, height 0 in edges and 1 in nodes --
#            the smallest place the two conventions part company.
write(1, from_shape([(-1, -1)], [42]))

# 02 sample: one-sided nodes with real subtrees hanging below them.
#            A zigzag was tried first and does NOT work: it has exactly one
#            leaf, and a solution that stops at the first one-sided node also
#            reports one, so it passes by accident. Here each one-sided node
#            leads to a subtree with several leaves, so stopping early
#            undercounts.
#                    1
#                   / \
#                  2   5
#                 /     \
#                3       6
#               / \     / \
#              4   7   8   9
write(2, from_shape([(1, 2), (3, -1), (-1, 4), (5, 6), (7, 8),
                     (-1, -1), (-1, -1), (-1, -1), (-1, -1)],
                    [1, 2, 5, 3, 6, 4, 7, 8, 9]))

# 03: the tree from 9.5 Problem 1, whose maximum depth is 3
write(3, from_shape([(1, 2), (-1, -1), (3, 4), (-1, -1), (-1, -1)],
                    [3, 9, 20, 15, 7]))

# 04: a perfect tree of 15 nodes: 8 leaves, height 3, depth 4
write(4, complete(15, list(range(1, 16))))

# 05: two nodes, in each of the two possible shapes
write(5, from_shape([(1, -1), (-1, -1)], [1, 2]))
write(6, from_shape([(-1, 1), (-1, -1)], [1, 2]))

# 07: one deep branch and one shallow one, so the height comes from one side
write(7, from_shape([(1, 5), (2, -1), (3, -1), (4, -1), (-1, -1), (-1, -1)],
                    [1, 2, 3, 4, 5, 6]))

# 08: negative values and repeats, which change nothing but are worth having
write(8, from_shape([(1, 2), (3, -1), (-1, 4), (-1, -1), (-1, -1)],
                    [-7, 0, -7, -1000000000, 1000000000]))

# ------------------------------------------------------------------ maximum

# 09: a perfect-ish complete tree at the full node count -- half the nodes are
#     leaves and the height is about 17
write(9, complete(NMAX))

# 10: a random tree at the full node count
write(10, random_tree(NMAX))

# 11: a left spine at the height cap: exactly one leaf, maximum recursion
write(11, skewed(HMAX, "left"))

# 12: a zigzag at the height cap. Still exactly one leaf, and every node is
#     one-sided, so it is the largest version of the case 02 trap.
write(12, zigzag(HMAX))

# 13: a bushy random tree, height held to 40
write(13, random_tree(NMAX, max_height=40))

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open("%s/output%02d.txt" % (OUT, i)) as f:
        leaves = int(f.readline())
        edges = int(f.readline())
        nodes = int(f.readline())
    print("  case %02d: leaves %6d  height(edges) %5d  depth(nodes) %5d"
          % (i, leaves, edges, nodes))
