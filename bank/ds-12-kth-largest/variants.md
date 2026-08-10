# Exam variation axes: ds-12-kth-largest

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-13-kth-smallest`, the same algorithm in the opposite
direction, so the axes must be split.

## The core of the original problem

Sort and index from the far end, or keep a min-heap of size `k`. The content
is the counting -- `k` from 1, duplicates counted separately, and the index
`n - k` rather than `k - 1`.

## Variation axes

- **Ask when each method wins**: full sort $O(n \log n)$ against a size-`k`
  heap $O(n \log k)$. For which `k` does the heap pay? What if `k` is 1, or
  `n`? **This is the best exam question here**, and it is the comparison 12.8
  Problem 1 is actually about -- see the note below on why the contest cannot
  ask it.
- **Quickselect**: partition around a pivot and recurse into one side only,
  $O(n)$ on average. **Reserved for the Korean section**, whose stub sketches
  it. Ask for the average and worst cases, and what a fixed first-element
  pivot does to already-sorted input.
- **The k-th distinct largest**: now duplicates collapse. One line different,
  and it is the mistake this problem punishes turned into the requirement.
- **The k smallest and the k largest at once**: what is the cheapest way to
  get both?
- **A running k-th largest**: values arrive one at a time and the k-th largest
  is asked for after each. Now only the heap works. Ties to
  `ds-11-median-stream`.
- **Ask about the index**: after an ascending sort, why is the k-th largest at
  `n - k`? Give `n = 6`, `k = 2` and ask for the index. Cheap and exact.
- **Ask about stability**: does it matter here? No -- equal values are
  indistinguishable, so any correct sort gives the same answer. A good
  contrast with `ds-12-sort-records`.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The same algorithm, other direction | `dsa-13-kth-smallest` (Korean set) | Same problem. The reserved split below keeps the exams apart. |
| Size-k heap | `ds-11-merge-k` | Chapter 11 owns heaps as a structure. Here the heap is one of two choices. |
| Streaming order statistics | `ds-11-median-stream` | The running variation belongs with that problem, not this one. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Quickselect -- partition, average and worst case, bad pivots |
| English (ds) | When the size-k heap beats a full sort, and when it does not |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
