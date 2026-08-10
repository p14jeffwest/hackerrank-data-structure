#!/usr/bin/env python3
"""Test case generator for ds-06-queue-two-stacks.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Design notes
------------
The book asks for amortized O(1) dequeue. That is the one requirement here
that can actually be checked, and it is checked by the clock: refilling the
outbox on every dequeue -- or worse, pouring everything back afterwards --
costs O(n) per call, and with 200,000 commands over a queue that stays large
the total is quadratic.

What the cases are built to catch:

  1. Refilling on every dequeue instead of only when the outbox is empty.
     This is wrong twice over. It buries older elements under newer ones, so
     the ORDER breaks as soon as an enqueue lands between two dequeues; and it
     is O(n) per call. Cases 03 and 06 interleave enqueues with dequeues for
     exactly this.

  2. Moving everything back to the inbox after each dequeue. The order stays
     correct, so it fails only on time. Cases 09 through 13 are large enough.

  3. isEmpty looking at one stack instead of both. Cases 04 and 05 leave
     elements sitting in the inbox while the outbox is empty, and the other
     way round.

  4. Not handling a dequeue on an empty queue.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20260604)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

BIG = 1_000_000_000
QMAX = 200_000


def run(commands):
    """Reference model of the driver, using a plain list as the queue."""
    queue = []
    out = []
    head = 0                      # index of the front, to keep this O(1)
    for c in commands:
        parts = c.split()
        op = parts[0]
        if op == "enqueue":
            queue.append(int(parts[1]))
        elif op == "dequeue":
            if head < len(queue):
                out.append(str(queue[head]))
                head += 1
            else:
                out.append("empty")
        elif op == "empty":
            out.append("1" if head >= len(queue) else "0")
        else:
            raise ValueError("unknown command: " + c)
    return out


def write(idx, commands):
    assert 1 <= len(commands) <= QMAX, "Q out of range in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(commands))
        f.write("\n".join(commands) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("".join(line + "\n" for line in run(commands)))


def value():
    return random.randint(1, BIG)


# ---------------------------------------------------------------- hand-built

# 00 sample: the sequence the book uses to describe the behaviour
write(0, [
    "enqueue 1", "enqueue 2", "enqueue 3",
    "dequeue",
    "enqueue 4",
    "dequeue", "dequeue", "dequeue",
    "empty", "dequeue", "empty",
])

# 01 sample: FIFO order over a straight run, so the answers come out in the
#            order they went in and not reversed
write(1, ["enqueue %d" % i for i in range(1, 8)] +
         ["dequeue"] * 7 + ["empty"])

# 02 sample: an empty queue touched in every way, and refilled afterwards
write(2, [
    "empty", "dequeue", "dequeue",
    "enqueue 5", "empty", "dequeue", "empty", "dequeue",
    "enqueue 6", "enqueue 7", "dequeue", "empty", "dequeue", "empty",
])

# 03 sample: an enqueue landing between two dequeues. This is where refilling
#            the outbox unconditionally reverses the order: 2 must come out
#            before 9, not after it.
write(3, [
    "enqueue 1", "enqueue 2", "enqueue 3",
    "dequeue",
    "enqueue 9",
    "dequeue", "dequeue", "dequeue", "empty",
])

# 04: elements sitting in the inbox while the outbox is empty, so an isEmpty
#     that only looks at the outbox answers wrongly
write(4, ["enqueue 1", "enqueue 2", "empty", "dequeue", "empty",
          "enqueue 3", "empty", "dequeue", "dequeue", "empty"])

# 05: the other way round -- the outbox holds everything and the inbox is
#     empty, so an isEmpty that only looks at the inbox answers wrongly
write(5, ["enqueue 1", "enqueue 2", "enqueue 3", "dequeue",
          "empty", "empty", "dequeue", "empty", "dequeue", "empty"])

# 06: tight interleaving, one enqueue and one dequeue at a time, keeping the
#     queue shallow but forcing a refill decision on nearly every call
cmds = []
for i in range(1, 400):
    cmds.append("enqueue %d" % i)
    cmds.append("dequeue")
    if i % 50 == 0:
        cmds.append("empty")
write(6, cmds)

# 07: batches -- fill a little, drain a little, so the refill boundary is
#     crossed over and over
cmds = []
while len(cmds) < 3000:
    for _ in range(random.randint(1, 12)):
        cmds.append("enqueue %d" % value())
    for _ in range(random.randint(1, 12)):
        cmds.append("dequeue")
    cmds.append("empty")
write(7, cmds[:3000])

# 08: more dequeues than enqueues, so the queue runs dry repeatedly
cmds = []
while len(cmds) < 3000:
    for _ in range(random.randint(1, 4)):
        cmds.append("enqueue %d" % value())
    for _ in range(random.randint(1, 10)):
        cmds.append("dequeue")
write(8, cmds[:3000])

# ------------------------------------------------------------------ maximum

half = QMAX // 2

# 09: fill completely, then drain completely. The queue is at its deepest for
#     the whole second half, which is the worst case for any solution that
#     touches every element on each dequeue.
write(9, ["enqueue %d" % value() for _ in range(half)] + ["dequeue"] * half)

# 10: fill completely, then alternate one dequeue with one enqueue, so the
#     queue stays at its deepest for the whole run
cmds = ["enqueue %d" % value() for _ in range(half)]
while len(cmds) < QMAX:
    cmds.append("dequeue")
    cmds.append("enqueue %d" % value())
write(10, cmds[:QMAX])

# 11: a large queue held throughout, with dequeues arriving in bursts
cmds = ["enqueue %d" % value() for _ in range(60000)]
while len(cmds) < QMAX:
    for _ in range(random.randint(1, 30)):
        cmds.append("dequeue")
    for _ in range(random.randint(1, 32)):
        cmds.append("enqueue %d" % value())
write(11, cmds[:QMAX])

# 12: maximum Q of tight interleaving over a deep queue, plus empty checks
cmds = ["enqueue %d" % value() for _ in range(40000)]
i = 0
while len(cmds) < QMAX:
    cmds.append("dequeue")
    cmds.append("enqueue %d" % value())
    i += 1
    if i % 500 == 0:
        cmds.append("empty")
write(12, cmds[:QMAX])

# 13: maximum Q, fully random mix
cmds = []
depth = 0
while len(cmds) < QMAX:
    r = random.random()
    if r < 0.55:
        cmds.append("enqueue %d" % value())
        depth += 1
    elif r < 0.93:
        cmds.append("dequeue")
        depth = max(0, depth - 1)
    else:
        cmds.append("empty")
write(13, cmds[:QMAX])

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        q = int(f.readline())
        cmds = [f.readline().rstrip("\n") for _ in range(q)]
    depth = best = 0
    for c in cmds:
        if c.startswith("enqueue"):
            depth += 1
            best = max(best, depth)
        elif c.startswith("dequeue"):
            depth = max(0, depth - 1)
    print("  case %02d: Q = %-7s max queue depth %7d" % (i, q, best))
