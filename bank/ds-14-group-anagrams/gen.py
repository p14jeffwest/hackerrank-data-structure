#!/usr/bin/env python3
"""Test case generator for ds-14-group-anagrams.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

The order had to be fixed
-------------------------
The book says the order of the groups and of the words within them is free,
which cannot be graded. This version requires:

  * within a group, the input order;
  * groups in the order their first word appeared.

That is not an arbitrary choice. It is what a LinkedHashMap gives, and
requiring it makes the chapter's own point testable: a plain HashMap has NO
order, so `new ArrayList<>(map.values())` returns the groups in an order that
depends on the hashing rather than on the input.

What the cases are built to catch
---------------------------------
  1. Returning a plain HashMap's values, so the group order is arbitrary.
     Case 02 is published as a sample and is arranged so the two orders
     differ.

  2. A key that loses information -- the sum of the character codes is the
     usual one. "ad" and "bc" both sum to 197 and are not anagrams. Case 03 is
     built from such pairs.

  3. Using the word itself as the key, so every distinct word is its own
     group. Case 00 catches it.

  4. Sorting the words within a group, or sorting the groups, which the order
     rule forbids. Case 04 has groups whose input order is not alphabetical.

Every file is ASCII with LF line endings.
"""
import random
import os
import string

random.seed(20261403)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

NMAX = 100_000
WORD_MAX = 20


def solve(strs):
    """Insertion-ordered grouping -- Python dicts preserve insertion order."""
    groups = {}
    for s in strs:
        key = "".join(sorted(s))
        groups.setdefault(key, []).append(s)
    return list(groups.values())


def write(idx, strs):
    n = len(strs)
    assert 1 <= n <= NMAX, "n out of range in case %d" % idx
    for s in strs:
        assert 1 <= len(s) <= WORD_MAX, "word length out of range in case %d" % idx
        assert all(c in string.ascii_lowercase for c in s), \
            "bad character in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % n)
        f.write(" ".join(strs) + "\n")
    groups = solve(strs)
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(groups))
        for g in groups:
            f.write(" ".join(g) + "\n")


def scramble(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)


# ---------------------------------------------------------------- hand-built

# 00 sample: the book's example
write(0, ["eat", "tea", "tan", "ate", "nat", "bat"])

# 01 sample: a single word, and words that share no letters at all
write(1, ["solo"])
write(2, ["abc", "def", "cba", "fed", "ghi"])

# 03 sample: the group order. `zzz` appears first and must come first, even
#            though its key sorts last. 03 must be published: returning a
#            plain HashMap's values puts the groups in hash order instead.
write(3, ["zzz", "abc", "cba", "yyy", "zzz", "bac"])

# 04: character-code collisions. "ad" and "bc" both sum to 197, and "ae" and
#     "bd" both sum to 199 -- neither pair is an anagram.
write(4, ["ad", "bc", "da", "cb", "ae", "bd", "ea", "db"])

# 05: groups whose words are not in alphabetical order, so sorting within a
#     group is visibly wrong
write(5, ["zebra", "barze", "arzeb", "apple", "pplea"])

# 06: every word an anagram of every other, so there is exactly one group
write(6, ["abc", "acb", "bac", "bca", "cab", "cba"])

# 07: no two words are anagrams, so every word is its own group
write(7, [word for word in ["a", "ab", "abc", "abcd", "abcde"]])

# 08: repeated identical words, which are anagrams of one another
write(8, ["dog", "god", "dog", "odg", "cat", "dog"])

# 09: words at both length limits
write(9, ["a", "z", "a", "abcdefghijklmnopqrst", "tsrqponmlkjihgfedcba"])

# 10: single letters only, so there are 26 groups at most
write(10, [random.choice(string.ascii_lowercase) for _ in range(200)])

# ------------------------------------------------------------------ maximum

# 11: the full count from a pool of base words, each scrambled -- large groups
bases = ["".join(random.choice(string.ascii_lowercase) for _ in range(8))
         for _ in range(200)]
write(11, [scramble(random.choice(bases)) for _ in range(NMAX)])

# 12: the full count of words that are all distinct in their letters, so
#     almost every word is its own group and the map is at its largest
words = []
seen = set()
while len(words) < NMAX:
    w = "".join(random.choice(string.ascii_lowercase) for _ in range(12))
    key = "".join(sorted(w))
    if key not in seen:
        seen.add(key)
        words.append(w)
write(12, words)

# 13: the full count at the maximum word length, from a small pool, so the
#     sorting of each word is at its most expensive
bases = ["".join(random.choice(string.ascii_lowercase) for _ in range(WORD_MAX))
         for _ in range(50)]
write(13, [scramble(random.choice(bases)) for _ in range(NMAX)])

print("generated 14 cases")
for i in range(14):
    ipath = "%s/input%02d.txt" % (IN, i)
    with open(ipath) as f:
        n = int(f.readline())
    with open("%s/output%02d.txt" % (OUT, i)) as f:
        g = int(f.readline())
    print("  case %02d: n = %-7d groups %-7d  in %8d B"
          % (i, n, g, os.path.getsize(ipath)))
