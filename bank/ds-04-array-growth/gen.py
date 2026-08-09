#!/usr/bin/env python3
"""Test case generator for ds-04-array-growth.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Design notes
------------
This problem asks for the cost of a sequence of operations on an array-based
list, not for the list itself. Three mistakes are meant to surface as partial
scores:

  1. Accumulating the move count in an int. Two hundred thousand insertions at
     the front cost about 2 * 10^10 moves, well past the int ceiling of
     2.1 * 10^9. Small cases pass and large ones come back negative.
     Cases 08, 10, 11 and 13 cross the line; case 07 does not, on purpose, so
     the mistake is partial rather than total.

  2. Actually building the list and moving elements one at a time. That is
     O(Q * n) and times out on the large cases, while the intended solution
     never allocates anything and is O(Q).

  3. Growing at the wrong moment. The book's add(int, T) calls ensureCapacity
     BEFORE it shifts, and add(T) calls it before it stores; remove never
     grows at all. Case 06 sits exactly on capacity boundaries so that an
     off-by-one in the order shows up in the capacity column.

Every generated sequence is valid: a position is only ever used when the list
is non-empty, and always in 0 .. size-1, which is what the book's
checkPosition permits.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20260412)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

QMAX = 200_000


def simulate(capacity, ops):
    """Reference model of the cost, following 4.2 exactly.

    add(T)          : ensureCapacity, then store          -> 0 moves
    add(int, T)     : ensureCapacity, then shift the tail -> size - position
    remove(int)     : pull the tail forward               -> size - 1 - position
    ensureCapacity(): when full, copy every stored element and double
    """
    size = moves = copies = 0
    for op in ops:
        if op[0] == "add":
            if size == capacity:
                copies += capacity
                capacity *= 2
            size += 1
        elif op[0] == "addAt":
            if size == capacity:
                copies += capacity
                capacity *= 2
            moves += size - op[1]
            size += 1
        else:                                    # removeAt
            moves += size - 1 - op[1]
            size -= 1
    return moves, copies, capacity


def render(op):
    return op[0] if len(op) == 1 else "%s %d" % op


def write(idx, cases):
    total = sum(len(ops) for _, ops in cases)
    assert 1 <= len(cases) <= 100, "T out of range in case %d" % idx
    assert total <= QMAX, "sum of Q = %d exceeds the limit in case %d" % (total, idx)
    for capacity, ops in cases:
        assert 1 <= capacity <= 1000
        assert 1 <= len(ops) <= QMAX
        # replay to confirm every position is one checkPosition would allow
        size = 0
        for op in ops:
            if op[0] == "add":
                size += 1
            else:
                assert size > 0, "case %d: position op on an empty list" % idx
                assert 0 <= op[1] < size, "case %d: position out of range" % idx
                size += 1 if op[0] == "addAt" else -1
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(cases))
        for capacity, ops in cases:
            f.write("%d %d\n" % (capacity, len(ops)))
            f.write("\n".join(render(op) for op in ops) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for capacity, ops in cases:
            f.write("%d %d %d\n" % simulate(capacity, ops))


def front_inserts(q):
    """One append, then q-1 insertions at position 0: the costliest sequence."""
    return [("add",)] + [("addAt", 0)] * (q - 1)


def random_ops(q, p_front=0.0):
    ops, size = [], 0
    while len(ops) < q:
        r = random.random()
        if size == 0 or r < 0.45:
            ops.append(("add",))
            size += 1
        elif r < 0.45 + p_front:
            ops.append(("addAt", 0))
            size += 1
        elif r < 0.75:
            ops.append(("addAt", random.randrange(size)))
            size += 1
        else:
            ops.append(("removeAt", random.randrange(size)))
            size -= 1
    return ops


# ---------------------------------------------------------------- hand-built

# 00 sample: the worked example from the statement
write(0, [(2, [("add",), ("add",), ("add",), ("addAt", 0),
               ("removeAt", 1), ("add",)])])

# 01 sample: nothing but appends, so every move is zero and only growth shows.
#            Capacity 2 doubles at sizes 2, 4 and 8.
write(1, [(2, [("add",)] * 10)])

# 02 sample: insertion at the front every time, the maximum shift per step,
#            then removal from the front, which costs the same going back
write(2, [
    (4, front_inserts(6)),
    (4, [("add",)] * 5 + [("removeAt", 0)] * 5),
    (4, [("add",)] * 5 + [("removeAt", 4), ("removeAt", 3)]),
])

# 03: removal at the last position costs nothing to shift
write(3, [(8, [("add",)] * 8 + [("removeAt", 7 - i) for i in range(8)])])

# 04: capacity 1, which doubles on almost every early append
write(4, [(1, [("add",)] * 20), (1, front_inserts(20))])

# 05: the list shrinks back down, and capacity must NOT shrink with it
write(5, [(2, [("add",)] * 40 + [("removeAt", 0)] * 39 + [("add",)] * 3)])

# 06: sequences that sit exactly on capacity boundaries, to catch growing at
#     the wrong moment. Filling to exactly capacity must not grow; the next
#     insertion must.
write(6, [
    (4, [("add",)] * 4),
    (4, [("add",)] * 5),
    (4, [("add",)] * 4 + [("addAt", 0)]),
    (4, [("add",)] * 4 + [("removeAt", 0)] + [("add",)]),
    (16, [("add",)] * 16 + [("addAt", 8)]),
    (1000, [("add",)] * 1000 + [("addAt", 500)]),
])

# 07: T at its maximum with a moderate total, and deliberately kept small
#     enough that an int move counter still survives this one
cases = []
remaining = QMAX // 4
for i in range(100):
    q = max(1, min(remaining - (100 - i - 1), random.randint(1, 600)))
    remaining -= q
    cases.append((random.randint(1, 1000), random_ops(q)))
write(7, cases)

# ------------------------------------------------------------------ maximum

# 08: the overflow case. 200,000 insertions at the front cost about
#     2 * 10^10 moves.
write(8, [(1, front_inserts(QMAX))])

# 09: 200,000 appends. No moves at all, and eighteen doublings from capacity 1.
write(9, [(1, [("add",)] * QMAX)])

# 10: build a long list, then dismantle it from the front, which costs the
#     same as building it did
half = QMAX // 2
write(10, [(1, [("add",)] * half + [("removeAt", 0)] * half)])

# 11: maximum size, heavily front-loaded random operations
write(11, [(1000, random_ops(QMAX, p_front=0.25))])

# 12: many mid-size random cases starting from assorted capacities
cases = []
remaining = QMAX
for i in range(100):
    q = max(1, min(remaining - (100 - i - 1), random.randint(1, 2000)))
    remaining -= q
    cases.append((random.choice([1, 2, 3, 7, 25, 100, 999, 1000]), random_ops(q)))
write(12, cases)

# 13: two large sequences, one all front insertion and one all middle
#     insertion, both crossing the int ceiling
q = QMAX // 2
middle = [("add",)]
size = 1
for _ in range(q - 1):
    middle.append(("addAt", size // 2))
    size += 1
write(13, [(1, front_inserts(q)), (1, middle)])

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        t = f.readline().strip()
    with open("%s/output%02d.txt" % (OUT, i)) as f:
        worst = max(int(line.split()[0]) for line in f)
    flag = "  <-- exceeds int" if worst > 2_147_483_647 else ""
    print("  case %02d: T = %-4s largest move count %14d%s" % (i, t, worst, flag))
