# Exam variation axes: ds-06-queue-two-stacks

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean book has no equivalent exercise, so every axis below is available to
the English section.

## The core of the original problem

Build a FIFO queue from two LIFO stacks. Reversing twice restores the original
order: the inbox reverses on the way in, the outbox reverses again on the way
out. The refill happens only when the outbox is empty, which is what keeps
`dequeue` $O(1)$ amortized.

## Variation axes

- **Turn it around**: build a stack out of two queues. It is the mirror
  problem and it is genuinely harder to make efficient -- one of `push` or
  `pop` has to stay $O(n)$. Asking *why* the asymmetry exists is the good
  version of this question.
- **Add an operation**: `peek()` at the front; `size()` without a counter;
  `isEmpty` if it were not provided. `peek` is the neat one, because it needs
  the same refill decision as `dequeue` and students usually duplicate the
  logic instead of sharing it.
- **Prove the bound**: show that $n$ enqueues and $n$ dequeues cost $O(n)$ in
  total, even though a single `dequeue` can move $n$ elements. The accounting
  argument -- each element is pushed twice and popped twice over its whole
  life -- is short, exact, and impossible to produce from memory alone.
  **This is the best exam question this problem supports.**
- **Break it deliberately**: what goes wrong if the outbox is refilled on
  every `dequeue`? Two separate answers: the order, and the cost. Students who
  only find one have not understood it.
- **Trace by hand**: give a command sequence and ask for the contents of both
  stacks after each step, with the front of the queue marked. The interesting
  moments are the refills.
- **Change the guarantee**: make `dequeue` worst-case $O(1)$ rather than
  amortized. It cannot be done with this design, and saying why is a real
  answer.
- **Bound the memory**: what is the largest total number of elements held
  across both stacks at once, in terms of the number of enqueues?
- **Undo/redo**: 6.2 item 4 describes undo and redo as a pair of stacks moving
  elements between them. Same shape, different purpose, and a good second
  programming question if this one is used for concepts.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Amortized analysis | `ds-04-array-growth`, `ds-06-daily-temperatures` | Three problems now rest on the same idea. Chapter 4 owns the doubling version, chapter 6 the "pushed once, popped once" version. Do not ask two of them on one exam. |
| The provided `ArrayStack` | `ds-06-array-stack` | That problem asks students to write it; this one hands it back. |
| Queue behaviour | chapter 7 | Chapter 7 implements a real queue. This problem should be marked before that chapter, or it stops being surprising. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Prove the amortized bound by the accounting argument |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
