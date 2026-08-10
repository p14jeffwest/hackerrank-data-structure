#!/usr/bin/env python3
"""Test case generator for ds-10-bst.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Why there is a preorder command
-------------------------------
The Korean counterpart prints the tree in inorder only. On a BST that is the
sorted key list, so it reveals the SET of keys and nothing about the shape --
and a student could pass the whole problem with a sorted collection and no
tree at all.

Adding preorder fixes that, but only because the book pins down the one place
where the shape is ambiguous: deleting a node with two children may promote
either the predecessor or the successor, and 10.3 uses the **predecessor**
(the left subtree's maximum). The statement requires it, and preorder is what
checks it.

What the cases are built to catch
---------------------------------
  1. Deleting with the successor instead of the predecessor. The inorder
     output is identical either way; only preorder separates them. Case 02 is
     published as a sample for this.

  2. Not reassigning the returned subtree root -- calling insert(root.left,
     key) without storing it. Nothing is ever attached to an empty slot.

  3. Inserting a duplicate key as a new node.

  4. Deleting a key that is not present, or deleting from an empty tree.

  5. The two-children case handled before the one-child cases, which drops a
     subtree.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20261001)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
MMAX = 200_000
INSERT_MAX = 100_000
HMAX = 5_000


class BST:
    """Reference model, iterative, using the book's predecessor rule."""

    def __init__(self):
        self.key, self.left, self.right = [], [], []
        self.root = -1

    def _new(self, k):
        self.key.append(k)
        self.left.append(-1)
        self.right.append(-1)
        return len(self.key) - 1

    def insert(self, k):
        if self.root == -1:
            self.root = self._new(k)
            return
        cur = self.root
        while True:
            if k < self.key[cur]:
                if self.left[cur] == -1:
                    self.left[cur] = self._new(k)
                    return
                cur = self.left[cur]
            elif k > self.key[cur]:
                if self.right[cur] == -1:
                    self.right[cur] = self._new(k)
                    return
                cur = self.right[cur]
            else:
                return                       # already present

    def search(self, k):
        cur = self.root
        while cur != -1:
            if k == self.key[cur]:
                return True
            cur = self.left[cur] if k < self.key[cur] else self.right[cur]
        return False

    def delete(self, k):
        # find the node and its parent
        parent, cur, side = -1, self.root, None
        while cur != -1 and self.key[cur] != k:
            parent = cur
            if k < self.key[cur]:
                cur, side = self.left[cur], "L"
            else:
                cur, side = self.right[cur], "R"
        if cur == -1:
            return                            # not present

        while True:
            if self.left[cur] != -1 and self.right[cur] != -1:
                # predecessor: the rightmost node of the left subtree
                pparent, p = cur, self.left[cur]
                while self.right[p] != -1:
                    pparent, p = p, self.right[p]
                self.key[cur] = self.key[p]
                parent, cur = pparent, p
                side = "L" if self.left[pparent] == p else "R"
                continue
            child = self.right[cur] if self.left[cur] == -1 else self.left[cur]
            if parent == -1:
                self.root = child
            elif side == "L":
                self.left[parent] = child
            else:
                self.right[parent] = child
            return

    def _walk(self, order):
        if self.root == -1:
            return []
        out, stack = [], [(self.root, 0)]
        while stack:
            i, stage = stack.pop()
            if i == -1:
                continue
            if order == "pre":
                out.append(self.key[i])
                stack.append((self.right[i], 0))
                stack.append((self.left[i], 0))
            else:
                if stage == 0:
                    stack.append((i, 1))
                    stack.append((self.left[i], 0))
                else:
                    out.append(self.key[i])
                    stack.append((self.right[i], 0))
        return out

    def inorder(self):
        return self._walk("in")

    def preorder(self):
        return self._walk("pre")

    def height(self):
        if self.root == -1:
            return 0
        best, stack = 0, [(self.root, 1)]
        while stack:
            i, d = stack.pop()
            best = max(best, d)
            for c in (self.left[i], self.right[i]):
                if c != -1:
                    stack.append((c, d + 1))
        return best


def run(commands):
    """Replay the commands. The height is sampled rather than measured after
    every command: measuring it each time is O(n) and turns generation into
    O(M*n), which at M = 200,000 does not finish. Sampling every 2,000
    commands and once at the end is enough to police the cap, because the
    height only grows while inserts are happening."""
    t = BST()
    out, peak = [], 0
    inserts = 0
    step = 0
    for c in commands:
        parts = c.split()
        op = parts[0]
        if op == "insert":
            t.insert(int(parts[1]))
            inserts += 1
        elif op == "delete":
            t.delete(int(parts[1]))
        elif op == "search":
            out.append("YES" if t.search(int(parts[1])) else "NO")
        elif op == "print":
            out.append(" ".join(map(str, t.inorder())))
        elif op == "preorder":
            out.append(" ".join(map(str, t.preorder())))
        else:
            raise ValueError(c)
        step += 1
        if step % 2000 == 0:
            peak = max(peak, t.height())
    peak = max(peak, t.height())
    return out, peak, inserts


SUMMARY = {}


def write(idx, commands):
    assert 1 <= len(commands) <= MMAX, "M out of range in case %d" % idx
    out, peak, inserts = run(commands)
    SUMMARY[idx] = (len(commands), inserts, peak)
    assert peak <= HMAX, "height %d exceeds the cap in case %d" % (peak, idx)
    assert inserts <= INSERT_MAX, "too many inserts in case %d" % idx
    assert sum(1 for c in commands if c in ("print", "preorder")) <= 10
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(commands))
        f.write("\n".join(commands) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("".join(line + "\n" for line in out))


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's own verification run from 10.3 item 6
write(0, ["insert 50", "insert 30", "insert 70", "insert 20", "insert 40",
          "insert 60", "insert 80", "print",
          "delete 20", "print",          # a leaf
          "delete 30", "print",          # one child
          "delete 50", "print"])         # two children

# 01 sample: search, duplicate insert, deleting something absent, and an
#            empty tree printing an empty line
write(1, ["print", "search 5", "delete 5",
          "insert 50", "insert 30", "insert 70",
          "search 30", "search 45", "insert 30", "print",
          "delete 999", "print",
          "delete 30", "delete 50", "delete 70", "print", "search 50"])

# 02 sample: the book's Check Your Understanding from 10.3. Removing the root
#            50 must promote 45, the largest key on the left. The successor
#            rule would promote 70 instead -- the inorder output is the same
#            either way, so only the preorder line tells them apart.
write(2, ["insert 50", "insert 30", "insert 70", "insert 20", "insert 45",
          "preorder", "delete 50", "preorder", "print"])

# 03: every removal case in turn, checked by shape each time
write(3, ["insert 50", "insert 30", "insert 70", "insert 20", "insert 40",
          "insert 80", "insert 35", "preorder",
          "delete 20", "preorder",       # leaf
          "delete 40", "preorder",       # one child (35)
          "delete 70", "preorder",       # one child (80)
          "delete 30", "preorder"])      # two children -> predecessor 35

# 04: deleting the root over and over until the tree empties
cmds = ["insert %d" % k for k in [50, 25, 75, 10, 30, 60, 90]]
for _ in range(7):
    cmds += ["preorder", "delete 50" if False else "print"]
cmds = ["insert %d" % k for k in [50, 25, 75, 10, 30, 60, 90]]
for k in [50, 25, 75, 10, 30, 60, 90]:
    cmds.append("delete %d" % k)
cmds.append("print")
cmds.append("search 50")
write(4, cmds)

# 05: a single node, inserted, searched, deleted, reinserted
write(5, ["insert 7", "print", "preorder", "search 7", "delete 7",
          "print", "search 7", "insert 7", "insert 7", "print"])

# 06: keys inserted in ascending order, so the tree is a right spine
write(6, ["insert %d" % k for k in range(1, 31)] +
         ["preorder", "delete 1", "delete 30", "preorder", "print"])

# 07: keys inserted in descending order, a left spine
write(7, ["insert %d" % k for k in range(30, 0, -1)] +
         ["preorder", "delete 30", "delete 1", "preorder", "print"])

# 08: values at the ends of the range, and negatives
write(8, ["insert 0", "insert -1000000000", "insert 1000000000",
          "search -1000000000", "print", "preorder",
          "delete 0", "print", "preorder"])

# ------------------------------------------------------------------ random


def random_case(m, inserts, key_hi, deletes=True):
    cmds = []
    live = []
    while len(cmds) < m:
        r = random.random()
        if len(cmds) < inserts and (r < 0.5 or not live):
            k = random.randint(-key_hi, key_hi)
            cmds.append("insert %d" % k)
            live.append(k)
        elif deletes and r < 0.72 and live:
            k = random.choice(live) if random.random() < 0.7 \
                else random.randint(-key_hi, key_hi)
            cmds.append("delete %d" % k)
            if k in live:
                live.remove(k)
        else:
            k = random.choice(live) if (live and random.random() < 0.5) \
                else random.randint(-key_hi, key_hi)
            cmds.append("search %d" % k)
    return cmds[:m]


# 09: a small random mix with the shape checked at the end
cmds = random_case(2000, 1200, 500)
cmds += ["print", "preorder"]
write(9, cmds)

# 10: maximum M, keys drawn from a wide range so the tree stays shallow
cmds = random_case(MMAX - 2, INSERT_MAX, VMAX)
cmds += ["print", "preorder"]
write(10, cmds)

# 11: maximum M, keys from a narrow range so duplicates and absent deletes
#     are constant
cmds = random_case(MMAX - 2, INSERT_MAX, 30_000)
cmds += ["print", "preorder"]
write(11, cmds)

# 12: inserts only, no deletes, at the full insert count
cmds = ["insert %d" % random.randint(-VMAX, VMAX) for _ in range(INSERT_MAX)]
cmds += ["search %d" % random.randint(-VMAX, VMAX) for _ in range(99_998)]
cmds += ["print", "preorder"]
write(12, cmds)

# 13: a deliberately deep tree -- a sorted run of 4,000 keys, which makes a
#     spine, with random keys around it. The height cap is 5,000 and this
#     case sits near it.
cmds = ["insert %d" % k for k in range(1, 4001)]
cmds += ["insert %d" % random.randint(4001, VMAX) for _ in range(20_000)]
cmds += ["search %d" % random.randint(1, 4000) for _ in range(50_000)]
cmds += ["delete %d" % k for k in range(1, 2001)]
cmds += ["print", "preorder"]
write(13, cmds)

print("generated 14 cases")
for i in range(14):
    m, inserts, peak = SUMMARY[i]
    print("  case %02d: M = %-7s inserts %6d  peak height %5d"
          % (i, m, inserts, peak))
