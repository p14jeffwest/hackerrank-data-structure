# Exam variation axes: ds-13-counting-sort

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

There is no Korean counterpart, so every axis below is available to the
English section.

## The core of the original problem

Count, prefix-sum, place. No two values are ever compared, so the $O(n \log n)$
lower bound for comparison sorts does not apply -- at the price of an array as
large as the value range.

## Variation axes

- **Ask about the back-to-front pass**: why place from the end of the input
  rather than the start? Because that is what makes the sort stable. Then:
  why does it not matter for `int[]`, and where does it? **This is the best
  exam question here** -- the answer is 13.5, where radix sort needs each
  digit pass to leave the previous digit's order alone, and 13.5's own Check
  Your Understanding asks exactly that.
- **Allow negative values**: shift everything by `-min` before counting and
  back afterwards. 13.5 mentions this for radix sort. One line, and students
  reliably forget the shift on the way out.
- **Sort records, not ints**: a key plus a payload. Now stability is visible
  and the placement pass has to carry the payload. This is where counting sort
  and `ds-12-sort-records` meet.
- **Ask for the cost trade-off**: when is $O(n + k)$ worse than $O(n \log n)$?
  When `k` dwarfs `n` -- case 09 of this problem is that shape, 50 values over
  a range of a million. Give numbers and ask which to use.
- **Build radix sort from it**: sort six-digit numbers by applying this to one
  digit at a time. That is 13.5 in full, and it needs the stability question
  answered first.
- **Sort strings of fixed length**: the same idea over an alphabet instead of
  a numeric range.
- **Ask what the prefix sum means**: after step 2, what does `count[v]` hold?
  The number of values at most `v`, which is also the index just past where
  the `v`s belong. Short and exact.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Stability | `ds-12-sort-records` | That problem owns stability as a requirement. Here it is invisible in the output and lives in the exam. |
| The 0/1/2 array | 12.7 Level 3 Problem 6 (Dutch National Flag) | Not a contest problem, so the three-pointer $O(1)$-space version is free exam material -- and it is a good contrast, same input and a different method. |
| Non-comparison sorting | 13.5 radix sort | Radix sort is not a contest problem here either. It is the natural sequel and depends on this one. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Why the placement pass runs backwards, and what breaks in radix sort if it does not |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
