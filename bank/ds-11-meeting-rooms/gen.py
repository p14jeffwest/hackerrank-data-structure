#!/usr/bin/env python3
"""Test case generator for ds-11-meeting-rooms.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Note on the Korean counterpart
------------------------------
dsa-13-meeting-rooms has the same name and is a different problem: it asks for
the largest number of meetings that fit in ONE room, which is a greedy
selection sorted by end time and uses no heap. That is why it lives in the
Korean sorting chapter. This one asks for the smallest number of ROOMS, which
is the heap problem, and nothing is shared between them.

What the cases are built to catch
---------------------------------
  1. Counting overlaps by comparing every pair, O(n^2). Cases 09 through 13
     are large enough to time out.

  2. Treating a meeting that ends exactly when another starts as overlapping.
     That asks for an extra room every time two meetings meet end to start.
     Case 02 is a chain of meetings doing precisely that and needs one room;
     the strict comparison asks for as many rooms as meetings.

  3. Not sorting by start time. Case 03 gives the meetings in an order that
     makes the unsorted answer wrong.

  4. Reporting the number of rooms in use at the end rather than the largest
     number ever in use. The heap in the reference never shrinks, which is
     what makes its final size the answer -- a solution that polls every
     finished meeting instead of at most one has to track the maximum itself.

The model computes the answer by a sweep over the endpoints, so it shares no
reasoning with the heap solution.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20261102)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

TMAX_TIME = 1_000_000_000
NMAX = 200_000
TOTAL = 200_000


def rooms_needed(meetings):
    """Sweep the endpoints. A meeting ending at time t frees its room before a
    meeting starting at t takes one, so ends are processed first at equal
    times."""
    events = []
    for s, e in meetings:
        events.append((s, 1))
        events.append((e, -1))
    events.sort(key=lambda x: (x[0], x[1]))     # -1 before +1 at the same time
    best = cur = 0
    for _, delta in events:
        cur += delta
        best = max(best, cur)
    return best


def write(idx, cases):
    total = sum(len(m) for m in cases)
    assert 1 <= len(cases) <= 500, "T out of range in case %d" % idx
    assert total <= TOTAL, "meeting total %d exceeds the limit in case %d" % (total, idx)
    for meetings in cases:
        assert 1 <= len(meetings) <= NMAX
        for s, e in meetings:
            assert 0 <= s < e <= TMAX_TIME, "bad meeting in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(cases))
        for meetings in cases:
            f.write("%d\n" % len(meetings))
            for s, e in meetings:
                f.write("%d %d\n" % (s, e))
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for meetings in cases:
            f.write("%d\n" % rooms_needed(meetings))


def shuffled(meetings):
    m = list(meetings)
    random.shuffle(m)
    return m


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's two examples
write(0, [[(0, 30), (5, 10), (15, 20)], [(7, 10), (2, 4)]])

# 01 sample: a single meeting, and two that are identical
write(1, [[(0, 1)], [(5, 9), (5, 9)], [(0, 1000000000)]])

# 02 sample: meetings that meet end to start. They do NOT overlap, so one room
#            holds all of them. A solution comparing with < instead of <=
#            asks for one room per meeting.
write(2, [
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)],
    [(10, 20), (20, 30)],
    [(0, 5), (5, 10), (3, 8)],        # the third one does overlap: 2 rooms
])

# 03: the meetings given in an order that punishes not sorting
write(3, [
    [(20, 30), (0, 10), (5, 25), (12, 15)],
    [(100, 200), (0, 50), (150, 250), (25, 175)],
])

# 04: everything overlapping everything, so the answer is n
write(4, [[(0, 100)] * 1, [(0, 100), (1, 99), (2, 98), (3, 97)],
          [(i, 1000) for i in range(10)]])

# 05: nothing overlapping at all, so the answer is 1
write(5, [[(2 * i, 2 * i + 1) for i in range(50)],
          shuffled([(2 * i, 2 * i + 1) for i in range(50)])])

# 06: a staircase where each meeting overlaps only its neighbour
write(6, [[(i, i + 2) for i in range(30)]])

# 07: times at the ends of their range
write(7, [[(0, 1000000000)],
          [(0, 500000000), (500000000, 1000000000)],
          [(0, 500000001), (500000000, 1000000000)]])

# 08: many small independent cases
cases = []
for _ in range(300):
    n = random.randint(1, 12)
    m = []
    for _ in range(n):
        s = random.randint(0, 100)
        m.append((s, s + random.randint(1, 30)))
    cases.append(m)
write(8, cases)

# ------------------------------------------------------------------ maximum


def random_meetings(n, span, length_hi):
    m = []
    for _ in range(n):
        s = random.randint(0, span)
        m.append((s, s + random.randint(1, length_hi)))
    return m


# 09: the full count, short meetings over a wide span -- few rooms needed, so
#     the heap stays small and only the sort costs anything
write(9, [random_meetings(NMAX, TMAX_TIME, 1000)])

# 10: the full count, long meetings over a narrow span -- almost everything
#     overlaps and the heap holds nearly all of them
write(10, [random_meetings(NMAX, 1000, 1000)])

# 11: the full count, all meetings identical, so every one needs its own room
write(11, [[(1000, 2000)] * NMAX])

# 12: the full count laid end to start in a single chain, shuffled on input.
#     One room holds them all, and a strict comparison asks for 200,000.
write(12, [shuffled([(i, i + 1) for i in range(NMAX)])])

# 13: T at its maximum, a mixture
cases = []
budget = TOTAL
for i in range(500):
    n = max(1, min(budget - (500 - i - 1), random.randint(1, 800)))
    budget -= n
    style = i % 3
    if style == 0:
        cases.append(random_meetings(n, 10_000, 500))
    elif style == 1:
        cases.append(shuffled([(j, j + 1) for j in range(n)]))
    else:
        cases.append([(0, 1000)] * n)
write(13, cases)

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open("%s/output%02d.txt" % (OUT, i)) as f:
        vals = [int(x) for x in f.read().split()]
    print("  case %02d: T = %-5d largest answer %7d  in %8d B"
          % (i, len(vals), max(vals), os.path.getsize(ipath)))
