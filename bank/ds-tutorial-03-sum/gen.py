#!/usr/bin/env python3
"""Test case generator for ds-tutorial-03-sum.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Design notes
------------
The lesson of this problem is that the running total needs `long` while the
individual values fit in `int`. So the set is deliberately split:

  * cases whose sum stays inside int  -> an int solution passes these
  * cases whose sum leaves int        -> an int solution silently returns junk

Case 02 is small, readable, and already overflows (three billion), so it is
published as a sample. A student who runs it before submitting sees a negative
number come out of three positive inputs, which is a better explanation of
overflow than any paragraph.

Cases 10 through 13 also cover the maximum size, N = 100,000, in both sign
directions.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20260809)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

LIM = 1_000_000_000
INT_MAX = 2_147_483_647
INT_MIN = -2_147_483_648


def write(idx, nums):
    n = len(nums)
    assert 1 <= n <= 100_000, "N out of range in case %d" % idx
    assert all(-LIM <= x <= LIM for x in nums), "value out of range in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % n)
        f.write(" ".join(map(str, nums)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("%d\n" % sum(nums))


cases = [
    # 00 sample: the worked example from the statement
    [10, 20, 30, 40],
    # 01 sample: smallest possible N, and a negative value
    [-7],
    # 02 sample: overflows int immediately, and small enough to check by hand.
    #            Published on purpose -- three positive numbers producing a
    #            negative answer is the clearest possible demonstration.
    [LIM, LIM, LIM],
    # 03: consecutive small values
    [1, 2, 3, 4, 5],
    # 04: all negative
    [-1, -2, -3],
    # 05: sums to exactly zero
    [5, -5, 100, -100, 0],
    # 06: just under the int ceiling, so an int solution still passes here
    [LIM, LIM],
    # 07: overflow in the negative direction
    [-LIM, -LIM, -LIM],
    # 08: nothing but zeros
    [0] * 10,
    # 09: a single maximum value
    [LIM],
]
for i, c in enumerate(cases):
    write(i, c)

# 10: maximum size, every value at the maximum -> sum 1e14
write(10, [LIM] * 100_000)

# 11: maximum size, every value at the minimum -> sum -1e14
write(11, [-LIM] * 100_000)

# 12: maximum size, random values
write(12, [random.randint(-LIM, LIM) for _ in range(100_000)])

# 13: maximum size, alternating signs so the total lands on zero
write(13, [LIM if i % 2 == 0 else -LIM for i in range(100_000)])

# 14: mid-size random
write(14, [random.randint(-LIM, LIM) for _ in range(1000)])

# Self-check: report how many cases an int accumulator would survive.
# This is the number the UPLOAD.md verification table should agree with.
total = 15
survives = 0
for i in range(total):
    with open("%s/input%02d.txt" % (IN, i)) as f:
        f.readline()
        nums = list(map(int, f.readline().split()))
    acc = 0
    for x in nums:
        acc = (acc + x + 2**31) % 2**32 - 2**31   # simulate int wraparound
    if acc == sum(nums):
        survives += 1

print("generated %d cases" % total)
print("an int accumulator would score %d/%d" % (survives, total))
