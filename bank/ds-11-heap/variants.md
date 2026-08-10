# Exam variation axes: ds-11-heap

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean chapter 11 has no heap-implementation problem, so every axis below
is available to the English section.

## The core of the original problem

Two movements. `push` appends and walks the value up while it is smaller than
its parent; `pop` takes the root, moves the last value into the gap, and walks
it down, always swapping with the smaller child. Both travel the height of the
tree and no further.

## Variation axes

- **Make it a max-heap**: one comparison flips in each method. Then ask how
  Java's `PriorityQueue` is turned into one, which 11.5's preamble answers.
- **Add an operation**: `decreaseKey(i, v)`, which needs an up-heap from `i`;
  `delete(i)`, which needs whichever direction the replacement value calls
  for -- and deciding *which* is the interesting part.
- **Build a heap from an array**: 11.4's two ways, bottom-up and top-down. Ask
  which is $O(n)$ and which is $O(n \log n)$, and why the difference is not
  the other way round. **This is the best exam question here** -- it is the
  one part of 11.4 no contest problem reaches.
- **Trace by hand**: 11.5's Level 1 Problems 1 and 2 are exactly this, and
  samples 00 and 01 are their answers, so students can be told to check
  themselves.
- **Ask which array is a heap**: 11.5 Level 1 Problem 3. Cheap and exact.
- **Ask what breaks**: down-heap swapping with the larger child -- give a
  small heap, one pop, and ask for the resulting array. It is not obviously
  broken, which is the point.
- **Ask about the shape**: why does appending at the end preserve the complete
  binary tree, and why does moving the LAST value to the root preserve it too?
  Any other choice does not.
- **Count the work**: how many comparisons does a `pop` make on a heap of
  1,000? 11.3's Check Your Understanding asks precisely this.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Using a priority queue | `ds-11-merge-k`, `ds-11-meeting-rooms`, `ds-11-median-stream` | Those three all use `PriorityQueue`. This is the only one that builds it, so keep implementation questions here and application questions there. |
| Array representation of a tree | `ds-09-traversal` | Chapter 9 uses links; here the tree is implicit in the indices. The contrast is worth one question. |
| Heap sort | chapter 12 | 11.3 item 4 notes that repeated `pop` sorts. Chapter 12 owns heap sort. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Building a heap from an array -- bottom-up versus top-down, and why one is $O(n)$ |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
