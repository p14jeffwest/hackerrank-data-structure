# Exam variation axes: ds-05-merge-sorted

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-07-merge-sorted` from the same source problem, so the
axes must be split carefully. That version presents it as two queues of people
merging by number; this one keeps the book's framing and enforces the
no-new-nodes rule.

## The core of the original problem

Merge two sorted linked lists by relinking their nodes. A dummy head removes
the special case of choosing the first node, and when one list runs out the
other is attached whole.

## Variation axes

- **Merge more than two**: k sorted lists at once. Merging them pairwise is
  $O(kn)$ and merging with a heap is $O(n \log k)$ -- which makes this the
  natural bridge into chapter 11. **Save it for after heaps.**
- **Change the ordering**: merge descending; merge by absolute value; merge by
  a key while keeping ties in first-list-first order, which finally makes the
  `<` versus `<=` choice observable.
- **Ask about stability**: given two lists containing equal values, which node
  ends up first under `<=` and which under `<`? No test can see the
  difference, so an exam is the only place to ask it.
- **Change the structure**: merge two sorted *doubly* linked lists, where every
  step has to fix `prev` as well; merge two sorted circular lists, where there
  is no `null` to stop at.
- **Drop the sortedness**: the two lists are not sorted, so the answer is a
  full sort. Ask what changes and why the linked structure is now a
  disadvantage. Connects to 13.1, where merge sort on linked lists comes back.
- **Remove the dummy**: write it without a dummy head and enumerate the extra
  cases that appear. There are more than students expect, and the empty-list
  cases are the ones they miss.
- **Ask what the dummy costs**: one node's worth of memory, no time. Then ask
  why it is not flagged by the driver's node check.
- **Trace by hand**: give two short lists and ask for the sequence of
  `current.next` assignments, not just the final list.
- **Split instead of merge**: given one sorted list, split it into two by
  alternating nodes. The inverse operation, same technique.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The merge itself | `dsa-07-merge-sorted` (Korean set) | Same source problem. The reserved split below keeps the two exams apart. |
| Dummy head | `ds-05-kth-from-end` variants | Only as a follow-up there. This problem owns the dummy. |
| Merging as a sorting step | chapter 13 (merge sort) | Chapter 13 owns merge sort. Keep this one about the relinking. |
| k-way merge | chapter 11 (heaps) | Reserved for chapter 11; do not spend it here. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Remove the dummy -- enumerate the cases it was hiding |
| English (ds) | Stability -- which node comes first under `<` and under `<=` |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
