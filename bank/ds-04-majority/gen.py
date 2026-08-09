#!/usr/bin/env python3
"""Test case generator for ds-04-majority.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Design notes
------------
The book states this problem with n <= 10^4, where counting each element
against every other one -- O(n^2) -- still finishes. The bound here is a sum
of n up to 200,000, so that approach times out and the problem separates
something.

What the cases are built to catch:

  1. O(n^2) counting. Cases 07 through 13 are large enough to time out.

  2. A voting loop that never replaces its candidate (it only adds and
     subtracts votes, keeping the first element forever). Cases 10 and 11 put
     the majority element late or in long interleaved runs, so the counter
     reaches zero repeatedly and a missing replacement step shows.

  3. Guessing from position -- returning the first element, or the middle one
     without sorting. Cases 02, 03 and 10 deliberately place the majority
     element away from both.

  4. Comparing boxed Integers with == instead of unboxing to int. Small-value
     cases sit inside the -128..127 cache and pass; large-value cases do not.
     Case 02 straddles the boundary and is published as a sample.

  5. Sorting the list in place and taking the middle. The driver snapshots the
     list and prints "modified" if the call rearranged it, so this scores zero
     everywhere rather than passing quietly.

Every case satisfies the guarantee stated in the problem: exactly one value
occurs strictly more than n/2 times.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20260411)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

BIG = 1_000_000_000
NMAX = 200_000


def majority(a):
    """Reference answer, computed the obvious way rather than by voting."""
    best, count = None, 0
    seen = {}
    for x in a:
        seen[x] = seen.get(x, 0) + 1
        if seen[x] > count:
            best, count = x, seen[x]
    assert count * 2 > len(a), "no majority element: %d of %d" % (count, len(a))
    return best


def write(idx, lists):
    total = sum(len(a) for a in lists)
    assert 1 <= len(lists) <= 500, "T out of range in case %d" % idx
    assert total <= NMAX, "sum of n = %d exceeds the limit in case %d" % (total, idx)
    for a in lists:
        assert 1 <= len(a) <= NMAX
        assert all(1 <= x <= BIG for x in a)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(lists))
        for a in lists:
            f.write("%d\n" % len(a))
            f.write(" ".join(map(str, a)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for a in lists:
            f.write("%d\n" % majority(a))


def build(major, n, others, order="shuffle"):
    """A list of length n whose majority element is `major`.

    `others` supplies the filler values, drawn in turn. The majority element
    takes n//2 + 1 slots, the minimum that qualifies, which is the hardest
    case for anything that guesses.

    The two unshuffled orderings each defeat a different mistake, and they
    defeat each other, so both are needed.

    order="fillers_first" puts every non-majority element before the first
    occurrence of the majority element. This is what makes an O(n^2)
    count-each-element solution actually cost O(n^2): such a solution returns
    as soon as it finds the answer, so on a shuffled list it stops after one
    or two elements and finishes in O(n).

    order="majority_first" does the reverse, ending the list with filler. This
    is what catches a voting loop that compares boxed Integers with ==. Such a
    loop never matches anything, so its counter sits at zero and it adopts
    almost every element it sees as the new candidate -- which means it ends
    holding whatever came last. Put the majority element at the end and the
    broken loop returns the right answer by luck; put filler at the end and it
    does not.
    """
    need = n // 2 + 1
    pool = [x for x in others if x != major]
    filler = [pool[i % len(pool)] for i in range(n - need)]
    if order == "fillers_first":
        return filler + [major] * need
    if order == "majority_first":
        return [major] * need + filler
    a = [major] * need + filler
    random.shuffle(a)
    return a


# ---------------------------------------------------------------- hand-built

# 00 sample: the two worked examples from the statement
write(0, [[3, 2, 3], [2, 2, 1, 1, 1, 2, 2]])

# 01 sample: the smallest shapes. A single element is its own majority; a list
#            of one repeated value; a majority holding exactly n//2 + 1 slots.
write(1, [
    [7],
    [1000000000],
    [4, 4, 4],
    [1, 2, 1],
    [5, 5, 1, 5],
    [9, 1, 9, 2, 9],
])

# 02 sample: values on both sides of the Integer cache boundary, with the
#            majority element sitting neither first nor in the middle.
#            An == comparison on boxed values finds 127 and misses 128.
write(2, [
    [1, 2, 127, 127, 127],
    [1, 2, 128, 128, 128],
    [500, 500, 3, 500, 4],
    [1000000000, 7, 1000000000, 8, 1000000000],
])

# 03: the majority element is the smallest, then the largest, value present
write(3, [
    [1, 900, 1, 800, 1],
    [900, 1, 900, 2, 900],
    [1, 1, 1000000000, 1, 1000000000],
])

# 04: long alternating runs, so a voting counter returns to zero often
write(4, [
    [1, 2, 1, 3, 1, 4, 1],
    [5, 1, 5, 2, 5, 3, 5, 4, 5],
    [2, 2, 3, 3, 2, 3, 2],
])

# 05: even lengths, majority at exactly n//2 + 1
write(5, [build(11, n, [21, 22, 23, 24, 25]) for n in [2, 4, 6, 8, 10, 100]])

# 06: many small lists, small values (inside the Integer cache)
write(6, [build(random.randint(1, 100), random.randint(1, 30),
                [random.randint(1, 100) for _ in range(5)])
          for _ in range(400)])

# 07: T at its maximum, sum of n at its maximum, large values
lists = []
remaining = NMAX
for i in range(500):
    n = 1 if i == 499 else min(remaining - (500 - i - 1), random.randint(1, 700))
    n = max(1, n)
    remaining -= n
    lists.append(build(random.randint(1, BIG), n,
                       [random.randint(1, BIG) for _ in range(8)]))
write(7, lists)

# ------------------------------------------------------------------ maximum

# 08: one maximum list, majority at the bare minimum n//2 + 1, fillers first
write(8, [build(123456789, NMAX, [random.randint(1, BIG) for _ in range(50)],
                order="fillers_first")])

# 09: one maximum list, majority everywhere but one slot, and that one slot
#     comes last. A voting loop using == on boxed values ends up holding the
#     final element, so ending on filler is what exposes it.
write(9, [[777] * (NMAX - 1) + [1]])

# 10: adversarial ordering. Every non-majority element comes first, so the
#     counter is driven to zero again and again before the majority element
#     appears at all. A loop that never replaces its candidate holds on to
#     the wrong value; a solution that returns the first element or the
#     middle element also misses.
need = NMAX // 2 + 1
a = [random.randint(1, BIG) for _ in range(NMAX - need)] + [424242] * need
write(10, [a])

# 11: the mirror of 10 -- majority and filler strictly interleaved, so the
#     counter oscillates around zero for the whole pass
filler = [random.randint(1, BIG) for _ in range(NMAX - need)]
a = [555555] * (need - (NMAX - need))   # leftover padding goes in FRONT, so
for i in range(NMAX - need):            # the list ends on filler
    a.append(555555)
    a.append(filler[i])
write(11, [a])

# 12: one maximum list where the filler is 100,000 distinct values, so a
#     counting table has to hold them all -- and they all come first, so a
#     count-each-element solution pays a full pass for every one of them
need = NMAX // 2 + 1
a = list(range(1000, 1000 + NMAX - need)) + [321] * need
write(12, [a])

# 13: two large lists, values pinned at the top of the range
half = NMAX // 2
write(13, [
    build(BIG, half, [BIG - 1, BIG - 2, BIG - 3], order="fillers_first"),
    build(BIG - 1, half, [BIG, BIG - 2, BIG - 3], order="majority_first"),
])

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        t = f.readline().strip()
    print("  case %02d: T = %-5s input %8d bytes" % (i, t, os.path.getsize(path)))
