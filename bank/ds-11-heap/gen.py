#!/usr/bin/env python3
"""Test case generator for ds-11-heap.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Why there is a print command
----------------------------
A heap is not determined by the set of values it holds -- many arrays satisfy
the heap condition over the same numbers. Printing only the popped values
would let any correct priority queue pass, including java.util.PriorityQueue,
whose internal array differs from the book's.

`print` shows the array itself, so the two algorithms of 11.3 have to be the
book's: the new value is appended and walked up, and on removal the LAST value
is moved to the root and walked down. That also makes the traces of 11.5
Level 1 checkable directly, which is what those exercises ask for by hand.

What the cases are built to catch
---------------------------------
  1. Down-heap swapping with the larger child instead of the smaller. The
     popped values are still roughly right for a while, but the array is
     wrong immediately. Case 02 is published as a sample.

  2. Removing the last element after overwriting the root rather than before,
     which loses a value.

  3. Up-heap stopping at the wrong moment, or comparing against the wrong
     parent index.

  4. Using java.util.PriorityQueue underneath. Every popped value is right and
     every printed array is wrong.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20261101)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
MMAX = 200_000


class Heap:
    """Reference model: the book's push and pop, on a plain list."""

    def __init__(self):
        self.a = []

    def push(self, x):
        self.a.append(x)
        i = len(self.a) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.a[i] < self.a[p]:
                self.a[i], self.a[p] = self.a[p], self.a[i]
                i = p
            else:
                break

    def pop(self):
        top = self.a[0]
        last = self.a.pop()
        if self.a:
            self.a[0] = last
            i, n = 0, len(self.a)
            while True:
                l, r, small = 2 * i + 1, 2 * i + 2, i
                if l < n and self.a[l] < self.a[small]:
                    small = l
                if r < n and self.a[r] < self.a[small]:
                    small = r
                if small == i:
                    break
                self.a[i], self.a[small] = self.a[small], self.a[i]
                i = small
        return top


def run(commands):
    h = Heap()
    out = []
    for c in commands:
        parts = c.split()
        op = parts[0]
        if op == "push":
            h.push(int(parts[1]))
        elif op == "pop":
            out.append("empty" if not h.a else str(h.pop()))
        elif op == "peek":
            out.append("empty" if not h.a else str(h.a[0]))
        elif op == "size":
            out.append(str(len(h.a)))
        elif op == "print":
            out.append(" ".join(map(str, h.a)))
        else:
            raise ValueError(c)
    return out


def write(idx, commands):
    assert 1 <= len(commands) <= MMAX, "M out of range in case %d" % idx
    prints = sum(1 for c in commands if c == "print")
    assert prints <= 20, "too many print commands in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(commands))
        f.write("\n".join(commands) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("".join(line + "\n" for line in run(commands)))


# ---------------------------------------------------------------- hand-built

# 00 sample: 11.5 Level 1 Problem 1 -- inserting 5, 3, 8, 1, 6 and showing the
#            array after each step
write(0, ["push 5", "print", "push 3", "print", "push 8", "print",
          "push 1", "print", "push 6", "print"])

# 01 sample: 11.5 Level 1 Problem 2 -- one pop from [1, 3, 8, 5, 6]
write(1, ["push 1", "push 3", "push 8", "push 5", "push 6", "print",
          "pop", "print", "size", "peek"])

# 02 sample: the down-heap example of 11.3 item 2. The root's children are
#            4 and 6; swapping with 6 instead of 4 leaves a broken heap that
#            still pops a plausible-looking value next time.
#            An empty heap is touched at both ends too.
write(2, ["pop", "peek", "size",
          "push 3", "push 4", "push 6", "push 21", "push 10", "push 7",
          "push 8", "print",
          "pop", "print", "peek",
          "pop", "print"])

# 03: pushing in ascending order, so nothing ever moves up
write(3, ["push %d" % i for i in range(1, 21)] + ["print"] +
         ["pop"] * 5 + ["print"])

# 04: pushing in descending order, so every value climbs to the root
write(4, ["push %d" % i for i in range(20, 0, -1)] + ["print"] +
         ["pop"] * 5 + ["print"])

# 05: all values equal, where no swap is ever needed and an off-by-one in the
#     comparison still shows in the array
write(5, ["push 7"] * 15 + ["print"] + ["pop"] * 7 + ["print", "size"])

# 06: a single element, pushed and popped repeatedly
write(6, ["push 5", "print", "pop", "print", "size", "pop",
          "push 9", "peek", "pop", "peek"])

# 07: the 11.3 item 1 example -- inserting 6 into the heap [3,4,7,21,10,20,8]
write(7, ["push 3", "push 4", "push 7", "push 21", "push 10", "push 20",
          "push 8", "print", "push 6", "print"])

# 08: negative values and the ends of the range
write(8, ["push 0", "push -1000000000", "push 1000000000", "print",
          "pop", "print", "pop", "print", "pop", "print", "pop"])

# ------------------------------------------------------------------ random


def random_case(m, hi, pop_heavy=False, prints=0):
    """`prints` spreads print commands through the run rather than leaving one
    at the end. That matters: java.util.PriorityQueue performs the same
    sift-up as the book, so a solution built on it prints the same array after
    a run of pushes -- the layouts only diverge after removals. A single print
    at the end catches it far less often than a handful spread through."""
    cmds, depth = [], 0
    every = m // (prints + 1) if prints else 0
    while len(cmds) < m:
        r = random.random()
        if depth == 0 or (not pop_heavy and r < 0.5) or (pop_heavy and r < 0.35):
            cmds.append("push %d" % random.randint(-hi, hi))
            depth += 1
        elif r < 0.85:
            cmds.append("pop")
            depth = max(0, depth - 1)
        elif r < 0.94:
            cmds.append("peek")
        else:
            cmds.append("size")
        if every and len(cmds) % every == 0 and cmds.count("print") < prints:
            cmds.append("print")
    return cmds[:m]


# 09: a moderate mix, with the array shown at the end
write(9, random_case(5000, 1000, prints=8) + ["print"])

# 10: maximum M, wide value range
write(10, random_case(MMAX - 12, VMAX, prints=10) + ["print"])

# 11: maximum M, narrow value range so ties are constant
write(11, random_case(MMAX - 12, 50, prints=10) + ["print"])

# 12: maximum M, pop-heavy so the heap is often empty
write(12, random_case(MMAX - 12, VMAX, pop_heavy=True, prints=10) + ["print"])

# 13: push everything, then pop everything -- the heap reaches its largest
#     and the pops come out in ascending order
half = (MMAX - 40) // 2
cmds = ["push %d" % random.randint(-VMAX, VMAX) for _ in range(half)]
cmds += ["print"]
for j in range(half):
    cmds.append("pop")
    if j % (half // 8) == 0:
        cmds.append("print")
cmds += ["print"]
write(13, cmds)

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        m = int(f.readline())
        cmds = [f.readline().rstrip("\n") for _ in range(m)]
    peak, d = 0, 0
    for c in cmds:
        if c.startswith("push"):
            d += 1
            peak = max(peak, d)
        elif c == "pop":
            d = max(0, d - 1)
    print("  case %02d: M = %-7s peak heap size %7d" % (i, m, peak))
