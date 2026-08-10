#!/usr/bin/env python3
"""Test case generator for ds-07-circular-queue.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What the cases are built to catch
---------------------------------
  1. A missing modulo. Everything works until the queue wraps for the first
     time, and then the index runs off the array. Cases 00 through 03 use
     capacities large enough that no wrap ever happens, so the mistake shows
     as a partial score and points straight at the wrap.

  2. Advancing front without the modulo, which is the same failure one step
     later -- the write wraps but the read does not.

  3. Missing count++ / count--, which shows in size, empty and full long
     before it shows in the values.

  4. Missing the isFull check, so enqueue overwrites the front element
     instead of reporting a full queue. This one is quiet: the queue keeps
     answering, with the wrong contents.

  5. Missing the isEmpty checks, which the driver reports as `crash` rather
     than `empty` when the array is read out of range.

Note the boundary handling is the book's, and it is deliberately asymmetric:
enqueue on a full queue THROWS, while dequeue and getFront on an empty queue
return null. Section 6.1 presents both policies; 7.3 uses one of each.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20260701)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

BIG = 1_000_000_000
QMAX = 200_000
CMAX = 100_000


def run(capacity, commands):
    """Reference model of the driver."""
    data = [None] * capacity
    front = 0
    count = 0
    out = []
    for c in commands:
        parts = c.split()
        op = parts[0]
        if op == "enqueue":
            if count == capacity:
                out.append("full")
            else:
                data[(front + count) % capacity] = int(parts[1])
                count += 1
        elif op == "dequeue":
            if count == 0:
                out.append("empty")
            else:
                out.append(str(data[front]))
                data[front] = None
                front = (front + 1) % capacity
                count -= 1
        elif op == "front":
            out.append("empty" if count == 0 else str(data[front]))
        elif op == "size":
            out.append(str(count))
        elif op == "empty":
            out.append("1" if count == 0 else "0")
        elif op == "full":
            out.append("1" if count == capacity else "0")
        elif op == "clear":
            for i in range(count):
                data[(front + i) % capacity] = None
            front = 0
            count = 0
        else:
            raise ValueError("unknown command: " + c)
    return out


def write(idx, capacity, commands):
    assert 1 <= capacity <= CMAX, "capacity out of range in case %d" % idx
    assert 1 <= len(commands) <= QMAX, "Q out of range in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d %d\n" % (capacity, len(commands)))
        f.write("\n".join(commands) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("".join(line + "\n" for line in run(capacity, commands)))


def wraps(capacity, commands):
    """How many enqueues would run off the array without the modulo.

    That is exactly the count of writes where front + count reaches capacity,
    which is the moment a missing % capacity throws.
    """
    front = count = 0
    n = 0
    for c in commands:
        if c.startswith("enqueue"):
            if count < capacity:
                if front + count >= capacity:
                    n += 1
                count += 1
        elif c.startswith("dequeue"):
            if count > 0:
                front = (front + 1) % capacity
                count -= 1
        elif c.startswith("clear"):
            front = count = 0
    return n


# ---------------------------------------------------------------- hand-built

# 00 sample: the worked example, and the capacity is large enough that the
#            array never wraps
write(0, 8, ["enqueue 10", "enqueue 20", "dequeue", "enqueue 30",
             "enqueue 40", "dequeue", "dequeue", "front", "size", "empty"])

# 01 sample: an empty queue touched in every way, still without wrapping
write(1, 5, ["empty", "full", "size", "dequeue", "front",
             "enqueue 7", "empty", "size", "front", "dequeue",
             "empty", "dequeue", "front"])

# 02 sample: the queue wraps. Capacity 4, and after two dequeues the writes
#            come back round to index 0. This is the case a missing modulo
#            cannot survive.
write(2, 4, ["enqueue 1", "enqueue 2", "dequeue", "dequeue",
             "enqueue 3", "enqueue 4", "enqueue 5", "enqueue 6",
             "full", "size", "front",
             "dequeue", "dequeue", "dequeue", "dequeue", "empty"])

# 03: a full queue rejecting more, without wrapping
write(3, 3, ["enqueue 1", "enqueue 2", "enqueue 3", "full",
             "enqueue 4", "enqueue 5", "size", "front",
             "dequeue", "full", "size"])

# 04: capacity 1, the smallest ring there is
write(4, 1,
      ["empty", "enqueue 1", "full", "enqueue 2", "front", "dequeue",
       "empty", "enqueue 3", "front", "dequeue", "dequeue"])

# 05: run around the ring several times with capacity 2
cmds = []
for i in range(1, 40):
    cmds += ["enqueue %d" % i, "enqueue %d" % (i * 100), "front",
             "dequeue", "dequeue", "empty"]
write(5, 2, cmds)

# 06: clear in the middle, which resets front to 0 while the ring was
#     part-way round
write(6, 5, ["enqueue 1", "enqueue 2", "enqueue 3", "dequeue", "dequeue",
             "enqueue 4", "enqueue 5", "enqueue 6", "size", "front",
             "clear", "size", "empty", "front",
             "enqueue 7", "front", "size", "dequeue"])

# 07: a queue kept exactly full, so every enqueue is rejected and every
#     dequeue immediately makes room again
cmds = ["enqueue %d" % i for i in range(1, 11)]
for i in range(200):
    cmds += ["enqueue %d" % (1000 + i), "full", "dequeue",
             "enqueue %d" % (2000 + i), "full"]
write(7, 10, cmds)

# ------------------------------------------------------------------ random


def random_case(capacity, q):
    cmds = []
    count = 0
    while len(cmds) < q:
        r = random.random()
        if r < 0.45:
            cmds.append("enqueue %d" % random.randint(1, BIG))
            count = min(capacity, count + 1)
        elif r < 0.75:
            cmds.append("dequeue")
            count = max(0, count - 1)
        elif r < 0.85:
            cmds.append("front")
        elif r < 0.91:
            cmds.append("size")
        elif r < 0.96:
            cmds.append("empty")
        elif r < 0.995:
            cmds.append("full")
        else:
            cmds.append("clear")
            count = 0
    return cmds[:q]


# 08: a small ring with heavy traffic, so it wraps constantly
write(8, 8, random_case(8, 5000))

# 09: a medium ring
write(9, 500, random_case(500, 5000))

# 10: maximum Q on a small ring
write(10, 16, random_case(16, QMAX))

# 11: maximum Q on a ring big enough that it never fills
write(11, CMAX, random_case(CMAX, QMAX))

# 12: maximum Q, filling most of a large ring and then cycling through it
cmds = ["enqueue %d" % random.randint(1, BIG) for _ in range(90000)]
while len(cmds) < QMAX:
    cmds.append("dequeue")
    cmds.append("enqueue %d" % random.randint(1, BIG))
write(12, CMAX, cmds[:QMAX])

# 13: maximum Q against a ring of capacity 2, so the wrap happens on almost
#     every operation
write(13, 2, random_case(2, QMAX))

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        cap, q = map(int, f.readline().split())
        cmds = [f.readline().rstrip("\n") for _ in range(q)]
    print("  case %02d: capacity %6d  Q = %-7s wraps %7d"
          % (i, cap, q, wraps(cap, cmds)))
