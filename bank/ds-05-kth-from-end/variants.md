# Exam variation axes: ds-05-kth-from-end

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

There is no Korean counterpart, but the Korean set does contain
`dsa-07-find-middle`, which is the same two-pointer idea. The reserved axes
below keep the two exams from asking the same question in different clothes.

## The core of the original problem

Return the data of the k-th node from the end without knowing the length. Two
pointers a fixed gap apart do it in one pass: the gap is preserved as both
advance, so when the leading one falls off the end the trailing one is exactly
k nodes behind it.

## Variation axes

- **Change what the gap is for**: the middle node, which is 5.5 Problem 5 and
  the same idea with a gap that grows -- one pointer moving twice as fast as
  the other. **Reserved for the Korean section**, which already has this as
  `dsa-07-find-middle`.
- **Remove the guarantee**: allow `k > n` and require a defined answer rather
  than a crash. Small change, and it forces the student to notice that the
  leading pointer can run out during the head start.
- **Change what is returned**: return the node's position from the front;
  remove the k-th node from the end and return the new head (the classic
  follow-up, and the dummy-head idea from 5.6 Problem 1 makes the k = n case
  clean); return the k-th from the end of a *doubly* linked list, where the
  answer is k-1 steps back from `tail` and the whole difficulty disappears.
- **Change the direction**: the k-th node from the front, and ask why that one
  needs no trick.
- **Ask for the invariant**: state precisely what is true of the two pointers
  at every step, and use it to argue the answer is right. The gap being
  constant is the entire proof.
- **Trace by hand**: give a short list and a k, and ask for the positions of
  both pointers after each step.
- **Ask about the cost**: compare one pass with two (measure the length, then
  walk n-k), and with copying the nodes into an array. All three are $O(n)$
  time; they differ in passes and in space. A good question is which of them
  survives if the list can only be read once, as from a stream.
- **Find the bug**: give the loop with `k - 1` steps of head start and ask
  which input first shows the error.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Two pointers with a gap | `dsa-07-find-middle` (Korean set) | Same technique. The Korean exam owns the middle-node version; keep the k-th-from-end version here. |
| Dummy head | `ds-05-merge-sorted` | That problem owns it. Only relevant here in the "remove the k-th node" variation. |
| Walking from `head` costs $O(n)$ | `ds-05-linked-list`, `ds-05-iterator-scan` | Those own the cost argument. Here it is background. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | The middle node -- one pointer twice as fast |
| English (ds) | Remove the k-th node from the end and return the new head |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
