#!/usr/bin/env python3
"""Test case generator for ds-08-palindrome.

The seed is fixed, so rerunning this produces identical files.

    python3 gen.py

What the cases are built to catch
---------------------------------
  1. Comparing case-insensitively. `Level` is NOT a palindrome here, because
     upper and lower case are different characters. Case 02 is published as a
     sample for exactly this.

  2. Getting the base case wrong. A range of one character (odd length) and a
     range of zero characters (even length) both have nothing left to compare.
     Stopping at only one of the two breaks half the inputs, so cases 01 and
     03 separate odd and even lengths deliberately.

  3. Off-by-one when narrowing: recursing on (low + 1, high) instead of
     (low + 1, high - 1) is a classic slip and gives wrong answers on almost
     everything.

  4. Recursion depth. A 1,000-character palindrome recurses 500 deep, which is
     fine, but the near-palindromes in case 07 are the ones that go deepest
     before failing.

What no test can check: whether the method is recursive at all. A student can
write `s.equals(new StringBuilder(s).reverse().toString())` and score full
marks. The Korean counterpart accepts the same limitation.

Every file is ASCII with LF line endings.
"""
import random
import os
import string

random.seed(20260801)

IN, OUT = "testcases/input", "testcases/output"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

ALPHABET = string.ascii_letters + string.digits     # letters and digits, no spaces
LMAX = 1_000
TMAX = 1_000


def write(idx, words):
    assert 1 <= len(words) <= TMAX, "T out of range in case %d" % idx
    for w in words:
        assert 1 <= len(w) <= LMAX, "length out of range in case %d" % idx
        assert all(c in ALPHABET for c in w), "bad character in case %d" % idx
    with open("%s/input%02d.txt" % (IN, idx), "w", newline="\n") as f:
        f.write("%d\n" % len(words))
        f.write("\n".join(words) + "\n")
    with open("%s/output%02d.txt" % (OUT, idx), "w", newline="\n") as f:
        for w in words:
            f.write("%s\n" % ("true" if w == w[::-1] else "false"))


def palindrome(length, alphabet=ALPHABET):
    half = [random.choice(alphabet) for _ in range(length // 2)]
    middle = [random.choice(alphabet)] if length % 2 else []
    return "".join(half + middle + half[::-1])


def near_palindrome(length, alphabet=ALPHABET):
    """A palindrome with exactly one character changed, so it fails late."""
    s = list(palindrome(length, alphabet))
    i = random.randrange(length)
    original = s[i]
    while s[i] == original:
        s[i] = random.choice(alphabet)
    return "".join(s)


# ---------------------------------------------------------------- hand-built

# 00 sample: the worked examples from the statement
write(0, ["aba", "abba", "a", "Level", "aa", "ab"])

# 01 sample: odd and even lengths side by side, which is where a base case
#            that handles only one of the two comes apart
write(1, [
    "a", "aa", "aba", "abba", "abcba", "abccba",
    "ab", "abc", "abca", "abcda",
])

# 02 sample: case sensitivity. `Level`, `Aba` and `AA` are all rejected, while
#            their single-case versions are accepted.
write(2, ["Level", "level", "Aba", "aba", "AA", "aa", "Zz", "zz", "aBa"])

# 03: single characters of every kind, all palindromes
write(3, list("aAzZ09"))

# 04: two characters, half of them palindromes
write(4, ["aa", "ab", "AA", "Aa", "aA", "11", "12", "a1", "99"])

# 05: digits, and mixtures of digits and letters
write(5, ["12321", "123321", "12345", "a1b1a", "a1b2a", "0", "00", "01",
          "1a1", "1a2"])

# 06: long palindromes at the maximum length, both parities
write(6, [palindrome(LMAX), palindrome(LMAX - 1),
          palindrome(LMAX, "ab"), palindrome(LMAX - 1, "ab")])

# 07: near-palindromes at the maximum length. These are the deepest failures:
#     the comparison runs a long way in before the mismatch appears.
write(7, [near_palindrome(LMAX) for _ in range(50)])

# 08: strings of one repeated character, all palindromes, at full length
write(8, ["a" * LMAX, "Z" * (LMAX - 1), "7" * LMAX, "q" * 999])

# 09: a palindrome broken at the very first character, and one broken at the
#     very middle -- the earliest and latest possible mismatches
cases = []
for length in [LMAX, LMAX - 1, 501, 500]:
    p = list(palindrome(length, "abc"))
    first = p[:]
    first[0] = "z" if first[0] != "z" else "y"
    middle = p[:]
    m = length // 2
    middle[m] = "z" if middle[m] != "z" else "y"
    cases += ["".join(p), "".join(first), "".join(middle)]
write(9, cases)

# ------------------------------------------------------------------ maximum

# 10: T at its maximum, short random strings, mostly not palindromes
write(10, ["".join(random.choice(ALPHABET) for _ in range(random.randint(1, 12)))
           for _ in range(TMAX)])

# 11: T at its maximum, half palindromes and half near-palindromes
words = []
for _ in range(TMAX // 2):
    n = random.randint(1, 400)
    words.append(palindrome(n))
    words.append(near_palindrome(n) if n > 1 else "a")
write(11, words)

# 12: T at its maximum, every string at or near the maximum length
words = []
for i in range(TMAX):
    n = random.randint(LMAX - 3, LMAX)
    words.append(palindrome(n, "ab") if i % 2 == 0 else near_palindrome(n, "ab"))
write(12, words)

# 13: T at its maximum, mixed case throughout, so a case-insensitive
#     comparison is wrong on most of them
words = []
for _ in range(TMAX):
    n = random.randint(2, 300)
    base = palindrome(n, string.ascii_lowercase)
    i = random.randrange(n)
    words.append(base[:i] + base[i].upper() + base[i + 1:])
write(13, words)

print("generated 14 cases")
for i in range(14):
    path = "%s/input%02d.txt" % (IN, i)
    with open(path) as f:
        t = int(f.readline())
        words = [f.readline().rstrip("\n") for _ in range(t)]
    trues = sum(1 for w in words if w == w[::-1])
    print("  case %02d: T = %-6s longest %5d  true %5d / %5d"
          % (i, t, max(len(w) for w in words), trues, t))
