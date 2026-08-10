# Exam variation axes: ds-07-sliding-window-max

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean book has no deque section and no equivalent exercise, so every axis
below is available to the English section.

## The core of the original problem

A deque of **indices**, held in decreasing order of the values they point at.
Drop expired indices from the front, drop beaten indices from the rear, and
the front is the current maximum. Every index enters and leaves once, so the
pass is $O(n)$.

## Variation axes

- **Change what is tracked**: the minimum instead of the maximum (one
  comparison flips); both at once; the maximum *and* its position; the number
  of distinct maxima across all windows.
- **Change the window**: a window that grows rather than slides, so the answer
  is a running maximum; two windows of different sizes at once; a window
  defined by a value range rather than a count.
- **Ask for the amortized argument**: the inner `while` loops can each run
  many times in a single iteration, so why is the whole pass $O(n)$? Each
  index is offered exactly once and polled at most once. **This is the best
  exam question here**, and it is the third appearance of that accounting
  pattern in the course -- see the overlap table.
- **Ask about indices versus values**: why must the deque hold indices? Give
  a strictly decreasing array and the value-based version, and ask for the
  first window where it goes wrong. Sample 02 is exactly that input, so the
  question can be set from material students have already seen.
- **Bound the deque**: what is the largest number of indices it ever holds,
  and which input achieves it? ($k$, on a strictly decreasing array.) And the
  smallest? (One, on a strictly increasing array.)
- **Trace by hand**: the book's own eight-element example, asking for the
  deque contents after each step. The walkthrough in 7.5 is already written
  in exactly that form.
- **Compare with a heap**: a priority queue with lazy deletion solves this in
  $O(n \log k)$. Ask what the deque exploits that the heap does not -- the
  answer is that expiry is always from the front, which a heap cannot use.
  Best saved for after chapter 11.
- **Run it backwards**: given the sequence of window maxima and `k`, say
  whether some array could produce it.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Monotonic structure, "each index enters and leaves once" | `ds-06-daily-temperatures`, `ds-06-queue-two-stacks`, `ds-04-array-growth` | Four problems now rest on amortized accounting. Chapter 4 owns the doubling version, chapter 6 the stack version. If this axis is used here, use none of the others on that exam. |
| Deque operations | `ds-07-circular-queue` | That problem can ask how a deque is built; this one uses it. Good as a pair. |
| Comparison with a heap | chapter 11 | Chapter 11 owns priority queues. Keep the comparison for then. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Indices versus values -- find the first window where the value-based deque is wrong |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
