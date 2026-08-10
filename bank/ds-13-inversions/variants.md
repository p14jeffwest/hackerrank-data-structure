# Exam variation axes: ds-13-inversions

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-14-inversions`, the same problem, so the axes must be
split.

## The core of the original problem

A count hung on merge sort's merge step. Taking one value from the right half
settles, in one addition, every inversion it forms with what is still left in
the left half. The sorting is a by-product; the count is the answer.

## Variation axes

- **Ask why one addition suffices**: when a right value is taken, why are
  *all* the remaining left values larger than it? Because the halves are
  sorted, so if the left front is larger, everything behind it is too. **This
  is the best exam question here** -- it is one sentence and it cannot be
  answered by having memorised the code.
- **Ask about the tie**: which comparison keeps equal values out of the count,
  and what does the other one count instead? Ties to `ds-13-merge-two`, where
  the same line is about stability.
- **Count a different relation**: pairs with `a[i] > 2 * a[j]`; pairs at
  distance at most `k`; pairs in a given index range. The first is the
  interesting one -- the merge no longer counts it for free and needs a second
  sweep.
- **Solve it another way**: a Fenwick tree over the ranks, sweeping from the
  right. Same $O(n \log n)$, completely different reasoning -- and it is what
  `gen.py` uses. Reserve for after any Fenwick material.
- **Ask what the answer means**: the number of swaps bubble sort would make.
  Give a small array and ask for both, and for why they agree.
- **Ask for the bound**: what is the largest possible answer for `n` values,
  and which arrangement achieves it? $n(n-1)/2$, strictly descending -- and
  that is why the count needs a `long`.
- **Trace by hand**: eight values, list what each merge adds.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The problem itself | `dsa-14-inversions` (Korean set) | Same problem by design. The reserved split below keeps the exams apart. |
| The merge step | `ds-13-merge-two` | That problem is this one's merge without the counting. Teach it first; do not examine both. |
| Overflow into `long` | `ds-tutorial-03-sum`, `ds-08-climb-stairs` | The tutorial owns the lesson. Here it is a secondary trap. |
| Bubble sort's swap count | `ds-12-sort-trace` variants | The "count the swaps" axis there is the same number. Pick one section for it. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | The largest possible answer, and why the count needs a `long` |
| English (ds) | Why one addition settles a whole block of inversions |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
