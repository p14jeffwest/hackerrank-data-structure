#!/usr/bin/env python3
"""Test case generator for ds-04-array-list.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Design notes
------------
Three methods are left to the student: add(int, T), remove(int), indexOf(T).
The case set is arranged so that each of the classic mistakes shows up as a
partial score rather than a zero.

  1. Shifting front-to-back in add(int, T) instead of back-to-front.
     Overwrites an element that has not moved yet. Any case with an addAt
     into a non-empty list catches this.

  2. Comparing with == instead of .equals() in indexOf.
     T is an object type here, and the JVM caches boxed Integer values in
     -128..127. So == quietly works for small numbers and fails for larger
     ones. Cases are deliberately split into small-value and large-value
     groups, and case 02 sits right on the 127/128 boundary so the failure is
     visible in a published sample.

  3. Skipping checkPosition.
     Every out-of-range position must print "error". A missing guard turns
     some of those into wrong values or into a silently corrupted list.

  4. Forgetting numberOfEntries--.
     The size and print commands expose it immediately.

Note that leaving out `list[numberOfEntries - 1] = null` in remove() changes
no output at all, since toString only reads up to numberOfEntries. It is a
garbage-collection concern, not a correctness one, and no test can catch it.

Everything written here is ASCII, with LF line endings.
"""
import random
import os

random.seed(20260409)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

BIG = 1_000_000_000


def run(commands):
    """Reference model. Mirrors the Tail exactly, including the error cases."""
    data = []
    out = []
    for c in commands:
        parts = c.split()
        op = parts[0]
        if op == "add":
            data.append(int(parts[1]))
        elif op == "addAt":
            i, x = int(parts[1]), int(parts[2])
            if 0 <= i < len(data):
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
    assert 1 <= len(commands) <= 20_000, "Q out of range in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(commands))
        f.write("\n".join(commands) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        body = run(commands)
        f.write("".join(line + "\n" for line in body))


# ---------------------------------------------------------------- hand-built

# 00 sample: the worked example from the statement
write(0, [
    "add 10", "add 20", "add 30", "print",
    "addAt 1 15", "print",
    "removeAt 0", "print",
    "indexOf 30", "get 5", "addAt 3 99", "size",
])

# 01 sample: an empty list, and every way a position can be out of range.
#            addAt 0 into an empty list is an error too, because a valid
#            position must refer to an element that already exists.
write(1, [
    "size", "print", "get 0", "removeAt 0", "addAt 0 5",
    "indexOf 7", "removeValue 7",
    "add 7", "print", "size",
    "get -1", "get 1", "removeAt 1", "addAt 1 9", "addAt -1 9",
    "get 0", "indexOf 7", "removeValue 7", "print", "size",
])

# 02 sample: values straddling the Integer cache boundary (-128..127).
#            An indexOf written with == finds 127 and misses 128, so this
#            sample fails visibly before the student ever submits.
write(2, [
    "add 126", "add 127", "add 128", "add 129", "add 1000", "print",
    "indexOf 126", "indexOf 127", "indexOf 128", "indexOf 129", "indexOf 1000",
    "indexOf 500",
    "removeValue 128", "print",
    "removeValue 127", "print",
])

# 03: duplicates. indexOf must report the FIRST match, removeValue must take
#     exactly one node.
write(3, [
    "add 5", "add 3", "add 5", "add 3", "add 5", "print",
    "indexOf 5", "indexOf 3",
    "removeValue 5", "print", "indexOf 5",
    "removeValue 3", "print",
    "removeValue 9", "size", "print",
])

# 04: insert at the front over and over, then walk the whole list back out
cmds = ["addAt 0 %d" % (i * 7 + 1) for i in range(1, 40)]
cmds = ["add 100"] + cmds + ["print", "size"] + \
       ["get %d" % i for i in range(0, 40, 5)]
write(4, cmds)

# 05: remove from the front over and over
cmds = ["add %d" % (i * 3) for i in range(1, 41)]
cmds += ["removeAt 0" for _ in range(20)] + ["print", "size"]
cmds += ["removeAt %d" % (19 - i) for i in range(20)] + ["print", "size"]
write(5, cmds)

# 06: insert and remove in the middle, where both shifting directions matter
cmds = ["add %d" % i for i in range(1, 21)]
cmds += ["addAt 10 %d" % (900 + i) for i in range(5)]
cmds += ["print"]
cmds += ["removeAt 12", "removeAt 11", "removeAt 10", "print", "size"]
write(6, cmds)

# 07: nothing but out-of-range positions against a short list
cmds = ["add 1", "add 2", "add 3"]
for i in [-5, -1, 3, 4, 100, 1000000]:
    cmds += ["get %d" % i, "removeAt %d" % i, "addAt %d 0" % i]
cmds += ["print", "size"]
write(7, cmds)

# ------------------------------------------------------------------ random

OPS_SMALL = 100          # value ceiling for the "== happens to work" group
Q_BIG = 20_000


def random_case(q, hi, seed_ops=30, front_heavy=False):
    """Build a random command sequence.

    The generator tracks the values it has inserted and aims most indexOf and
    removeValue queries at one of them. Querying purely random values would be
    useless here: with hi = 1e9 the value is almost never present, indexOf
    returns -1 either way, and an == solution would sail through. The whole
    point of the large-value cases is that the query HITS.
    """
    vals = [random.randint(1, hi) for _ in range(seed_ops)]
    cmds = ["add %d" % v for v in vals]
    n = seed_ops

    def a_value():
        # 80% of the time, ask about something that is actually in there
        if vals and random.random() < 0.80:
            return random.choice(vals)
        return random.randint(1, hi)

    while len(cmds) < q:
        r = random.random()
        if front_heavy and r < 0.50:
            v = random.randint(1, hi)
            cmds.append("addAt 0 %d" % v)
            vals.append(v)
            n += 1
        elif r < 0.28:
            v = random.randint(1, hi)
            cmds.append("add %d" % v)
            vals.append(v)
            n += 1
        elif r < 0.46 and n > 0:
            v = random.randint(1, hi)
            cmds.append("addAt %d %d" % (random.randrange(n), v))
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
write(10, random_case(Q_BIG, OPS_SMALL))

# 11: maximum Q, large values
write(11, random_case(Q_BIG, BIG))

# 12: maximum Q, front-heavy insertion. This is the worst case for shifting:
#     the list grows large and every insert moves the whole tail.
write(12, random_case(Q_BIG, BIG, front_heavy=True))

# 13: maximum Q, nothing but appends and lookups. Forces the array to double
#     many times, and checks that indexOf stays correct at full size. The
#     queried values are drawn from what was inserted, so they all hit.
vals = [random.randint(1, BIG) for _ in range(Q_BIG - 200)]
cmds = ["add %d" % v for v in vals]
cmds += ["size", "get 0", "get %d" % (Q_BIG - 201)]
cmds += ["indexOf %d" % random.choice(vals) for _ in range(197)]
write(13, cmds)

print("generated 14 cases")
for i in range(14):
    with open("%s/input%02d.txt" % (IN, i)) as f:
        q = f.readline().strip()
    print("  case %02d: Q = %s" % (i, q))
