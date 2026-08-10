# Exam variation axes: ds-08-climb-stairs

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-09-climb-stairs`, the same problem, so the axes must
be split.

## The core of the original problem

`ways(n) = ways(n-1) + ways(n-2)` with `ways(1) = 1` and `ways(2) = 2`. The
recurrence is easy; what the problem tests is filling the table once instead
of re-deriving it, and choosing a type wide enough for the answer.

## Variation axes

- **Change the step sizes**: 1, 2 or 3 steps at a time, giving a tribonacci
  recurrence; steps of 1 and 3 only; steps of any size up to `k`. The first is
  the natural exam version -- the derivation is the same and no memorised
  Fibonacci helps.
- **Forbid some steps**: certain stairs are broken and cannot be landed on.
  One extra line in the loop, and it turns the problem into a genuine dynamic
  programme rather than a sequence lookup.
- **Ask for the type analysis**: given the step sizes and `n`, how large does
  the answer get, and what is the narrowest type that holds it? **This is the
  best exam question here** -- it is the whole reason the bound is 90 rather
  than the book's 45.
- **Ask about the cost**: why is the plain recursion $O(2^n)$? How many calls
  does `ways(20)` make? 8.2 item 4 tabulates the answer, so this can be set
  from material students have read.
- **Compare the three shapes**: plain recursion, memoized recursion, and the
  loop. Same recurrence, three costs in time and space. The loop's $O(1)$
  space is the part students miss.
- **Trace by hand**: fill the table for `n = 1..8` and say which value each
  entry came from.
- **Run it backwards**: given that the answer for some `n` is 89, what is `n`?
- **Count routes with a constraint**: how many routes use exactly `k` double
  steps? This is a binomial coefficient, and connecting the two views is a
  good discussion question.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The problem itself | `dsa-09-climb-stairs` (Korean set) | Same problem by design. The reserved split below keeps the exams apart. |
| Integer overflow | `ds-tutorial-03-sum`, `ds-04-array-growth` | Third appearance. The tutorial owns the lesson; here it is the discriminator. Do not ask about overflow in two places on one exam. |
| Recurrence relations | `ds-08-hanoi` | Hanoi's doubles, this one adds. Both can appear, but not the same derivation twice. |
| Memoization | 8.3 | Chapter 8's own subject, and this is its only appearance in the contest. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Change the step sizes -- 1, 2 or 3 at a time |
| English (ds) | The type analysis -- how large does the answer get, and what holds it |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
