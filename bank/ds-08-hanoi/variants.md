# Exam variation axes: ds-08-hanoi

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-09-hanoi`, the same problem, so the axes must be
split.

## The core of the original problem

Move `n-1` disks out of the way, move the largest, bring the `n-1` back. The
recursion is three lines; the difficulty is the rotation of the peg roles
between the two recursive calls.

## Variation axes

- **Ask for the count only**: $2^n - 1$, with the recurrence
  $M(n) = 2M(n-1) + 1$ and its solution. Answers 8.4 Problem 3(c) directly.
- **Ask for one move**: which disk moves at step $k$, or where the largest
  disk is after $k$ moves. Both are answerable without generating the sequence
  and separate students who understand the structure from those who can only
  run it.
- **Change the goal peg**: move the disks to B instead of C, and ask what
  changes in the code. Almost nothing -- which is the point.
- **Add a rule**: disks may only move between adjacent pegs (A-B and B-C, not
  A-C). The recurrence becomes $M(n) = 3M(n-1) + 2$, so $3^n - 1$ moves. A
  genuinely different derivation from the same picture.
- **Four pegs**: the Frame-Stewart problem. Too hard to solve, but "why does
  adding a peg make the recurrence hard to write?" is a fair discussion
  question.
- **Trace by hand**: list the moves for `n = 3`, or give the first four moves
  of `n = 4` and ask for the next two.
- **Ask why it cannot be a loop**: 8.3 converts tail recursion to iteration.
  Hanoi has two recursive calls and is not tail recursive, so an explicit
  stack is needed. **Pair this with `ds-08-palindrome`**, which is tail
  recursive and converts in one step -- the contrast is the lesson.
- **Count the stack depth**: the recursion goes $n$ frames deep, not $2^n$.
  Students routinely confuse the number of calls with the depth, and this is
  the cleanest place to correct it.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The problem itself | `dsa-09-hanoi` (Korean set) | Same problem by design. The reserved split below keeps the exams apart. |
| Gathering output rather than printing | `ds-tutorial-03-sum` | The tutorial owns that lesson. Here it is a timing concern that the test data does not actually enforce -- see `UPLOAD.md`. |
| Recurrence relations | `ds-08-climb-stairs` | Both rest on a recurrence. Hanoi's doubles, Fibonacci's adds. Asking for both on one exam is fine; asking the same derivation twice is not. |
| Tail recursion and conversion to a loop | `ds-08-palindrome` | Deliberate pair: one converts trivially, the other does not. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Ask for one move -- which disk moves at step k |
| English (ds) | Adjacent pegs only, and the $3^n - 1$ recurrence |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
