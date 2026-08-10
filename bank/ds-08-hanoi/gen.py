#!/usr/bin/env python3
"""Test case generator for ds-08-hanoi.

The seed is fixed -- in fact nothing here is random, since the answer for a
given N is unique.

    python3 gen.py

What the cases are built to catch
---------------------------------
  1. Printing each move with System.out.println. At N = 20 that is 1,048,575
     separate writes and it does not finish. Cases 11 through 13 are large
     enough; the small ones are not, so the mistake shows as a partial score.

  2. Rotating the pegs wrongly in the two recursive calls. The first call
     must use the TARGET peg as its spare and the second must use the
     ORIGINAL peg. Any other arrangement still prints 2^n - 1 lines -- so the
     count is right and only the moves are wrong, which is why the move list
     is part of the answer and not just the total.

  3. A base case of n == 1 that forgets to print, or an off-by-one in the
     count.

The output is the largest of any problem in this set: about 7.3 MB for N = 20.

Every file is ASCII with LF line endings.
"""
import os

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

NMAX = 20


def hanoi(n, frm, to, aux, out):
    """Reference model, written iteratively over an explicit stack.

    A recursive model would be clearer, but n = 20 means 2^20 frames and
    Python's default recursion limit is 1,000. The stack here holds the same
    frames the recursion would, with a flag saying whether the frame has
    already emitted its own move.
    """
    stack = [(n, frm, to, aux, False)]
    while stack:
        n, frm, to, aux, expanded = stack.pop()
        if n == 0:
            continue
        if expanded:
            out.append("%s -> %s" % (frm, to))
        else:
            # push in reverse, so they come off in the order 1, 2, 3
            stack.append((n - 1, aux, to, frm, False))
            stack.append((n, frm, to, aux, True))
            stack.append((n - 1, frm, aux, to, False))


def write(idx, n):
    assert 1 <= n <= NMAX, "N out of range in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % n)
    moves = []
    hanoi(n, "A", "C", "B", moves)
    assert len(moves) == 2 ** n - 1, "move count wrong for n = %d" % n
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("%d\n" % (2 ** n - 1))
        f.write("\n".join(moves) + "\n")


# 00 sample: the worked example, three disks in seven moves
write(0, 3)

# 01 sample: one disk, the smallest case there is
write(1, 1)

# 02 sample: two disks, the smallest case where the auxiliary peg is used
write(2, 2)

# 03 through 10: every size up the middle of the range
for idx, n in enumerate([4, 5, 6, 8, 10, 12, 14, 16], start=3):
    write(idx, n)

# 11, 12, 13: the sizes where the volume of output starts to matter
write(11, 18)
write(12, 19)
write(13, 20)

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    opath = "%s/output%02d.txt" % (OUT, i)
    with open(ipath) as f:
        n = int(f.readline())
    print("  case %02d: N = %-3d moves %8d  out %8d B"
          % (i, n, 2 ** n - 1, os.path.getsize(opath)))
