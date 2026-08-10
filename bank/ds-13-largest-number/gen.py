#!/usr/bin/env python3
"""Test case generator for ds-13-largest-number.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What the cases are built to catch
---------------------------------
  1. Sorting by value instead of by the concatenation. 3 and 30 are the
     smallest example -- "330" beats "303", so 3 goes first even though 30 is
     the larger number. Case 02 is published as a sample and is built from
     numbers that are prefixes of one another, which is the only situation
     where the two orders disagree.

  2. Missing the all-zeros case. Concatenating gives "000...", and the answer
     is "0". Case 03 is published for it.

  3. Comparing by string alone, without the concatenation. "9" > "34" as text
     and also in this order, so that mistake survives many inputs -- case 02
     is where it does not.

  4. Building the answer as a number rather than a string. The concatenation
     of 10,000 ten-digit numbers is 100,000 digits long, so no numeric type
     holds it. Nothing can force it, but the large cases make the answer
     obviously out of range.

The model sorts with functools.cmp_to_key on the same concatenation rule.
That is the same reasoning as the solution, which is unavoidable here -- the
required order is defined by the comparison.

Every file is ASCII with LF line endings.
"""
import random
import os
from functools import cmp_to_key

random.seed(20261304)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
NMAX = 100_000


def compare(a, b):
    """Negative means a comes FIRST. a goes first when a+b is the larger
    concatenation.

    The sign here was inverted in the first version of this generator, which
    sorted ascending and produced "3033459" for the book's own example instead
    of "9534330". The Java solution disagreed on the very first case, which is
    why both are always run against each other before anything is trusted.
    """
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0


def solve(nums):
    s = sorted((str(v) for v in nums), key=cmp_to_key(compare))
    if s[0] == "0":
        return "0"
    return "".join(s)


def write(idx, nums):
    n = len(nums)
    assert 1 <= n <= NMAX, "n out of range in case %d" % idx
    assert all(0 <= v <= VMAX for v in nums), "value out of range in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % n)
        f.write(" ".join(map(str, nums)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write(solve(nums) + "\n")


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's three examples
write(0, [3, 30, 34, 5, 9])
write(1, [10, 2])

# 02 sample: numbers that are prefixes of one another, which is the ONLY
#            situation where sorting by value and sorting by concatenation
#            disagree. 02 must be published: by value the answer would be
#            "302303", by concatenation it is "330302".
write(2, [3, 30, 302, 303])

# 03 sample: every number is 0, so the answer is "0" and not "0000"
write(3, [0, 0, 0, 0])

# 04: a single number, including a single 0
write(4, [7])
write(5, [0])

# 06: one 0 among non-zero numbers, where the 0 goes last
write(6, [0, 5, 0, 12])

# 07: repeated digits, where the tie rule has to be consistent
write(7, [1, 11, 111, 1111])

# 08: numbers built from the same digit in different lengths
write(8, [8, 88, 888, 8888, 89])

# 09: the ends of the value range
write(9, [1000000000, 999999999, 1, 0])

# 10: every number identical
write(10, [42] * 8)

# 11: a spread of digit lengths, shuffled
nums = [9, 90, 900, 91, 19, 1, 99, 909, 990]
random.shuffle(nums)
write(11, nums)

# ------------------------------------------------------------------ maximum

# 12: the full count, random over the whole range. The answer is about
#     900,000 digits long, so no numeric type can hold it.
write(12, [random.randint(0, VMAX) for _ in range(NMAX)])

# 13: the full count drawn from numbers that are prefixes of one another, so
#     almost every comparison is one where value order and concatenation
#     order disagree
pool = [3, 30, 300, 3000, 34, 340, 5, 50, 500, 9, 90, 900, 1, 10, 100]
write(13, [random.choice(pool) for _ in range(NMAX)])

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open(ipath) as f:
        n = int(f.readline())
    with open("%s/output%02d.txt" % (OUT, i)) as f:
        digits = len(f.readline().strip())
    print("  case %02d: n = %-7d answer %8d digits" % (i, n, digits))
