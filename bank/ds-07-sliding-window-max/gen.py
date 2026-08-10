#!/usr/bin/env python3
"""Test case generator for ds-07-sliding-window-max.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What the cases are built to catch
---------------------------------
  1. Recomputing the maximum of each window from scratch, O(n*k). Case 10 has
     n = 500,000 with k = n/2, which is the worst pairing: about 6 * 10^10
     comparisons. Cases 11 through 13 are large too.

  2. Storing values in the deque instead of indices. Expiry is a question
     about position, so a deque of values cannot tell whether its front has
     left the window. Any case where the maximum falls out of the window
     catches it -- 02 in particular, which is strictly decreasing.

  3. An off-by-one in the expiry test. The front leaves the window when its
     index is below i - k + 1, not at it. Cases 01 and 04 pin both ends.

  4. Emitting an answer before the first window is complete, or missing the
     last one. Every case checks the count implicitly, since a short line is
     a wrong line.

A note on what is NOT a mistake: dropping the rear on `<` rather than `<=`
leaves equal values in the deque and still reports the right maximum. The
deque grows a little, and nothing else changes. No test can separate the two,
and none tries to.

Every file is ASCII with LF line endings.
"""
import random
import os
from collections import deque

random.seed(20260704)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

LIM = 1_000_000_000
NMAX = 500_000


def solve(nums, k):
    """Reference model: the same monotonic deque."""
    window = deque()
    out = []
    for i, v in enumerate(nums):
        while window and window[0] < i - k + 1:
            window.popleft()
        while window and nums[window[-1]] <= v:
            window.pop()
        window.append(i)
        if i >= k - 1:
            out.append(nums[window[0]])
    return out


def write(idx, cases):
    total = sum(len(a) for a, _ in cases)
    assert 1 <= len(cases) <= 500, "T out of range in case %d" % idx
    assert total <= NMAX, "sum of n = %d exceeds the limit in case %d" % (total, idx)
    for nums, k in cases:
        assert 1 <= len(nums) <= NMAX
        assert 1 <= k <= len(nums), "k out of range in case %d" % idx
        assert all(-LIM <= x <= LIM for x in nums)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(cases))
        for nums, k in cases:
            f.write("%d %d\n" % (len(nums), k))
            f.write(" ".join(map(str, nums)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for nums, k in cases:
            result = solve(nums, k)
            assert len(result) == len(nums) - k + 1
            f.write(" ".join(map(str, result)) + "\n")


def rnd(n):
    return [random.randint(-LIM, LIM) for _ in range(n)]


# ---------------------------------------------------------------- hand-built

BOOK = [1, 3, -1, -3, 5, 3, 6, 7]

# 00 sample: the book's own example, and the same array at the two extreme
#            window sizes
write(0, [(BOOK, 3), (BOOK, 1), (BOOK, 8)])

# 01 sample: k = 1 and k = n on several shapes. k = 1 means every element is
#            its own answer; k = n means one answer for the whole array.
write(1, [
    ([5], 1),
    ([3, 1, 2], 1),
    ([3, 1, 2], 3),
    ([3, 1, 2], 2),
    ([-1, -2, -3], 1),
    ([-1, -2, -3], 3),
])

# 02 sample: strictly decreasing. The maximum is always the element that is
#            about to leave the window, so a deque holding values instead of
#            indices cannot expire it and reports the wrong answer from the
#            second window onward.
write(2, [
    ([9, 8, 7, 6, 5], 2),
    ([9, 8, 7, 6, 5], 3),
    ([5, 6, 7, 8, 9], 3),
    ([4, 4, 4, 4, 4], 3),
])

# 03: the maximum repeated, so several indices tie for it inside one window
write(3, [
    ([7, 3, 7, 3, 7], 3),
    ([1, 9, 9, 1, 9, 9, 1], 4),
    ([2, 2, 1, 2, 2], 2),
])

# 04: windows sliding over a single spike, which walks through every position
#     of the window in turn
write(4, [([0, 0, 0, 9, 0, 0, 0], k) for k in [1, 2, 3, 4, 7]])

# 05: values at the ends of the range, and all-negative arrays
write(5, [
    ([LIM, -LIM, LIM, -LIM], 2),
    ([-LIM, -LIM + 1, -LIM + 2], 2),
    ([LIM] * 5, 3),
    ([0], 1),
])

# 06: many small random cases
cases = []
for _ in range(400):
    n = random.randint(1, 20)
    cases.append((rnd(n), random.randint(1, n)))
write(6, cases)

# 07: T at its maximum, sum of n at its maximum
cases = []
remaining = NMAX
for i in range(500):
    n = 1 if i == 499 else max(1, min(remaining - (500 - i - 1), random.randint(1, 1900)))
    remaining -= n
    cases.append((rnd(n), random.randint(1, n)))
write(7, cases)

# ------------------------------------------------------------------ maximum

# 08: one maximum array with k = 1, so the output is as long as the input
write(8, [(rnd(NMAX), 1)])

# 09: one maximum array with k = n, so there is a single answer but the whole
#     array still has to be read
write(9, [(rnd(NMAX), NMAX)])

# 10: the worst pairing for a brute-force scan: k = n/2 gives n/2 windows of
#     n/2 elements each, about 6 * 10^10 comparisons
write(10, [(rnd(NMAX), NMAX // 2)])

# 11: strictly decreasing at full size. The deque fills to k indices and
#     never pops from the rear, which is its worst case for memory. k is a
#     quarter of n so the brute-force cost stays high as well.
write(11, [([NMAX - i for i in range(NMAX)], NMAX // 4)])

# 12: strictly increasing at full size. Every new element clears the deque, so
#     it holds one index throughout -- the opposite shape.
write(12, [([i for i in range(NMAX)], NMAX // 3)])

# 13: full size, random, with a large window
write(13, [(rnd(NMAX), 100_000)])

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    opath = "%s/output%02d.txt" % (OUT, i)
    with open(ipath) as f:
        t = int(f.readline())
        work = 0
        for _ in range(t):
            n, k = map(int, f.readline().split())
            f.readline()
            # a brute-force scan costs (n - k + 1) windows of k elements.
            # NOT n * k: at k = n there is only one window, which is why an
            # earlier version of case 09 looked expensive and was not.
            work += (n - k + 1) * k
    print("  case %02d: T = %-5s brute-force cost %14d  out %8d B"
          % (i, t, work, os.path.getsize(opath)))
