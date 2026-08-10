#!/usr/bin/env python3
"""Test case generator for ds-14-hash-table.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Why there is a print command
----------------------------
Without it, any working map passes -- a student could ignore the buckets
entirely and delegate to java.util.HashMap. `print` shows every bucket's
contents in order, so the table has to be the chaining one the problem
describes: the right slot, computed with key % size, and the right order
within each chain.

That also makes 14.4's picture checkable directly. The same reasoning as
ds-11-heap's print command.

What the cases are built to catch
---------------------------------
  1. Not handling negative keys. Java's % returns a negative remainder for a
     negative left operand, and a negative index throws. Case 02 is published
     as a sample and is built from negative keys.

  2. put on an existing key appending a second entry instead of replacing the
     value. get() might still find the right one depending on the order of the
     walk, but the bucket contents are wrong at once. Case 03 overwrites keys
     repeatedly.

  3. Collisions handled by overwriting whatever is in the slot -- no chain at
     all. Case 01 is the book's own example, where 1 and 11 share a slot.

  4. remove taking out the wrong entry, or the whole bucket. Case 04 removes
     from the middle of a chain.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20261402)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

KEY_MAX = 1_000_000_000
VAL_MAX = 1_000_000_000
MMAX = 200_000
SIZE_MAX = 1_000


class Table:
    """Reference model: a list of chains, exactly as the problem describes."""

    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash(self, key):
        return ((key % self.size) + self.size) % self.size

    def put(self, key, value):
        b = self.buckets[self.hash(key)]
        for entry in b:
            if entry[0] == key:
                entry[1] = value
                return
        b.append([key, value])

    def get(self, key):
        for entry in self.buckets[self.hash(key)]:
            if entry[0] == key:
                return entry[1]
        return -1

    def remove(self, key):
        b = self.buckets[self.hash(key)]
        for i, entry in enumerate(b):
            if entry[0] == key:
                del b[i]
                return

    def render(self):
        parts = []
        for i in range(self.size):
            s = "%d:" % i
            for k, v in self.buckets[i]:
                s += " %d=%d" % (k, v)
            parts.append(s)
        return " |".join(parts)


def run(size, commands):
    t = Table(size)
    out = []
    for c in commands:
        p = c.split()
        if p[0] == "put":
            t.put(int(p[1]), int(p[2]))
        elif p[0] == "get":
            out.append(str(t.get(int(p[1]))))
        elif p[0] == "remove":
            t.remove(int(p[1]))
        elif p[0] == "print":
            out.append(t.render())
        else:
            raise ValueError(c)
    return out


def write(idx, size, commands):
    assert 1 <= size <= SIZE_MAX, "size out of range in case %d" % idx
    assert 1 <= len(commands) <= MMAX, "M out of range in case %d" % idx
    prints = sum(1 for c in commands if c == "print")
    assert prints <= 20, "too many print commands in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d %d\n" % (size, len(commands)))
        f.write("\n".join(commands) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("".join(line + "\n" for line in run(size, commands)))


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's own example. 1 and 11 land in the same bucket.
write(0, 10, ["put 1 100", "put 11 200", "get 1", "get 11",
              "print", "remove 1", "get 1", "get 11", "print"])

# 01 sample: a chain of four keys in one bucket, removed from the middle
write(1, 5, ["put 0 10", "put 5 20", "put 10 30", "put 15 40", "print",
             "remove 10", "print", "get 10", "get 15", "print"])

# 02 sample: negative keys. -7 % 10 is -7 in Java, and a negative index
#            throws. 02 must be published: it is the only sample that reaches
#            that, and the book states the requirement explicitly.
write(2, 10, ["put -7 1", "put 3 2", "print", "get -7", "get 3",
              "put -13 5", "print", "remove -7", "print", "get -7"])

# 03: putting the same key over and over. The value changes; the position in
#     the chain does not.
write(3, 4, ["put 2 1", "put 6 2", "put 2 99", "print",
             "put 6 88", "print", "get 2", "get 6"])

# 04: a table of size 1, so every key collides
write(4, 1, ["put 5 50", "put -5 -1", "put 0 7", "print",
             "remove -5", "print", "get -5", "get 5"])

# 05: keys and values at the ends of their ranges
write(5, 7, ["put 1000000000 1000000000", "put -1000000000 0",
             "print", "get 1000000000", "get -1000000000"])

# 06: a stored value of -1, which the get() convention cannot distinguish
#     from a miss. Kept deliberately -- it is the problem's convention.
write(6, 3, ["put 4 -1", "get 4", "get 5", "print"])

# 07: removing keys that are not there, and from empty buckets
write(7, 5, ["remove 3", "print", "put 3 30", "remove 8", "print",
             "remove 3", "remove 3", "print", "get 3"])

# 08: every bucket used exactly once
write(8, 8, ["put %d %d" % (i, i * 10) for i in range(8)] +
            ["print"] + ["get %d" % i for i in range(8)])

# ------------------------------------------------------------------ random


def random_case(m, size, key_hi, prints=4, negative_only=False):
    cmds = []
    live = []
    every = m // (prints + 1)
    while len(cmds) < m:
        r = random.random()
        if r < 0.45 or not live:
            k = random.randint(-key_hi, -1) if negative_only \
                else random.randint(-key_hi, key_hi)
            cmds.append("put %d %d" % (k, random.randint(0, VAL_MAX)))
            if k not in live:
                live.append(k)
        elif r < 0.7:
            k = random.choice(live) if random.random() < 0.7 \
                else (random.randint(-key_hi, -1) if negative_only
                      else random.randint(-key_hi, key_hi))
            cmds.append("get %d" % k)
        else:
            k = random.choice(live)
            cmds.append("remove %d" % k)
            live.remove(k)
        if every and len(cmds) % every == 0 and cmds.count("print") < prints:
            cmds.append("print")
    return cmds[:m]


# 09: a small table with plenty of traffic, so the chains grow long
write(9, 8, random_case(3000, 8, 1000))

# 10: maximum M on a small table -- the worst load factor, and the case that
#     shows what 14.5 is about
write(10, 10, random_case(MMAX - 5, 10, 100_000))

# 11: maximum M on the largest table, keys spread wide
write(11, SIZE_MAX, random_case(MMAX - 5, SIZE_MAX, KEY_MAX))

# 12: every key congruent to every other, so ALL of them land in one bucket
#     however large the table is -- the degenerate case 14.5 warns about.
#
#     Only 4,000 puts here, not 200,000. With one chain holding everything,
#     each put walks the whole chain, so the work is quadratic FOR THE
#     CORRECT SOLUTION TOO: 200,000 keys would be 2 * 10^10 steps and the
#     reference would be the thing that timed out. 4,000 is 8 * 10^6, which
#     makes the point without punishing anybody.
size = 997
cmds = []
for i in range(4000):
    cmds.append("put %d %d" % (size * i, i))
for i in range(0, 4000, 400):
    cmds.append("get %d" % (size * i))
cmds.append("print")
write(12, size, cmds)

# 13: maximum M with negative keys throughout
write(13, 64, random_case(MMAX - 5, 64, 100_000, negative_only=True))

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        size, m = map(int, f.readline().split())
    print("  case %02d: size = %-6d M = %-7d" % (i, size, m))
