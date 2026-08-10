#!/usr/bin/env python3
"""Test case generator for ds-08-gcd.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What the cases are built to catch
---------------------------------
  1. A base case of b == 1 instead of b == 0, which is the natural guess if
     you think of the answer as "keep dividing until nothing divides". It
     happens to give the right answer whenever the last non-zero remainder is
     1, so coprime pairs pass and everything else fails.

  2. Assuming a >= b. The recursion sorts itself out -- if a < b then
     a % b == a and the next call has them the other way round -- but a
     solution that writes `a - b` style logic, or that swaps by hand and gets
     it wrong, breaks. Case 02 gives every pair in both orders.

  3. Equal arguments, and a value of 1 on either side.

  4. Recursion depth. The deepest inputs are consecutive Fibonacci numbers;
     case 05 uses the largest such pair below 10^9, which needs 44 calls.

Note what is NOT tested: whether the method is recursive. `while (b != 0)` is
a two-line loop and passes everything. As with ds-08-palindrome, the recursion
is asked for in the constraints and assessed on the exam.

Every file is ASCII with LF line endings.
"""
import random
import os
from math import gcd

random.seed(20260804)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
TMAX = 100_000


def depth(a, b):
    """How many calls Euclid's recursion makes, for the notes below."""
    n = 1
    while b:
        a, b = b, a % b
        n += 1
    return n


def write(idx, pairs):
    assert 1 <= len(pairs) <= TMAX, "T out of range in case %d" % idx
    for a, b in pairs:
        assert 1 <= a <= VMAX and 1 <= b <= VMAX, \
            "value out of range in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(pairs))
        for a, b in pairs:
            f.write("%d %d\n" % (a, b))
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for a, b in pairs:
            f.write("%d\n" % gcd(a, b))


# the Fibonacci numbers, which are the worst case for the recursion depth
fib = [1, 2]
while fib[-1] + fib[-2] <= VMAX:
    fib.append(fib[-1] + fib[-2])


# ---------------------------------------------------------------- hand-built

# 00 sample: the worked examples
write(0, [(48, 36), (17, 5)])

# 01 sample: one argument divides the other, and both are equal.
#            These are the cases where the recursion stops immediately.
write(1, [(12, 12), (100, 25), (25, 100), (7, 7), (1000000000, 1000000000)])

# 02 sample: every pair given both ways round. A solution that assumes
#            a >= b answers half of them wrongly; the correct recursion needs
#            no swap, because a % b is a when a < b.
write(2, [(48, 36), (36, 48), (17, 5), (5, 17), (100, 3), (3, 100)])

# 03: 1 on one side or the other, and the smallest values there are
write(3,
      [(1, 1), (1, 999999999), (999999999, 1), (1, 2), (2, 1), (2, 2)])

# 04: coprime pairs only. A solution whose base case is b == 1 rather than
#     b == 0 passes all of these and nothing else.
write(4, [(17, 5), (13, 7), (999999937, 2), (35, 24), (101, 100), (7, 12)])

# 05: consecutive Fibonacci numbers, the deepest recursion for a given size
write(5, [(fib[i + 1], fib[i]) for i in range(len(fib) - 1)])

# 06: powers of two, and one number a multiple of the other by a large factor
write(6, [(2 ** 29, 2 ** 15), (2 ** 29, 3), (999999999, 3), (999999999, 9),
          (536870912, 262144)])

# 07: pairs sharing a large known factor
cases = []
for _ in range(500):
    g = random.randint(2, 100000)
    x = random.randint(1, VMAX // g)
    y = random.randint(1, VMAX // g)
    cases.append((g * x, g * y))
write(7, cases)

# ------------------------------------------------------------------ maximum

# 08: T at its maximum, uniformly random
write(8, [(random.randint(1, VMAX), random.randint(1, VMAX))
          for _ in range(TMAX)])

# 09: T at its maximum, small values, where many pairs share factors
write(9, [(random.randint(1, 100), random.randint(1, 100))
          for _ in range(TMAX)])

# 10: T at its maximum, every pair a consecutive Fibonacci pair, so every
#     query goes to the maximum depth
write(10, [(fib[-1], fib[-2])] * TMAX)

# 11: T at its maximum, one side always 1
write(11, [(random.randint(1, VMAX), 1) if i % 2 == 0
           else (1, random.randint(1, VMAX)) for i in range(TMAX)])

# 12: T at its maximum, both sides equal
write(12, [(v, v) for v in
           (random.randint(1, VMAX) for _ in range(TMAX))])

# 13: T at its maximum, the smaller value always first
cases = []
for _ in range(TMAX):
    a = random.randint(1, VMAX)
    b = random.randint(1, VMAX)
    cases.append((min(a, b), max(a, b)))
write(13, cases)

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        t = int(f.readline())
        pairs = [tuple(map(int, f.readline().split())) for _ in range(t)]
    print("  case %02d: T = %-7s deepest recursion %3d"
          % (i, t, max(depth(a, b) for a, b in pairs)))
