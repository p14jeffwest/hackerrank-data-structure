# Exam variation axes: ds-11-merge-k

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

There is no Korean counterpart, so every axis below is available to the
English section.

## The core of the original problem

Only the front of each list can be the next smallest, so the heap holds one
candidate per list and never grows past `k`. Take the smallest, write it down,
and put back the next element of the list it came from.

## Variation axes

- **Ask only for the first m values**: with `m` far smaller than `N`, sorting
  everything is wasteful and the heap is not. **This is the sharpest exam
  question here**, because it is exactly the difference the contest version
  cannot enforce -- see the note below.
- **Ask for the cost comparison**: heap merge, pairwise merging, and sorting
  everything -- $O(N \log k)$, $O(Nk)$, $O(N \log N)$. When is each best?
  Sorting wins when `k` is close to `N`; the heap wins when `k` is small or
  the lists arrive as streams.
- **Merge two at a time**: merge lists 1 and 2, then that with 3, and so on.
  Give `k` equal lists and ask for the total work. It is $O(Nk)$, and seeing
  why is the point.
- **Merge in pairs instead**: merge them tournament-style, halving `k` each
  round. That is $O(N \log k)$ with no heap at all. Ask why.
- **Report the source**: alongside each value, which list it came from. The
  heap already carries that; sorting would have to be told to.
- **Streams instead of arrays**: the lists cannot be held in memory and can
  only be read forwards. Which methods survive? Only the heap.
- **Trace by hand**: three short lists, list the heap contents after each
  step.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Merging two sorted sequences | `ds-05-merge-sorted` | That problem merges two linked lists by relinking. This one merges k arrays. The pair is a good "what changes when k grows" question. |
| Using `PriorityQueue` | `ds-11-meeting-rooms`, `ds-11-median-stream` | Three application problems share the tool. Vary the question. |
| k-way merge in sorting | chapter 13 | Merge sort is chapter 13's. Keep the sorting connection there. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Only the first m values -- why sorting everything now loses |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
