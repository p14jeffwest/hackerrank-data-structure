# Exam variation axes: ds-08-palindrome

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-09-palindrome`, the same problem, so the axes must be
split.

## The core of the original problem

Compare the two outer characters and narrow inwards. The base case is a range
of zero or one character; the helper method exists because the public
signature cannot carry the range.

## Variation axes

- **Reverse instead**: return the reversed string recursively. This is the
  book's own exercise (8.4 Problem 5) and uses the same narrowing. Available
  to either section, but see the overlap note.
- **Loosen the rule**: ignore case; ignore anything that is not a letter or
  digit, so `A man, a plan, a canal: Panama` counts. The second is the good
  version -- the recursion now has to skip characters, and the base case has
  to survive skipping past the far end.
- **Ask for the recurrence**: what is $T(n)$ for this method, and what does it
  solve to? $T(n) = T(n-2) + 1$, so $O(n)$. Directly answers 8.4 Problem 3.
- **Ask about the base case**: why is `low >= high` right and `low == high`
  wrong? Which inputs does the second one break, and how? The answer -- every
  even-length string, by running past the ends -- is exactly what case 01
  tests.
- **Ask about the helper**: why can `isPalindrome(String)` not recurse on its
  own? Name two other ways to carry the state (substring, an index field) and
  say what each costs. Substring is the interesting one: it is $O(n)$ per
  call, which turns an $O(n)$ method into $O(n^2)$.
- **Trace by hand**: give a five-character string and list the calls with
  their arguments, in order.
- **Turn it into a count**: how many characters have to change to make the
  string a palindrome? Same traversal, a different accumulator.
- **Remove the recursion**: rewrite it as a loop, and say why this one is easy
  to convert when Hanoi is not. The answer is that it is tail recursion,
  which is 8.3's subject.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The problem itself | `dsa-09-palindrome` (Korean set) | Same problem by design. The reserved split below keeps the exams apart. |
| Reversing a string recursively | 8.4 Problem 5 | Not a contest problem here, so it is free as exam material -- but it is so close to this problem that using both on one exam tests one thing twice. |
| Tail recursion and converting to a loop | 8.3 | Chapter 8's own subject. `ds-08-hanoi` is the counterexample; pair them rather than asking twice. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Loosen the rule -- ignore case and punctuation |
| English (ds) | Why the helper is needed, and what `substring` would cost |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
