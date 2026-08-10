#!/usr/bin/env python3
"""Test case generator for ds-05-linked-list.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Relationship to ds-04-array-list
--------------------------------
The two problems are deliberately the same problem: same interface, same three
methods, same command driver, same output format. Only the implementation
underneath changes. Two things differ, and both are on purpose.

  * The bound on addAt. The book's Array_List.checkPosition admits
    0 <= i < size, so appending through add(int, T) is an error there. The
    book's LinkedList.add(int, T) admits 0 <= i <= size, so appending IS
    allowed here. That is the book's own asymmetry and it is left standing.

  * Q is 10,000 rather than 20,000. On a linked list, addAt, removeAt and get
    all walk from head, so the same command mix costs O(Q * n) instead of
    O(Q). Halving Q buys back roughly the same wall time, which is the
    chapter's whole point stated in numbers.

What the cases are built to catch
---------------------------------
  1. Swapping the two splice lines. Assigning prev.next before reading it
     leaves node.next pointing at node itself, and toString then loops
     forever. This shows up as a timeout, not a wrong answer.

  2. Not moving tail back when the last node is removed. Silent until the
     next append, which then attaches to a node no longer in the list.
     Case 04 is built around exactly this sequence.

  3. indexOf comparing with == instead of .equals(). Case 02 straddles the
     Integer cache boundary at 127/128 and is published as a sample.

  4. Copying the array version's bound and rejecting i == size. Case 00 and
     every append-heavy case catch it.

  5. Forgetting numberOfEntries++ / --.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20260501)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

BIG = 1_000_000_000
QMAX = 10_000


def run(commands):
    """Reference model. Mirrors the Tail, including the error cases.

    Note the two different bounds:
        addAt   0 <= i <= size     (appending is allowed)
        removeAt, get   0 <= i < size
    """
    data = []
    out = []
    for c in commands:
        parts = c.split()
        op = parts[0]
        if op == "add":
            data.append(int(parts[1]))
        elif op == "addAt":
            i, x = int(parts[1]), int(parts[2])
            if 0 <= i <= len(data):
                data.insert(i, x)
            else:
                out.append("error")
        elif op == "removeAt":
            i = int(parts[1])
            if 0 <= i < len(data):
                out.append(str(data.pop(i)))
            else:
                out.append("error")
        elif op == "removeValue":
            x = int(parts[1])
            if x in data:
                data.remove(x)
                out.append("1")
            else:
                out.append("0")
        elif op == "get":
            i = int(parts[1])
            out.append(str(data[i]) if 0 <= i < len(data) else "error")
        elif op == "indexOf":
            x = int(parts[1])
            out.append(str(data.index(x)) if x in data else "-1")
        elif op == "size":
            out.append(str(len(data)))
        elif op == "print":
            out.append("[" + ", ".join(map(str, data)) + "]")
        else:
            raise ValueError("unknown command: " + c)
    return out


def write(idx, commands):
    assert 1 <= len(commands) <= QMAX, "Q out of range in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(commands))
        f.write("\n".join(commands) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("".join(line + "\n" for line in run(commands)))


# ---------------------------------------------------------------- hand-built

# 00 sample: the worked example from the statement. The last two commands are
#            the ones that differ from the array version: addAt at size
#            appends here instead of failing.
write(0, [
    "add 10", "add 20", "add 30", "print",
    "addAt 1 15", "print",
    "removeAt 0", "print",
    "indexOf 30", "get 5", "addAt 3 99", "print", "size",
])

# 01 sample: an empty list, and the edges of both bounds. addAt 0 into an
#            empty list is legal (0 == size); get 0 and removeAt 0 are not.
write(1, [
    "size", "print", "get 0", "removeAt 0",
    "indexOf 7", "removeValue 7",
    "addAt 0 5", "print", "size",
    "addAt 1 6", "print",           # i == size: appends
    "addAt 3 7", "print",           # i > size: error
    "addAt -1 8",
    "get 2", "removeAt 2", "removeAt 1", "print", "size",
])

# 02 sample: values straddling the Integer cache boundary (-128..127).
#            An indexOf written with == finds 127 and misses 128.
write(2, [
    "add 126", "add 127", "add 128", "add 129", "add 1000", "print",
    "indexOf 126", "indexOf 127", "indexOf 128", "indexOf 129", "indexOf 1000",
    "indexOf 500",
    "removeValue 128", "print",
    "removeValue 127", "print",
])

# 03: duplicates. indexOf must report the FIRST match, removeValue takes one.
write(3, [
    "add 5", "add 3", "add 5", "add 3", "add 5", "print",
    "indexOf 5", "indexOf 3",
    "removeValue 5", "print", "indexOf 5",
    "removeValue 3", "print",
    "removeValue 9", "size", "print",
])

# 04: the tail trap, isolated. Remove the last node, then append. If tail was
#     not moved back, the new node hangs off a node that has left the list and
#     never appears in the output.
write(4, [
    "add 1", "add 2", "add 3", "print",
    "removeAt 2", "print",          # removes the tail node
    "add 4", "print", "size",       # append: needs the corrected tail
    "removeAt 1", "print",
    "add 5", "print",
    "removeAt 0", "removeAt 0", "print", "size",
    "add 6", "print",               # append onto a list emptied and refilled
    "removeAt 0", "add 7", "print", "size",
])

# 05: insert at the front over and over, then take them off the front
cmds = ["add 100"] + ["addAt 0 %d" % (i * 7 + 1) for i in range(1, 40)]
cmds += ["print", "size"] + ["get %d" % i for i in range(0, 40, 5)]
cmds += ["removeAt 0"] * 20 + ["print", "size"]
write(5, cmds)

# 06: insert and remove in the middle, where getNodeAt(givenPosition - 1)
#     is what does the work
cmds = ["add %d" % i for i in range(1, 21)]
cmds += ["addAt 10 %d" % (900 + i) for i in range(5)]
cmds += ["print"]
cmds += ["removeAt 12", "removeAt 11", "removeAt 10", "print", "size"]
cmds += ["addAt 25 555", "print"]       # i == size after the removals
write(6, cmds)

# 07: out-of-range positions against a short list, for both bounds
cmds = ["add 1", "add 2", "add 3"]
for i in [-5, -1, 3, 4, 100, 1000000]:
    cmds += ["get %d" % i, "removeAt %d" % i, "addAt %d 0" % i]
cmds += ["print", "size"]
write(7, cmds)

# ------------------------------------------------------------------ random

OPS_SMALL = 100          # value ceiling for the "== happens to work" group


def random_case(q, hi, seed_ops=30, front_heavy=False, append_heavy=False):
    """Random command mix.

    indexOf and removeValue aim most of their queries at values that were
    actually inserted. Querying purely at random would make indexOf return -1
    either way at hi = 1e9, and the == mistake would sail through.
    """
    vals = [random.randint(1, hi) for _ in range(seed_ops)]
    cmds = ["add %d" % v for v in vals]
    n = seed_ops

    def a_value():
        if vals and random.random() < 0.80:
            return random.choice(vals)
        return random.randint(1, hi)

    while len(cmds) < q:
        r = random.random()
        if front_heavy and r < 0.45:
            v = random.randint(1, hi)
            cmds.append("addAt 0 %d" % v)
            vals.append(v)
            n += 1
        elif append_heavy and r < 0.45:
            v = random.randint(1, hi)
            cmds.append("addAt %d %d" % (n, v))     # i == size: the append path
            vals.append(v)
            n += 1
        elif r < 0.28:
            v = random.randint(1, hi)
            cmds.append("add %d" % v)
            vals.append(v)
            n += 1
        elif r < 0.46:
            v = random.randint(1, hi)
            cmds.append("addAt %d %d" % (random.randint(0, n), v))
            vals.append(v)
            n += 1
        elif r < 0.60 and n > 0:
            cmds.append("removeAt %d" % random.randrange(n))
            n -= 1
        elif r < 0.72:
            cmds.append("removeValue %d" % a_value())
            n = max(0, n - 1)          # approximate; the model decides for real
        elif r < 0.90:
            cmds.append("indexOf %d" % a_value())
        elif r < 0.96 and n > 0:
            cmds.append("get %d" % random.randrange(n))
        else:
            cmds.append("size")
    return cmds[:q]


# 08: small values only, so an == solution survives this one
write(8, random_case(600, OPS_SMALL))

# 09: large values, so an == solution fails this one
write(9, random_case(600, BIG))

# 10: maximum Q, small values
write(10, random_case(QMAX, OPS_SMALL))

# 11: maximum Q, large values
write(11, random_case(QMAX, BIG))

# 12: maximum Q, front-heavy. Cheap on a linked list (addFirst is O(1)) and
#     expensive on an array -- the mirror image of ds-04-array-list case 12.
write(12, random_case(QMAX, BIG, front_heavy=True))

# 13: maximum Q, append-heavy through addAt at i == size, which is the path
#     that does not exist in the array version at all
write(13, random_case(QMAX, BIG, append_heavy=True))

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        q = f.readline().strip()
    print("  case %02d: Q = %-6s input %8d bytes" % (i, q, os.path.getsize(path)))
