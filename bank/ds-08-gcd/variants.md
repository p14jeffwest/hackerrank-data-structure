# Exam variation axes: ds-08-gcd

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-09-gcd`, the same problem, so the axes must be split.

## The core of the original problem

`gcd(a, b) = gcd(b, a mod b)` with `gcd(a, 0) = a`. One recursive call, an
argument that shrinks fast, and a base case at zero.

## Variation axes

- **Least common multiple**: `lcm(a, b) = a / gcd(a, b) * b`. The division
  must come first or the product overflows -- a small trap worth setting once.
- **Extend it**: find `x` and `y` with `ax + by = gcd(a, b)`. The extended
  Euclidean algorithm is the same recursion carrying two more values back up,
  and it is a genuine step up in difficulty.
- **More than two numbers**: the gcd of an array, by folding. Then ask why
  folding works, which is a question about associativity rather than about
  recursion.
- **Ask about the base case**: why `b == 0` and not `b == 1`? Which inputs
  does the second one get right? (Exactly the coprime pairs, because their
  last non-zero remainder is 1.)
- **Ask about the argument order**: what happens with `gcd(a % b, b)` instead
  of `gcd(b, a % b)`? Infinite recursion, because the pair never changes after
  the first step.
- **Ask about subtraction**: `gcd(a - b, b)` is correct and unusable. Give
  `a = 1`, `b = 10^9` and ask how many calls it makes. This is the sharpest
  question this problem supports -- it separates "correct" from "affordable"
  in one line of arithmetic.
- **Ask for the depth**: how deep can the recursion go for values up to
  $10^9$? The worst case is consecutive Fibonacci numbers, and the answer is
  about 44. Deriving even a rough bound is a good exercise.
- **Convert it to a loop**: this is tail recursion, so the conversion is
  mechanical. Pair with `ds-08-hanoi`, which cannot be converted that way.
- **Trace by hand**: `gcd(48, 36)` or `gcd(5, 17)`, listing the arguments at
  each call. The second is the interesting one, because the first step just
  swaps them.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The problem itself | `dsa-09-gcd` (Korean set) | Same problem by design. The reserved split below keeps the exams apart. |
| Tail recursion, converting to a loop | `ds-08-palindrome`, `ds-08-hanoi` | Three problems touch this. Chapter 8 owns it; ask it once, ideally as the palindrome-versus-Hanoi contrast. |
| Correct but unaffordable | `ds-06-queue-two-stacks`, `ds-08-climb-stairs` | The subtraction version is the cheapest instance of this idea in the whole set. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Least common multiple, and where the overflow is |
| English (ds) | Subtraction instead of remainder -- correct, and how many calls |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
