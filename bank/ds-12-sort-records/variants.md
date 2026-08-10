# Exam variation axes: ds-12-sort-records

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-13-sort-records`, the same problem, so the axes must be
split.

## The core of the original problem

Sort descending on the score alone, and let stability take care of the ties.
The two ways of getting it wrong are reversing after an ascending sort, and
adding a tie-break the problem did not ask for.

## Variation axes

- **Ask for the definition**: what does it mean for a sort to be stable, and
  which of bubble, selection, insertion and heap sort are? That is 12.7 Level
  1 Problem 2's stability column, and it is not a contest problem here.
- **Ask which Java sort is stable**: `Arrays.sort` on objects is a merge sort
  and stable; on primitives it is a quicksort and is not. Why does the
  difference not matter for `int[]`? **This is the best exam question here** --
  the answer is that equal ints are indistinguishable, so there is nothing for
  stability to preserve.
- **Break it deliberately**: give a comparator with a name tie-break and ask
  what it changes, and which participants move.
- **Ask about reversing**: sorting ascending and flipping the array gives the
  scores in the right order. What exactly is wrong with it? Give an input
  where it shows.
- **Two keys for real**: order by score descending and, among equal scores, by
  name ascending. Now the tie-break IS wanted, and the question becomes how to
  write a two-level comparator -- the opposite lesson, and worth setting after
  this one.
- **Sort by a derived key**: by the length of the name, by the last letter, by
  score modulo 10. Stability becomes visible in each.
- **Make stability necessary**: sort by score, then by something else, in two
  separate passes. The result is correct only because the second sort is
  stable, and explaining that is a real question.
- **Ask about the comparator contract**: what happens if a comparator is
  inconsistent -- say it reports `x < y` and `y < x`? Java throws
  `IllegalArgumentException: Comparison method violates its general contract`.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The problem itself | `dsa-13-sort-records` (Korean set) | Same problem by design. The reserved split below keeps the exams apart. |
| Stability as a property of the basic sorts | `ds-12-sort-trace` | That problem traces selection sort, which is unstable. Asking there "does this preserve ties?" is the natural link. |
| Comparators | `ds-11-meeting-rooms`, `ds-12-merge-intervals` | Both sort by a key with `Comparator.comparingInt`. Those own the sorting-as-preprocessing question. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Two keys for real -- score descending, then name ascending |
| English (ds) | Why `Arrays.sort` differs for objects and primitives, and why it does not matter for `int[]` |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
