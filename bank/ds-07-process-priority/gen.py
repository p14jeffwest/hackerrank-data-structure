#!/usr/bin/env python3
"""Test case generator for ds-07-process-priority.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

A note on the bounds
--------------------
This is the one problem so far where raising n had to be done carefully rather
than generously.

The number of queue operations is itself quadratic in the worst case. With
priorities 1, 2, ..., n the queue turns over completely before each run, so
the simulation performs n(n+1)/2 polls no matter how the "is anything better
still waiting?" test is implemented. At n = 1000 that is 500,500 polls, which
is fine; at n = 10,000 it would be 50 million and no approach that actually
simulates the queue would survive. Since the chapter is about queues, the
simulation has to stay, so n is capped at 1,000.

Within that cap the bound still separates two approaches:

  * the book's own answer walks the queue on every poll to look for a higher
    priority. That is O(n) per poll on top of O(n^2) polls, so O(n^3), and at
    n = 1000 it does not finish.
  * sorting the priorities once and keeping a pointer answers the same
    question in O(1), because the processes still queued are exactly the ones
    not yet run.

The book says as much in its own answer: "A better approach: counting the
number at each priority in advance, or managing the maximum with a
PriorityQueue, is more efficient."

What the cases are built to catch
---------------------------------
  1. The O(n) scan per poll. Cases 09 through 13 are large enough.
  2. Testing with >= instead of >. Equal priorities would then displace each
     other, and a queue of identical priorities circulates for ever -- this
     shows as a timeout, not a wrong answer. Case 02 is published for it.
  3. Counting the run order from 0 instead of 1.

Every file is ASCII with LF line endings.
"""
import random
import os
from collections import deque

random.seed(20260703)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

PMAX = 1_000_000
NMAX = 1_000
TOTAL = 20_000


def solve(priority, target):
    """Reference model: the simulation, with the maximum read off a sorted copy."""
    n = len(priority)
    order_source = sorted(priority)
    queue = deque(range(n))
    remaining = n - 1
    order = 0
    while queue:
        current = queue.popleft()
        if priority[current] < order_source[remaining]:
            queue.append(current)
        else:
            order += 1
            remaining -= 1
            if current == target:
                return order
    return -1


def write(idx, cases):
    total = sum(len(p) for p, _ in cases)
    assert 1 <= len(cases) <= 100, "T out of range in case %d" % idx
    assert total <= TOTAL, "sum of n = %d exceeds the limit in case %d" % (total, idx)
    for priority, target in cases:
        assert 1 <= len(priority) <= NMAX
        assert 0 <= target < len(priority)
        assert all(1 <= p <= PMAX for p in priority)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(cases))
        for priority, target in cases:
            f.write("%d %d\n" % (len(priority), target))
            f.write(" ".join(map(str, priority)) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for priority, target in cases:
            f.write("%d\n" % solve(priority, target))


# ---------------------------------------------------------------- hand-built

# 00 sample: the two worked examples from the book
write(0, [([2, 1, 3, 2], 2), ([1, 1, 9, 1, 1, 1], 0)])

# 01 sample: a single process, and a target at each end of a short queue
write(1, [([5], 0), ([3, 1, 2], 0), ([3, 1, 2], 1), ([3, 1, 2], 2)])

# 02 sample: every priority the same. Nothing displaces anything, so the
#            processes run in their original order. A test written with >=
#            makes them displace each other and the queue never empties.
write(2, [([4, 4, 4, 4], 0), ([4, 4, 4, 4], 3), ([7, 7], 1)])

# 03: ties at the top, so several processes share the highest priority and
#     run in queue order among themselves
write(3, [
    ([9, 9, 1, 9], 3),
    ([1, 9, 9, 9], 0),
    ([5, 5, 5, 1, 5], 3),
])

# 04: strictly increasing, the worst shape for the number of polls
write(4, [(list(range(1, 21)), i) for i in [0, 10, 19]])

# 05: strictly decreasing, where every process runs the moment it is taken
write(5, [(list(range(20, 0, -1)), i) for i in [0, 10, 19]])

# 06: the target is the very last to run, and the very first
write(6, [
    ([1] + [2] * 9, 0),
    ([2] * 9 + [1], 9),
    ([1000000, 1, 1, 1], 0),
    ([1, 1, 1, 1000000], 3),
])

# 07: priorities at the ends of their range
write(7, [
    ([1, PMAX], 0), ([1, PMAX], 1),
    ([PMAX, PMAX, 1], 2),
    ([1, 1, PMAX, PMAX], 1),
])

# 08: many small random cases
cases = []
for _ in range(100):
    n = random.randint(1, 40)
    cases.append(([random.randint(1, 20) for _ in range(n)], random.randrange(n)))
write(8, cases)

# ------------------------------------------------------------------ maximum

# 09: 20 cases at the full n, strictly increasing -- 500,500 polls each.
#     The target is index 0, the LOWEST priority, which runs last. That
#     matters: the simulation stops as soon as the target runs, so a random
#     target usually ends the loop early and the case stops testing anything.
#     An earlier version did exactly that and no wrong variant failed it.
write(9, [(list(range(1, NMAX + 1)), 0) for _ in range(20)])

# 10: 20 cases at the full n, random priorities, with the target chosen to be
#     the process that runs LAST so that the whole simulation is performed
cases = []
for _ in range(20):
    p = [random.randint(1, PMAX) for _ in range(NMAX)]
    last = min(range(NMAX), key=lambda i: (p[i], -i))   # lowest priority, latest position
    cases.append((p, last))
write(10, cases)

# 11: 20 cases at the full n, priorities drawn from a tiny set so there are
#     long runs of ties. The target again runs last.
cases = []
for _ in range(20):
    p = [random.randint(1, 3) for _ in range(NMAX)]
    last = min(range(NMAX), key=lambda i: (p[i], -i))
    cases.append((p, last))
write(11, cases)

# 12: 20 cases at the full n, all priorities equal. Every process runs in
#     order, and a >= test loops for ever here.
write(12, [([500] * NMAX, NMAX - 1) for _ in range(20)])

# 13: T at its maximum, 100 cases of 200
cases = []
for _ in range(100):
    n = 200
    p = list(range(1, n + 1))
    random.shuffle(p)
    cases.append((p, random.randrange(n)))
write(13, cases)

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        t = int(f.readline())
        total = 0
        for _ in range(t):
            total += int(f.readline().split()[0])
            f.readline()
    print("  case %02d: T = %-5s sum n %6d" % (i, t, total))
