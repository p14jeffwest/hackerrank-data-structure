# Exam variation axes: ds-11-median-stream

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

There is no Korean counterpart, so every axis below is available to the
English section.

## The core of the original problem

Two heaps facing each other, kept within one of each other in size. The
crossing move -- push into `lower`, move its top to `upper`, then move back if
`upper` has grown -- is what maintains both invariants at once, and it is the
whole trick.

## Variation axes

- **Ask for a different order statistic**: the k-th smallest so far, for a
  fixed `k` given up front. Two heaps again, split at `k` instead of in the
  middle.
- **Allow removal**: numbers can also leave the stream. `PriorityQueue.remove`
  is $O(n)$, so the usual answer is lazy deletion with a count of pending
  removals -- a genuine step up and a good challenge item.
- **Ask why two heaps and not one**: a single sorted structure gives the
  median in $O(1)$ but costs $O(n)$ per insertion. What does splitting buy?
  **This is the best short exam question here.**
- **Ask about the invariants**: state precisely what must be true of `lower`
  and `upper` after every `addNum`. There are two conditions, and students
  reliably give only the size one.
- **Trace by hand**: give six numbers arriving in order and ask for the
  contents of both heaps after each. Sample 02's stream works, and its answers
  are already published.
- **Break it deliberately**: what goes wrong if the rebalancing step is
  dropped? Every value ends up on one side and the other heap is empty.
- **Change the tie-breaking**: with an even count, report the lower of the two
  middles rather than their average. One line, and it makes the parity
  question explicit.
- **Ask about the arithmetic**: two values near $10^9$ sum past the `int`
  range. Where exactly does the widening have to happen?

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Two structures maintained together | `ds-06-queue-two-stacks` | Same shape of idea -- two of one thing standing in for another. The amortized argument there and the invariant argument here are different questions, so both can be used. |
| Using `PriorityQueue` | `ds-11-meeting-rooms`, `ds-11-merge-k` | Three application problems share the tool. Vary the question. |
| Overflow when averaging | `ds-tutorial-03-sum` | The tutorial owns the lesson. Here it is a secondary trap. |
| k-th largest | 11.5 Level 2 Problem 5 | Not a contest problem, so it is free as exam material. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Allow removal from the stream -- lazy deletion |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
