#!/usr/bin/env python3
"""Test case generator for ds-09-traversal.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

The input format
----------------
A tree is given as a level-order listing with `#` for a missing child. The
children of a missing node are not listed, so the listing is as short as the
tree allows. The same format is used by every chapter 9 problem, and by the
Korean chapter 10 problems, so the parsing only has to be explained once.

The height cap
--------------
Nodes go up to 100,000 but the **height is capped at 5,000**, and that cap is
load-bearing rather than decorative. Three of the four traversals are
recursive, so the stack depth is the tree's height; a fully skewed tree of
100,000 nodes would overflow the Java stack and the correct solution would be
the one that crashed. 5,000 frames is comfortable. Case 11 sits exactly at the
cap.

What the cases are built to catch
---------------------------------
  1. Putting the visit in the wrong place among the three recursive lines.
     Cases 00 and 02 have trees where the three orders differ in every
     position.

  2. Writing levelOrder recursively, or forgetting it is not a DFS at all.
     Case 03 is deliberately a tree where preorder and level-order agree, so
     a student who confuses them passes it and fails everything else.

  3. Missing the null check, which shows on any tree with a one-sided node.

Every file is ASCII with LF line endings.
"""
import random
import os
from collections import deque

random.seed(20260901)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
NMAX = 100_000
HMAX = 5_000


class Tree:
    """A binary tree held as three parallel arrays, so nothing is recursive."""

    def __init__(self):
        self.value = []
        self.left = []
        self.right = []

    def add(self, v):
        self.value.append(v)
        self.left.append(-1)
        self.right.append(-1)
        return len(self.value) - 1

    def size(self):
        return len(self.value)


def tokens_of(tree):
    """The level-order listing with `#`, exactly as the Head parses it."""
    if tree.size() == 0:
        return ["#"]
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
    # trailing '#' tokens carry no information; the Head stops at the end
    while len(out) > 1 and out[-1] == "#":
        out.pop()
    return out


def traversals(tree):
    """preorder, inorder, postorder, level-order -- all without recursion."""
    if tree.size() == 0:
        return [], [], [], []

    pre, ino, post = [], [], []
    # state: (node, stage) with stage 0 = arrive, 1 = between, 2 = leave
    stack = [(0, 0)]
    while stack:
        i, stage = stack.pop()
        if i == -1:
            continue
        if stage == 0:
            pre.append(tree.value[i])
            stack.append((i, 1))
            stack.append((tree.left[i], 0))
        elif stage == 1:
            ino.append(tree.value[i])
            stack.append((i, 2))
            stack.append((tree.right[i], 0))
        else:
            post.append(tree.value[i])

    level = []
    q = deque([0])
    while q:
        i = q.popleft()
        level.append(tree.value[i])
        if tree.left[i] != -1:
            q.append(tree.left[i])
        if tree.right[i] != -1:
            q.append(tree.right[i])

    return pre, ino, post, level


def height_of(tree):
    if tree.size() == 0:
        return 0
    best = 0
    stack = [(0, 1)]
    while stack:
        i, d = stack.pop()
        best = max(best, d)
        for c in (tree.left[i], tree.right[i]):
            if c != -1:
                stack.append((c, d + 1))
    return best


HEIGHTS = {}


def write(idx, tree):
    assert 1 <= tree.size() <= NMAX, "node count out of range in case %d" % idx
    h = height_of(tree)
    assert h <= HMAX, "height %d exceeds the cap in case %d" % (h, idx)
    assert all(-VMAX <= v <= VMAX for v in tree.value)
    HEIGHTS[idx] = h
    toks = tokens_of(tree)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(toks))
        f.write(" ".join(toks) + "\n")
    pre, ino, post, level = traversals(tree)
    assert len(pre) == len(ino) == len(post) == len(level) == tree.size()
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for seq in (pre, ino, post, level):
            f.write(" ".join(map(str, seq)) + "\n")


def from_shape(pairs, values=None):
    """Build from an explicit list of (left, right) index pairs."""
    t = Tree()
    for i, v in enumerate(values if values else range(1, len(pairs) + 1)):
        t.add(v)
    for i, (l, r) in enumerate(pairs):
        t.left[i] = l
        t.right[i] = r
    return t


def complete(n, values=None):
    """A complete binary tree: child indices 2i+1 and 2i+2."""
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
    for i in range(n):
        t.add(random.randint(-VMAX, VMAX))
    for i in range(n - 1):
        if direction == "left":
            t.left[i] = i + 1
        else:
            t.right[i] = i + 1
    return t


def random_tree(n, max_height=HMAX):
    """Attach each new node under a random existing node with a free slot."""
    t = Tree()
    t.add(random.randint(-VMAX, VMAX))
    depth = [1]
    open_slots = [0]
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

# 00 sample: the worked example, whose four traversals all differ
write(0, from_shape([(1, 2), (3, 4), (-1, 5), (-1, -1), (-1, -1), (-1, -1)],
                    [5, 3, 8, 1, 4, 9]))

# 01 sample: a single node, where all four traversals are the same
write(1, from_shape([(-1, -1)], [42]))

# 02 sample: the tree from 9.3's Check Your Understanding
write(2, from_shape([(1, 2), (3, 4), (-1, -1), (-1, -1), (-1, -1)],
                    [1, 2, 3, 4, 5]))

# 03: a tree where preorder and LEVEL-order happen to agree, so confusing the
#     two is not caught here. It is in the set to keep that mistake partial.
write(3, complete(3, [1, 2, 3]))

# 04: one-sided nodes on both sides, which is where a missing null check bites
write(4, from_shape([(1, -1), (-1, 2), (3, -1), (-1, -1)], [1, 2, 3, 4]))

# 05: a left spine and a right spine
write(5, skewed(50, "left"))
write(6, skewed(50, "right"))

# 07: a complete tree of 63 nodes with values 1..63
write(7, complete(63, list(range(1, 64))))

# 08: negative values and repeats
write(8, from_shape([(1, 2), (3, 4), (5, -1), (-1, -1), (-1, -1), (-1, -1)],
                    [-7, 0, -7, 1000000000, -1000000000, 0]))

# ------------------------------------------------------------------ maximum

# 09: a complete tree at the full node count. Its height is about 17, so the
#     recursion is shallow and the queue is wide -- 50,000 nodes at the last
#     level.
write(9, complete(NMAX))

# 10: a random tree at the full node count
write(10, random_tree(NMAX))

# 11: a tree at the height cap. A caterpillar: a spine with the remaining
#     nodes hung off it, so the recursion goes exactly as deep as the
#     constraints allow.
#     The spine is HMAX - 1 nodes, not HMAX: every hanging node sits one level
#     below its spine node, so a spine of 5,000 would make the tree 5,001 tall
#     and break the cap. The generator's assertion caught that.
t = Tree()
t.add(random.randint(-VMAX, VMAX))
spine = [0]
for _ in range(HMAX - 2):
    c = t.add(random.randint(-VMAX, VMAX))
    t.left[spine[-1]] = c
    spine.append(c)
i = 0
while t.size() < NMAX:
    parent = spine[i % len(spine)]
    if t.right[parent] == -1:
        t.right[parent] = t.add(random.randint(-VMAX, VMAX))
    i += 1
    if i > 4 * NMAX:
        break
write(11, t)

# 12: a right spine of 5,000, the mirror of case 11's shape
write(12, skewed(HMAX, "right"))

# 13: a random tree with the height held down to 40, so it is bushy and wide
write(13, random_tree(NMAX, max_height=40))

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open(ipath) as f:
        m = int(f.readline())
    with open("%s/output%02d.txt" % (OUT, i)) as f:
        n = len(f.readline().split())
    print("  case %02d: tokens %7d  nodes %7d  height %5d  in %8d B"
          % (i, m, n, HEIGHTS[i], os.path.getsize(ipath)))
