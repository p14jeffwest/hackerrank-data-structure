#!/usr/bin/env python3
"""Test case generator for ds-10-validate.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What the cases are built to catch
---------------------------------
  1. Comparing a node only against its parent. This is the mistake the book
     raises twice -- in 10.1 item 2 and again in its Check Your Understanding
     -- and it accepts trees where a node is a legal child of its parent and
     still sits on the wrong side of an ancestor. Case 02 is nothing but such
     trees, and it is published as a sample.

  2. Bounds held in int. Keys go all the way to Integer.MIN_VALUE and
     Integer.MAX_VALUE, so there is no int value left to mean "no bound yet":
     a root of Integer.MIN_VALUE is rejected by its own starting bound. Case
     03 is built from those two values.

  3. Allowing equality. The rule is strict on both sides; a duplicate key
     anywhere makes the tree invalid. Case 04 places duplicates at a parent
     and a child, and at two nodes far apart.

  4. Checking the inorder traversal is sorted but with `<=` rather than `<`,
     which is the same equality mistake in a different disguise. That approach
     is otherwise correct and welcome.

Roughly half the trees in every random case are valid, so a solution that
always answers one way scores about half.

Every file is ASCII with LF line endings.
"""
import random
import os
from collections import deque

random.seed(20261002)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

INT_MIN, INT_MAX = -2**31, 2**31 - 1
NMAX = 100_000
HMAX = 5_000
TOTAL = 200_000            # sum of node counts over all trees in one case


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


def tokens_of(tree):
    out = [str(tree.key[0])]
    q = deque([0])
    while q:
        i = q.popleft()
        for c in (tree.left[i], tree.right[i]):
            if c == -1:
                out.append("#")
            else:
                out.append(str(tree.key[c]))
                q.append(c)
    while len(out) > 1 and out[-1] == "#":
        out.pop()
    return out


def is_valid(tree):
    """The range check, iteratively."""
    stack = [(0, None, None)]
    while stack:
        i, low, high = stack.pop()
        if i == -1:
            continue
        k = tree.key[i]
        if low is not None and k <= low:
            return False
        if high is not None and k >= high:
            return False
        stack.append((tree.left[i], low, k))
        stack.append((tree.right[i], k, high))
    return True


def height_of(tree):
    best, stack = 0, [(0, 1)]
    while stack:
        i, d = stack.pop()
        best = max(best, d)
        for c in (tree.left[i], tree.right[i]):
            if c != -1:
                stack.append((c, d + 1))
    return best


def write(idx, trees):
    total = sum(t.size() for t in trees)
    assert 1 <= len(trees) <= 500, "T out of range in case %d" % idx
    assert total <= TOTAL, "node total %d exceeds the limit in case %d" % (total, idx)
    for t in trees:
        assert 1 <= t.size() <= NMAX
        assert height_of(t) <= HMAX, "height cap broken in case %d" % idx
        assert all(INT_MIN <= k <= INT_MAX for k in t.key)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(trees))
        for t in trees:
            toks = tokens_of(t)
            f.write("%d\n" % len(toks))
            f.write(" ".join(toks) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for t in trees:
            f.write("%s\n" % ("true" if is_valid(t) else "false"))


def from_shape(pairs, keys):
    t = Tree()
    for k in keys:
        t.add(k)
    for i, (l, r) in enumerate(pairs):
        t.left[i], t.right[i] = l, r
    return t


def bst_from_sorted(keys, max_height=HMAX):
    """A balanced BST over the given sorted keys, built iteratively."""
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


def break_one(tree, rng):
    """Raise one key so that it violates an ancestor and NOTHING ELSE.

    The victim is the RIGHTMOST node of some node's left subtree. Raising its
    key keeps it above its own parent (it is that parent's right child) and
    above its own left child, so every parent-child pair in the tree still
    obeys the rule. Only the ancestor's bound is broken.

    An earlier version picked an arbitrary node in the left subtree and raised
    it. That node had children of its own, and raising it above them made the
    tree locally inconsistent too -- which a parent-only check detects, so the
    case stopped testing what it was for.
    """
    for i in range(tree.size()):
        l = tree.left[i]
        if l == -1:
            continue
        victim = l
        while tree.right[victim] != -1:      # rightmost of the left subtree
            victim = tree.right[victim]
        if victim == l and tree.left[i] == l and tree.right[l] == -1:
            pass                              # still fine: l is its own rightmost
        tree.key[victim] = tree.key[i] + rng.randint(1, 1000)
        return True
    for i in range(tree.size()):
        r = tree.right[i]
        if r == -1:
            continue
        victim = r
        while tree.left[victim] != -1:
            victim = tree.left[victim]
        tree.key[victim] = tree.key[i] - rng.randint(1, 1000)
        return True
    return False


def random_valid(n, spread=10**6):
    keys = sorted(random.sample(range(-spread, spread), n))
    return bst_from_sorted(keys)


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's two examples from 10.6 Problem 1
write(0, [
    from_shape([(1, 2), (-1, -1), (-1, -1)], [2, 1, 3]),
    from_shape([(1, 2), (-1, -1), (3, 4), (-1, -1), (-1, -1)], [5, 1, 4, 3, 6]),
])

# 01 sample: the smallest shapes, plus the ends of the int range.
#            INT_MIN as a root is the case an int-based bound cannot express:
#            there is no int below it to use as "no bound yet".
write(1, [
    from_shape([(-1, -1)], [42]),
    from_shape([(1, -1), (-1, -1)], [5, 3]),
    from_shape([(-1, 1), (-1, -1)], [5, 7]),
    from_shape([(1, -1), (-1, -1)], [5, 7]),      # invalid: larger on the left
    from_shape([(-1, -1)], [INT_MIN]),
    from_shape([(-1, -1)], [INT_MAX]),
    from_shape([(1, 2), (-1, -1), (-1, -1)], [0, INT_MIN, INT_MAX]),
])

# 02 sample: every tree here is locally consistent -- each node obeys the rule
#            against its own parent -- and every one of them is invalid,
#            because a node sits on the wrong side of a GRANDPARENT.
#            The book raises this twice, in 10.1 item 2 and again in its
#            Check Your Understanding.
write(2, [
    # 10.1 item 2: 25's left child 2 is smaller than the root 10
    from_shape([(1, 2), (-1, -1), (3, 4), (-1, -1), (-1, -1)], [10, 5, 25, 2, 45]),
    # 10.1 Check Your Understanding: 10's right child 25 exceeds the root 20
    from_shape([(1, 2), (3, 4), (-1, -1), (-1, -1), (-1, -1)], [20, 10, 30, 5, 25]),
    # the mirror of the first
    from_shape([(1, 2), (3, 4), (-1, -1), (-1, -1), (-1, -1)], [50, 25, 75, 10, 80]),
])

# 03: keys at the ends of the int range, where an int-based bound has no
#     value left to mean "no bound yet"
write(3, [
    from_shape([(-1, -1)], [INT_MIN]),
    from_shape([(-1, -1)], [INT_MAX]),
    from_shape([(1, 2), (-1, -1), (-1, -1)], [0, INT_MIN, INT_MAX]),
    from_shape([(1, -1), (-1, -1)], [INT_MIN, INT_MIN]),        # invalid: equal
    from_shape([(-1, 1), (-1, -1)], [INT_MAX, INT_MAX]),        # invalid: equal
])

# 04: duplicates, which the strict rule forbids
write(4, [
    from_shape([(1, -1), (-1, -1)], [7, 7]),
    from_shape([(-1, 1), (-1, -1)], [7, 7]),
    from_shape([(1, 2), (-1, -1), (-1, -1)], [5, 3, 5]),
    from_shape([(1, 2), (3, -1), (-1, -1), (-1, -1)], [10, 5, 15, 10]),
    from_shape([(1, 2), (-1, -1), (-1, -1)], [5, 3, 7]),        # valid, for contrast
])

# 05: a left spine and a right spine, both valid
write(5, [
    from_shape([(i + 1, -1) for i in range(29)] + [(-1, -1)],
               list(range(30, 0, -1))),
    from_shape([(-1, i + 1) for i in range(29)] + [(-1, -1)],
               list(range(1, 31))),
])

# 06: a valid BST with one key changed so that it breaks only against an
#     ancestor, mixed with the untouched original
t = random_valid(60)
u = random_valid(60)
break_one(u, random)
write(6, [t, u])

# 07: trees that are valid except at the very deepest node
t = bst_from_sorted(list(range(1, 64)))
u = bst_from_sorted(list(range(1, 64)))
u.key[u.size() - 1] = -1                     # a deep leaf made too small
write(7, [t, u])

# 08: many small trees, half valid
trees = []
for i in range(200):
    t = random_valid(random.randint(1, 15))
    if i % 2 == 1 and not break_one(t, random):
        t.key[0] = t.key[0]                  # too small to break; leave valid
    trees.append(t)
write(8, trees)

# ------------------------------------------------------------------ maximum

# 09: one large valid BST
write(9, [random_valid(NMAX)])

# 10: one large BST with a single key changed deep inside
t = random_valid(NMAX)
break_one(t, random)
write(10, [t])

# 11: T at its maximum, alternating valid and broken
trees = []
budget = TOTAL
for i in range(500):
    n = max(1, min(budget - (500 - i - 1), random.randint(1, 800)))
    budget -= n
    t = random_valid(n)
    if i % 2 == 1:
        break_one(t, random)
    trees.append(t)
write(11, trees)

# 12: a deep valid BST -- a spine at the height cap -- and the same spine with
#     one key changed
keys = list(range(1, HMAX + 1))
t = Tree()
t.add(keys[0])
for i in range(1, len(keys)):
    c = t.add(keys[i])
    t.right[i - 1] = c
u = Tree()
u.add(keys[0])
for i in range(1, len(keys)):
    c = u.add(keys[i])
    u.right[i - 1] = c
u.key[u.size() - 1] = 0                      # the deepest node, far too small
write(12, [t, u])

# 13: two large trees whose keys span the whole int range
big = sorted(random.sample(range(INT_MIN, INT_MAX), 50_000))
t = bst_from_sorted(big)
u = bst_from_sorted(big)
break_one(u, random)
write(13, [t, u])

print("generated 14 cases")
for i in range(14):
    with open("%s/output%02d.txt" % (OUT, i)) as f:
        ans = f.read().split()
    with open("%s/input%02d.txt" % (IN, i)) as f:
        t = int(f.readline())
    print("  case %02d: T = %-5d true %4d / %-4d  in %8d B"
          % (i, t, ans.count("true"), len(ans),
             os.path.getsize("%s/input%02d.txt" % (IN, i))))
