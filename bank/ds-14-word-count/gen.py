#!/usr/bin/env python3
"""Test case generator for ds-14-word-count.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What the cases are built to catch
---------------------------------
  1. Scanning the whole list for every query. That is O(N*Q), which at
     200,000 of each is 4 * 10^10 and does not finish. Cases 10 through 13
     are large enough; the small ones are not, so the mistake shows as a
     partial score.

  2. get() instead of getOrDefault(), which returns null for a word that never
     appeared and throws when it is unboxed. Case 02 is published as a sample
     and is entirely made of words that are not in the list.

  3. Counting distinct occurrences rather than all of them -- a HashSet where a
     HashMap was needed. Case 03 is built from heavy repetition.

The words are drawn from a pool so that queries hit and miss in known
proportions; roughly half the queries in the large cases are words that never
appeared.

Every file is ASCII with LF line endings.
"""
import random
import os
import string

random.seed(20261401)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

NMAX = 200_000
QMAX = 200_000
WORD_MAX = 10


def write(idx, words, queries):
    assert 1 <= len(words) <= NMAX, "N out of range in case %d" % idx
    assert 1 <= len(queries) <= QMAX, "Q out of range in case %d" % idx
    for w in words + queries:
        assert 1 <= len(w) <= WORD_MAX, "word length out of range in case %d" % idx
        assert all(c in string.ascii_lowercase for c in w), \
            "bad character in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n%s\n" % (len(words), " ".join(words)))
        f.write("%d\n%s\n" % (len(queries), " ".join(queries)))
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for q in queries:
            f.write("%d\n" % counts.get(q, 0))


def word(i):
    """A distinct lower-case word of at most ten letters."""
    s = ""
    i += 1
    while i:
        i, r = divmod(i - 1, 26)
        s = string.ascii_lowercase[r] + s
    return s


# ---------------------------------------------------------------- hand-built

# 00 sample: the worked example
write(0, ["apple", "banana", "apple", "cherry", "banana", "apple"],
       ["apple", "banana", "cherry", "durian"])

# 01 sample: one word in the list, asked for and not asked for
write(1, ["kiwi"], ["kiwi", "mango"])

# 02 sample: every query is a word that never appeared, so every answer is 0.
#            02 must be published: get() returns null here and throws when it
#            is unboxed, while getOrDefault() gives the 0 that is wanted.
write(2, ["alpha", "beta"], ["gamma", "delta", "epsilon", "zeta"])

# 03: one word repeated many times, so counting distinct words instead of
#     occurrences answers 1 where the answer is 20
write(3, ["repeat"] * 20 + ["other"], ["repeat", "other", "missing"])

# 04: the same word queried several times over
write(4, ["a", "b", "a", "a"], ["a", "a", "b", "b", "c", "a"])

# 05: words at both length limits
write(5, ["a", "abcdefghij", "a", "abcdefghij", "abcdefghij"],
       ["a", "abcdefghij", "abcdefghi"])

# 06: words that are prefixes of one another, which a careless key would
#     confuse
write(6, ["ab", "abc", "abcd", "ab", "abc", "ab"],
       ["ab", "abc", "abcd", "abcde", "a"])

# 07: many distinct words, each appearing once
write(7, [word(i) for i in range(500)],
       [word(i) for i in range(0, 500, 7)] + ["zzzz"])

# ------------------------------------------------------------------ maximum

# 08: the full list drawn from a small pool, so every word appears often
pool = [word(i) for i in range(50)]
write(8, [random.choice(pool) for _ in range(NMAX)],
       [random.choice(pool) for _ in range(QMAX)])

# 09: the full list of DISTINCT words, so every count is 1 and the map is at
#     its largest
words = [word(i) for i in range(NMAX)]
write(9, words, [random.choice(words) for _ in range(QMAX)])

# 10: the full list and the full query count, half the queries missing
pool = [word(i) for i in range(20_000)]
absent = [word(i) for i in range(20_000, 40_000)]
write(10, [random.choice(pool) for _ in range(NMAX)],
      [random.choice(pool if i % 2 == 0 else absent) for i in range(QMAX)])

# 11: the full list, every word the same, and every query that same word --
#     the worst case for a per-query scan, since it never exits early
write(11, ["same"] * NMAX, ["same"] * QMAX)

# 12: the full list, every query a word that never appeared. A per-query scan
#     has to walk the whole list every time.
write(12, [word(i % 1000) for i in range(NMAX)], ["nothing"] * QMAX)

# 13: the full list, words of the maximum length so the input is largest
long_pool = [word(i).rjust(WORD_MAX, "z") for i in range(5_000)]
write(13, [random.choice(long_pool) for _ in range(NMAX)],
      [random.choice(long_pool) for _ in range(QMAX)])

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open(ipath) as f:
        n = int(f.readline())
        f.readline()
        q = int(f.readline())
    print("  case %02d: N = %-7d Q = %-7d  in %8d B"
          % (i, n, q, os.path.getsize(ipath)))
