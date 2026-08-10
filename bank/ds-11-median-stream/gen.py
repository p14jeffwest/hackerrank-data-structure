#!/usr/bin/env python3
"""Test case generator for ds-11-median-stream.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What the cases are built to catch
---------------------------------
  1. Keeping every value in a list and sorting it on each query. That is
     O(n log n) per query and O(M n log n) overall; cases 09 through 13 have
     enough queries against a large stream to time it out.

  2. Inserting into a sorted list to keep it ordered, which is O(n) per add.
     Same cases catch it.

  3. Not rebalancing after an add, so the two halves drift apart and the
     median comes from the wrong heap. Case 02 feeds a strictly increasing
     stream, where every value goes to the same side.

  4. Halving the sum of the two middles as ints. Two values near 10^9 sum past
     the int range. Case 03 is built from values near the top of the range.

  5. Getting the parity wrong -- reading the median from the wrong heap when
     the count is odd.

The model keeps a sorted list and answers by index, which shares nothing with
the two-heap method.

Every file is ASCII with LF line endings.
"""
import random
import os
import bisect

random.seed(20261104)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

VMAX = 1_000_000_000
MMAX = 200_000


def render(total):
    """Format 2*median exactly, without floating point.

    The median is either an integer or an integer plus a half, so the printed
    form is decided by the parity of the sum of the two middles. Doing it on
    integers avoids any question about what the grader's double prints, and
    it handles the sign correctly -- a naive sum/2 would print 0.5 for a
    median of -0.5.
    """
    sign = "-" if total < 0 else ""
    a = abs(total)
    return "%s%d%s" % (sign, a // 2, ".0" if a % 2 == 0 else ".5")


def run(commands):
    data = []
    out = []
    for c in commands:
        parts = c.split()
        if parts[0] == "add":
            bisect.insort(data, int(parts[1]))
        elif parts[0] == "median":
            if not data:
                out.append("empty")
            else:
                n = len(data)
                total = 2 * data[n // 2] if n % 2 else data[n // 2 - 1] + data[n // 2]
                out.append(render(total))
        elif parts[0] == "size":
            out.append(str(len(data)))
        else:
            raise ValueError(c)
    return out


def write(idx, commands):
    assert 1 <= len(commands) <= MMAX, "M out of range in case %d" % idx
    for c in commands:
        if c.startswith("add"):
            v = int(c.split()[1])
            assert -VMAX <= v <= VMAX, "value out of range in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(commands))
        f.write("\n".join(commands) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("".join(line + "\n" for line in run(commands)))


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's own example
write(0, ["add 1", "add 2", "median", "add 3", "median", "size"])

# 01 sample: a median before anything is added, one value, and the parity
#            alternating on every step
write(1, ["median", "size",
          "add 5", "median", "add 5", "median", "add 1", "median",
          "add 9", "median", "add 7", "median", "size"])

# 02 sample: a strictly increasing stream, where every new value belongs to
#            the larger half. Without rebalancing the halves drift apart and
#            the median is read from the wrong heap almost at once.
write(2, [c for i in range(1, 11) for c in ("add %d" % i, "median")])

# 03: values near the top of the range, so the two middles sum past the int
#     range and halving them as ints goes wrong
write(3, ["add 1000000000", "median", "add 999999999", "median",
          "add 999999998", "median", "add 1000000000", "median"])

# 04: a strictly decreasing stream, the mirror of case 02
write(4, [c for i in range(10, 0, -1) for c in ("add %d" % i, "median")])

# 05: negatives, including a median of exactly -0.5
write(5, ["add -1", "median", "add 0", "median", "add -2", "median",
          "add 1", "median", "add -1000000000", "median"])

# 06: every value the same
write(6, [c for _ in range(12) for c in ("add 7", "median")])

# 07: values arriving alternately far below and far above the middle
cmds = []
for i in range(20):
    cmds.append("add %d" % (-1000 * i if i % 2 == 0 else 1000 * i))
    cmds.append("median")
write(7, cmds)

# 08: many adds and a single median at the end
write(8, ["add %d" % random.randint(-VMAX, VMAX) for _ in range(2000)]
        + ["median", "size"])

# ------------------------------------------------------------------ maximum


def mixed(m, hi, median_share):
    cmds, n = [], 0
    while len(cmds) < m:
        if n == 0 or random.random() > median_share:
            cmds.append("add %d" % random.randint(-hi, hi))
            n += 1
        else:
            cmds.append("median")
    return cmds[:m]


# 09: maximum M, half adds and half medians
write(9, mixed(MMAX, VMAX, 0.5))

# 10: maximum M, mostly medians against a stream that keeps growing -- the
#     worst case for anything that re-sorts on each query
write(10, mixed(MMAX, VMAX, 0.8))

# 11: maximum M, ascending values throughout, half medians
cmds, n = [], 0
while len(cmds) < MMAX:
    if n == 0 or random.random() > 0.5:
        n += 1
        cmds.append("add %d" % n)
    else:
        cmds.append("median")
write(11, cmds[:MMAX])

# 12: maximum M, values drawn from a tiny set so ties dominate
write(12, mixed(MMAX, 3, 0.5))

# 13: maximum M, values at the ends of the range so the two middles are far
#     apart and their sum is large
cmds, n = [], 0
while len(cmds) < MMAX:
    if n == 0 or random.random() > 0.4:
        n += 1
        cmds.append("add %d" % random.choice([-VMAX, VMAX, VMAX - 1, -VMAX + 1]))
    else:
        cmds.append("median")
write(13, cmds[:MMAX])

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        m = int(f.readline())
        cmds = [f.readline().rstrip("\n") for _ in range(m)]
    adds = sum(1 for c in cmds if c.startswith("add"))
    meds = sum(1 for c in cmds if c == "median")
    print("  case %02d: M = %-7s adds %7d  medians %7d" % (i, m, adds, meds))
