#!/usr/bin/env python3
"""Test case generator for ds-06-array-stack.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What the cases are built to catch
---------------------------------
  1. item[top++] instead of item[++top]. Post-increment stores at the old top,
     so the very first push writes to item[-1] and throws. Every case catches
     it, which is why case 00 opens with a push.

  2. Missing ensureCapacity(). The stack is created with the book's default
     capacity of 50, so nothing goes wrong until the 51st element is pushed.
     Cases 00 through 03 stay under that on purpose and cases 04 onward do
     not, so the mistake shows as a partial score rather than a zero.

  3. Missing top-- in pop. Repeated pops keep returning the same value, and
     size stops shrinking.

  4. Missing empty checks in pop and peek. Without them the array is read at
     index -1 and throws ArrayIndexOutOfBoundsException, which the driver
     still catches -- so an accidental "empty" comes out and the case passes.
     That is worth knowing: this particular mistake is NOT caught here, and
     it is recorded in UPLOAD.md rather than papered over.

Note what no test can see: leaving out item[top] = null in pop changes no
output at all. It is a garbage-collection concern, exactly as in
ds-04-array-list.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20260601)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

BIG = 1_000_000_000
QMAX = 200_000


def run(commands):
    """Reference model of the driver."""
    stack = []
    out = []
    for c in commands:
        parts = c.split()
        op = parts[0]
        if op == "push":
            stack.append(int(parts[1]))
        elif op == "pop":
            out.append(str(stack.pop()) if stack else "empty")
        elif op == "peek":
            out.append(str(stack[-1]) if stack else "empty")
        elif op == "size":
            out.append(str(len(stack)))
        elif op == "empty":
            out.append("1" if not stack else "0")
        elif op == "clear":
            stack.clear()
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


def depth_of(commands):
    """Largest number of elements held at once, for the notes below."""
    n = best = 0
    for c in commands:
        if c.startswith("push"):
            n += 1
            best = max(best, n)
        elif c.startswith("pop"):
            n = max(0, n - 1)
        elif c.startswith("clear"):
            n = 0
    return best


# ---------------------------------------------------------------- hand-built

# 00 sample: the worked example. Opens on an empty stack, so pop and peek
#            report `empty` before anything is pushed.
write(0, [
    "pop", "peek",
    "push 10", "push 20", "peek", "size",
    "pop", "pop", "empty", "pop",
    "push 5", "size",
])

# 01 sample: LIFO order, straight from 6.1. Push 1, 2, 3 and take them back.
write(1, [
    "push 1", "push 2", "push 3", "size",
    "pop", "pop", "pop", "empty", "size",
])

# 02 sample: the empty stack in every way it can be touched
write(2, [
    "empty", "size", "pop", "peek",
    "push 7", "empty", "size", "peek",
    "pop", "empty", "size", "pop", "peek",
])

# 03: clear, then keep using the stack. Stays under the default capacity.
write(3, ["push %d" % i for i in range(1, 31)] +
         ["size", "peek", "clear", "size", "empty", "pop", "peek"] +
         ["push %d" % i for i in range(100, 110)] + ["size", "peek"])

# 04: crosses the default capacity of 50 for the first time. A push without
#     ensureCapacity throws here and not before.
write(4, ["push %d" % i for i in range(1, 61)] + ["size", "peek"] +
         ["pop"] * 60 + ["size", "empty"])

# 05: exactly at the boundary -- 50 pushes are fine, the 51st expands
write(5, ["push %d" % i for i in range(1, 51)] + ["size", "peek"] +
         ["push 999", "size", "peek"] + ["pop", "pop", "size"])

# 06: repeated growth, 50 -> 100 -> 200 -> 400 -> 800
write(6, ["push %d" % random.randint(1, BIG) for _ in range(801)] +
         ["size", "peek"] + ["pop"] * 400 + ["size"])

# 07: alternating push and pop, so the stack never grows but the operations
#     never stop either
cmds = []
for i in range(2000):
    cmds.append("push %d" % random.randint(1, BIG))
    cmds.append("pop")
    if i % 100 == 0:
        cmds.append("size")
        cmds.append("empty")
write(7, cmds)

# ------------------------------------------------------------------ random


def random_case(q, empty_heavy=False):
    cmds = []
    depth = 0
    while len(cmds) < q:
        r = random.random()
        if depth == 0 and not empty_heavy:
            cmds.append("push %d" % random.randint(1, BIG))
            depth += 1
        elif r < 0.42:
            cmds.append("push %d" % random.randint(1, BIG))
            depth += 1
        elif r < 0.70:
            cmds.append("pop")
            depth = max(0, depth - 1)
        elif r < 0.85:
            cmds.append("peek")
        elif r < 0.92:
            cmds.append("size")
        elif r < 0.98:
            cmds.append("empty")
        else:
            cmds.append("clear")
            depth = 0
    return cmds[:q]


# 08: moderate size, mixed
write(8, random_case(5000))

# 09: moderate size with the stack often empty, so pop and peek report
#     `empty` constantly
write(9, random_case(5000, empty_heavy=True))

# 10: maximum Q, mixed
write(10, random_case(QMAX))

# 11: maximum Q, push-heavy, so the array doubles all the way up
cmds = ["push %d" % random.randint(1, BIG) for _ in range(QMAX - 2000)]
cmds += ["size", "peek"]
cmds += ["pop"] * 1998
write(11, cmds)

# 12: maximum Q, empty-heavy
write(12, random_case(QMAX, empty_heavy=True))

# 13: maximum Q with clear used often, so the array is large but the reported
#     size keeps returning to zero
cmds = []
while len(cmds) < QMAX:
    for _ in range(random.randint(50, 400)):
        cmds.append("push %d" % random.randint(1, BIG))
    cmds.append("size")
    cmds.append("peek")
    cmds.append("clear")
    cmds.append("size")
    cmds.append("pop")
write(13, cmds[:QMAX])

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        q = int(f.readline())
        cmds = [f.readline().rstrip("\n") for _ in range(q)]
    print("  case %02d: Q = %-7s max depth %7d" % (i, q, depth_of(cmds)))
