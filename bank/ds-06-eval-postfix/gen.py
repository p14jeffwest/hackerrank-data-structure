#!/usr/bin/env python3
"""Test case generator for ds-06-eval-postfix.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

Design notes
------------
The book states this over a handful of short expressions. Raised here to a sum
of 300,000 tokens, which makes the reading and the output size matter and
rules out anything quadratic.

What the cases are built to catch:

  1. Popping the operands in the wrong order. The book's own TIP at the end of
     6.2 item 2 warns about it: the FIRST value popped is the RIGHT operand.
     Reversing it is invisible for + and * and wrong every time for - and /.
     Case 05 contains only + and *, so a reversed solution passes it, which
     turns the mistake into a partial score.

  2. Mistaking a negative literal for the operator. `-11` is a number; `-` is
     an operator. A test that looks only at the first character misreads every
     negative operand. Case 02 is published as a sample for this.

  3. Java's integer division, which truncates toward ZERO rather than
     flooring: -7 / 2 is -3, not -4. Case 04 is nothing but that.

The reference model below implements Java's truncation deliberately. Python's
// floors, and using it would have produced expected output that agrees with a
Java solution only when the signs happen to match.

Every generated expression is valid: operators never run short of operands,
exactly one value is left at the end, no division by zero occurs, and every
intermediate result stays within 10^9 in absolute value.

Every file is ASCII with LF line endings.
"""
import random
import os

random.seed(20260602)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

BOUND = 1_000_000_000          # the hard limit the problem promises
KEEP = 500_000_000             # what combine aims for, so that a fallback of
                               # a + b or a - b can never break BOUND
OPERAND_LO, OPERAND_HI = -1000, 1000
TOKENS_MAX = 300_000


def idiv(a, b):
    """Integer division the way Java does it: truncate toward zero."""
    q = abs(a) // abs(b)
    return q if (a < 0) == (b < 0) else -q


def apply(op, a, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    return idiv(a, b)


def evaluate(tokens):
    """Reference model: the same algorithm the solution uses."""
    stack = []
    for token in tokens:
        if len(token) == 1 and token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            stack.append(apply(token, a, b))
        else:
            stack.append(int(token))
    assert len(stack) == 1, "expression does not reduce to one value"
    return stack[0]


def build(leaves, ops="+-*/"):
    """A valid postfix expression with the given number of operands.

    Built iteratively rather than recursively, because a recursive tree walk
    would blow Python's stack at 150,000 leaves. Values are combined only when
    the result stays inside the bound, so no case can drift out of range.
    """
    tokens = []
    values = []

    def combine():
        b = values.pop()
        a = values.pop()
        candidates = [(op, apply(op, a, b)) for op in ops
                      if not (op == "/" and b == 0)]
        safe = [(op, r) for op, r in candidates if abs(r) <= KEEP]
        if safe:
            op, r = random.choice(safe)
        else:
            # The fallback must stay inside `ops`; an earlier version fell back
            # to "-" unconditionally, which quietly injected subtraction into
            # the cases built from "+*" only and cost them their whole purpose.
            # Every stack value is at most KEEP, so the smallest-magnitude
            # candidate is at most 2 * KEEP and cannot exceed BOUND.
            op, r = min(candidates, key=lambda c: abs(c[1]))
        assert abs(r) <= BOUND
        tokens.append(op)
        values.append(r)

    for i in range(leaves):
        v = random.randint(OPERAND_LO, OPERAND_HI)
        tokens.append(str(v))
        values.append(v)
        while len(values) >= 2 and random.random() < 0.5:
            combine()
    while len(values) > 1:
        combine()

    assert len(tokens) == 2 * leaves - 1
    return tokens


def build_chain(leaves, ops):
    """A left-nested expression: ((((a op b) op c) op d) ...).

    Used for the cases that restrict the operator set. `build` cannot be
    trusted there: with only "+*" available, both candidates can exceed the
    limit at once and its fallback then pushes a value above KEEP, which the
    next combine turns into an overflow. Here one operand of every step is a
    fresh literal of at most 1000, so a leaf of the opposite sign always
    brings the running value back down and a safe operator always exists.

    The stack never holds more than two values, so these cases test the
    operator handling rather than the stack depth. Depth is covered by cases
    09, 10 and 13.
    """
    acc = random.randint(1, 50)
    tokens = [str(acc)]
    for _ in range(leaves - 1):
        good = []
        for _attempt in range(30):
            leaf = random.randint(OPERAND_LO, OPERAND_HI)
            if abs(acc) > KEEP // 2:          # steer back toward zero
                leaf = -abs(leaf) if acc > 0 else abs(leaf)
            candidates = [(op, apply(op, acc, leaf)) for op in ops
                          if not (op == "/" and leaf == 0)]
            good = [(op, r) for op, r in candidates if abs(r) <= KEEP]
            if good:
                break
        assert good, "no safe operator for acc=%d" % acc
        op, r = random.choice(good)
        tokens += [str(leaf), op]
        acc = r
    assert len(tokens) == 2 * leaves - 1
    return tokens


def write(idx, expressions):
    total = sum(len(e) for e in expressions)
    assert 1 <= len(expressions) <= 2000, "T out of range in case %d" % idx
    assert total <= TOKENS_MAX, \
        "token total %d exceeds the limit in case %d" % (total, idx)
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(expressions))
        for e in expressions:
            f.write(" ".join(e) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for e in expressions:
            f.write("%d\n" % evaluate(e))


def s(text):
    return text.split()


# ---------------------------------------------------------------- hand-built

# 00 sample: the worked examples from the book
write(0, [s("2 1 + 3 *"), s("4 13 5 / +"),
          s("10 6 9 3 + -11 * / * 17 + 5 +"), s("3 4 + 5 *")])

# 01 sample: subtraction and division, where the pop order shows.
#            Each pair is the same two numbers in the other order.
write(1, [s("5 3 -"), s("3 5 -"), s("13 5 /"), s("5 13 /"),
          s("100 7 -"), s("7 100 -")])

# 02 sample: negative literals standing next to the minus operator.
#            A solution that decides on the first character alone reads
#            "-11" as an operator and falls apart here.
write(2, [s("-11 3 -"), s("3 -11 -"), s("-11 -3 *"), s("-11 -3 /"),
          s("-1 -1 +"), s("-1000 1000 +")])

# 03: a single operand and nothing to do
write(3, [s("7"), s("-7"), s("0"), s("1000"), s("-1000")])

# 04: division truncating toward zero, which is where Java and a floor-based
#     model disagree
write(4, [s("-7 2 /"), s("7 -2 /"), s("-7 -2 /"), s("7 2 /"),
          s("-1 2 /"), s("1 -2 /"), s("-999 1000 /")])

# 05: nothing but + and *, so a solution that pops its operands the wrong way
#     round still passes this case
write(5, [build_chain(random.randint(2, 40), ops="+*") for _ in range(200)])

# 06: deeply left-nested, then deeply right-nested. The first keeps the stack
#     at two values; the second grows it to the full length.
left = []
for _ in range(60):
    k = random.randint(2, 30)
    toks = [str(random.randint(1, 50))]
    for _ in range(k - 1):
        toks += [str(random.randint(1, 50)), random.choice("+-")]
    left.append(toks)
right = []
for _ in range(60):
    k = random.randint(2, 30)
    toks = [str(random.randint(1, 50)) for _ in range(k)]
    toks += list(random.choice("+-") for _ in range(k - 1))
    right.append(toks)
write(6, left + right)

# 07: zero as an operand, but never as a divisor
write(7, [s("0 5 +"), s("5 0 +"), s("0 5 *"), s("0 5 -"), s("5 0 -"),
          s("0 5 /"), s("0 0 +"), s("0 0 *")])

# 08: many small random expressions over all four operators
write(8, [build(random.randint(1, 20)) for _ in range(1500)])

# ------------------------------------------------------------------ maximum

# 09: one very long expression
write(9, [build(TOKENS_MAX // 2)])

# 10: T at its maximum with a large total
exprs = []
remaining = TOKENS_MAX
for i in range(2000):
    room = remaining - (2000 - i - 1)
    leaves = max(1, min((room + 1) // 2, random.randint(1, 90)))
    e = build(leaves)
    remaining -= len(e)
    exprs.append(e)
write(10, exprs)

# 11: a long expression of + and * only, at full size
write(11, [build_chain(TOKENS_MAX // 2, ops="+*")])

# 12: a long expression of - and / only, at full size, which is the worst case
#     for the pop order
write(12, [build_chain(TOKENS_MAX // 2, ops="-/")])

# 13: two long right-nested expressions, so the stack fills to nearly the full
#     token count before anything is reduced
half = TOKENS_MAX // 4
exprs = []
for _ in range(2):
    toks = [str(random.randint(-1000, 1000)) for _ in range(half)]
    toks += ["-"] * (half - 1)
    exprs.append(toks)
write(13, exprs)

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        t = int(f.readline())
        total = sum(len(f.readline().split()) for _ in range(t))
    print("  case %02d: T = %-6s tokens %7d" % (i, t, total))
