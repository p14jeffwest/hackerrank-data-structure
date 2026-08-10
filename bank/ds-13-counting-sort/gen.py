#!/usr/bin/env python3
"""Test case generator for ds-13-counting-sort.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Counting sort cannot be enforced by time, and the sizes reflect that
------------------------------------------------------------------
Measured on this container, sorting the same input two ways:

    n = 2,000,000, maxValue = 1,000,000 : counting 566 ms, Arrays.sort  874 ms
    n = 2,000,000, maxValue =     1,000 : counting 397 ms, Arrays.sort  590 ms
    n = 5,000,000, maxValue = 1,000,000 : counting 1219 ms, Arrays.sort 1972 ms

The gap is real -- counting sort is about 1.5 times faster -- and nowhere near
a factor that a time limit could turn into a pass/fail. At 5,000,000 the input
file alone is 34 MB, which is too large for a test set, and both solutions
still finish comfortably.

So n is capped at 1,000,000. A larger n would cost megabytes and buy nothing.
The requirement is stated in the constraints and assessed on the exam, the
same position as ds-13-merge-two.

What the cases DO check is that the counting sort itself is right, which is
where the mistakes are.

What the cases are built to catch
---------------------------------
  1. A count array of maxValue entries instead of maxValue + 1, so the
     largest value has nowhere to go. Cases 02 and 09 contain maxValue itself.

  2. Placing values from the FRONT rather than the back. That still sorts
     correctly for plain ints -- the values are indistinguishable -- so no
     case can catch it, and it is recorded as an exam point instead. It is
     the property radix sort in 13.5 depends on.

  3. Forgetting the prefix sum and emitting each value count[v] times. That
     also produces a correct answer for this problem; it is the other way to
     write a counting sort and it is fine.

  4. Assuming values start at 1, or that every value between 0 and maxValue
     occurs. Cases 03 and 04 are sparse and start at 0.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20261302)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

NMAX = 1_000_000
KMAX = 1_000_000


def write(idx, a, max_value):
    n = len(a)
    assert 1 <= n <= NMAX, "n out of range in case %d" % idx
    assert 0 <= max_value <= KMAX, "maxValue out of range in case %d" % idx
    assert all(0 <= v <= max_value for v in a), \
        "a value exceeds maxValue in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d %d\n" % (n, max_value))
        f.write(" ".join(map(str, a)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write(" ".join(map(str, sorted(a))) + "\n")


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's two examples, which use only 0, 1 and 2
write(0, [2, 0, 2, 1, 1, 0], 2)
write(1, [2, 2, 0], 2)

# 02 sample: maxValue itself appears, and so does 0. A count array sized
#            maxValue rather than maxValue + 1 runs off the end here.
write(2, [1000000, 0, 1000000, 500000, 0], 1000000)

# 03: a wide range with only a handful of values used, none of them adjacent
write(3, [999999, 3, 3, 700000, 1, 999999], 1000000)

# 04: every value the same, and that value is 0
write(4, [0] * 10, 5)

# 05: a single value
write(5, [7], 7)

# 06: already ascending, and already descending
write(6, list(range(0, 20)), 19)
write(7, list(range(19, -1, -1)), 19)

# 08: maxValue = 0, so every value must be 0
write(8, [0, 0, 0], 0)

# 09: the full value range with n far smaller, so the count array dwarfs the
#     input -- the case where counting sort is at its worst
write(9, sorted(random.sample(range(KMAX + 1), 50)), KMAX)

# 10: every value between 0 and 20 present exactly twice
write(10, [v for v in range(21) for _ in range(2)], 20)

# ------------------------------------------------------------------ maximum

# 11: the full size over the full value range -- about one occurrence each
write(11, [random.randint(0, KMAX) for _ in range(NMAX)], KMAX)

# 12: the full size over a narrow range, so each value occurs about a
#     thousand times
write(12, [random.randint(0, 1000) for _ in range(NMAX)], 1000)

# 13: the full size, every value identical
write(13, [123456] * NMAX, KMAX)

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open(ipath) as f:
        n, k = map(int, f.readline().split())
    print("  case %02d: n = %-8d maxValue = %-8d  in %8d B"
          % (i, n, k, os.path.getsize(ipath)))
