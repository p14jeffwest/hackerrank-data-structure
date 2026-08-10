#!/usr/bin/env python3
"""Test case generator for ds-07-last-card.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Design notes
------------
The book (7.5, Problem 4) states this with cards numbered 1 through N and asks
only for the survivor. That version does not need a queue at all: the survivor
of 1..N is a closed form, and a student who spots it never simulates anything.

Two changes fix that, both taken from the Korean counterpart:

  * the cards carry arbitrary numbers, so no formula in N gives the answer;
  * the discard ORDER is asked for as well, which cannot be produced without
    running the whole simulation.

The rule itself, and the worked examples, are the book's.

What the cases are built to catch:

  1. Removing from the front of a structure that shifts -- ArrayList.remove(0),
     or java.util.LinkedList driven by get(i). Either is O(n^2). Cases 08
     through 13 are large enough that it cannot finish.

  2. Getting the two steps the wrong way round -- moving first and discarding
     second, or discarding two at a time.

  3. N = 1, where nothing is discarded and the first output line is empty.

Every file is ASCII with LF line endings.
"""
import random
import os
from collections import deque

random.seed(20260702)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

BIG = 1_000_000_000
NMAX = 500_000


def simulate(cards):
    """Reference model: discard the front, then send the new front to the back."""
    deck = deque(cards)
    discarded = []
    while len(deck) > 1:
        discarded.append(deck.popleft())
        deck.append(deck.popleft())
    return discarded, deck[0]


def write(idx, cards):
    n = len(cards)
    assert 1 <= n <= NMAX, "N out of range in case %d" % idx
    assert all(1 <= x <= BIG for x in cards), "value out of range in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % n)
        f.write(" ".join(map(str, cards)) + "\n")
    discarded, survivor = simulate(cards)
    assert len(discarded) == n - 1
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write(" ".join(map(str, discarded)) + "\n")
        f.write("%d\n" % survivor)


# ---------------------------------------------------------------- hand-built

# 00 sample: the worked example from the statement
write(0, [10, 20, 30, 40])

# 01 sample: the book's own examples, with the cards numbered 1..N.
#            N = 5 leaves 2 and N = 7 leaves 6.
write(1, list(range(1, 6)))

# 02 sample: N = 1. Nothing is discarded, so the first output line is EMPTY
#            and the survivor is the only card. Published because an empty
#            line is easy to get wrong and impossible to guess.
write(2, [9])

# 03: N = 2 and N = 3, the smallest cases where anything happens at all
write(3, [7, 8])

# 04: the book's second example
write(4, list(range(1, 8)))

# 05: a power of two, where the survivor is the last card
write(5, list(range(1, 17)))

# 06: repeated values, so the discard order is about positions and not values
write(6, [5, 5, 5, 9, 5, 5, 5, 5])

# 07: values at the ends of the range
write(7, [1, BIG, 1, BIG, 1, BIG, 1])

# ------------------------------------------------------------------ maximum

# 08: maximum N, cards numbered 1..N so the answer can be checked by hand
#     against the closed form if it is ever needed
write(8, list(range(1, NMAX + 1)))

# 09: maximum N, random values
write(9, [random.randint(1, BIG) for _ in range(NMAX)])

# 10: maximum N, every card the same. The discard order is then a pure test
#     of the simulation length, and the survivor is fixed.
write(10, [777] * NMAX)

# 11: maximum N, values at the top of the range, so the output is at its
#     largest -- about 5.5 MB of ten-digit numbers
write(11, [random.randint(BIG - 999, BIG) for _ in range(NMAX)])

# 12: a power of two at full size, where every discard is on an even step
size = 1 << 18                                   # 262,144
write(12, [random.randint(1, BIG) for _ in range(size)])

# 13: one more than a power of two, the neighbouring case
write(13, [random.randint(1, BIG) for _ in range(size + 1)])

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    opath = "%s/output%02d.txt" % (OUT, i)
    with open(ipath) as f:
        n = int(f.readline())
    print("  case %02d: N = %-7s in %8d B  out %8d B"
          % (i, n, os.path.getsize(ipath), os.path.getsize(opath)))
