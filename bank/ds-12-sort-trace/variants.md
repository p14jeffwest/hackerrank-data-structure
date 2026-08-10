# Exam variation axes: ds-12-sort-trace

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-13-selection-trace`, the same problem, so the axes must
be split.

## The core of the original problem

One pass settles one position: find the smallest value in what remains and
swap it in. The interesting part is the state **partway** -- the front is
sorted, and the tail is not the original order, because the swaps have thrown
values backwards.

## Variation axes

- **Trace a different sort**: bubble after `k` passes, insertion after
  processing index `k`. **These are 12.7 Level 1 Problem 1 (a) and (c)**, and
  neither is a contest problem here, so both are free exam material. The good
  question is asking for all three on the same array and having students say
  why the states differ.
- **Count instead of trace**: how many swaps does selection sort make on this
  array? How many comparisons? The comparison count is $n(n-1)/2$ whatever the
  input, which surprises people.
- **Run it backwards**: give an array partway through and ask how many passes
  have been done, or what the original could have been.
- **Ask about stability**: selection sort is not stable. Give the smallest
  array that demonstrates it -- three elements is enough -- and ask which
  equal pair changes order. Ties to `ds-12-sort-records`.
- **Ask about the self-swap**: what changes if the swap is skipped when the
  smallest value is already in place? Nothing in the array, and everything in
  the count. Good short question.
- **Ask why the tail is scrambled**: after `k` passes, what can be said about
  positions `k` onwards? Only that they are the remaining values in some
  order. Students expect them untouched.
- **Ask about copying**: the method is told not to modify its argument. Why
  does it matter, and what would go wrong in a caller that reused the array?
  **No test can check this**, so it belongs on an exam.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The problem itself | `dsa-13-selection-trace` (Korean set) | Same problem by design. The reserved split below keeps the exams apart. |
| Stability | `ds-12-sort-records` | That problem owns stability as a requirement. Here it is a property to describe. |
| Complexity of the basic sorts | 12.7 Level 1 Problem 2 | Not a contest problem; free exam material. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Count the swaps and the comparisons |
| English (ds) | Trace bubble and insertion on the same array, and explain the difference |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
