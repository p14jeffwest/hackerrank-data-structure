# Exam variation axes: ds-07-last-card

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-06-last-card`, deliberately the same problem in the
same format, so the axes must be split.

## The core of the original problem

Discard the front card, send the next one to the back, repeat. Two dequeues
and one enqueue per round, and the only real decision is which structure makes
removal from the front $O(1)$.

## Variation axes

- **Change the ratio**: discard one and move `m` to the back, or move one and
  discard `m`. Same loop, different arithmetic, and it stops any memorised
  answer from carrying over.
- **Generalise to Josephus**: remove every `K`-th person from a circle. This
  is 7.5 Problem 5, and this problem is its `K = 2` case. Asking a student to
  see that connection is worth more than asking them to code it again.
- **Find the closed form**: for cards numbered 1..N, the survivor is
  $2(N - 2^{\lfloor \log_2 N \rfloor}) $ adjusted at the boundary. Derive it,
  or just tabulate N = 1..16 and describe the pattern. **This is the sharpest
  exam question here**, and it is available precisely because the contest
  version blocks it by using arbitrary card values.
- **Run it backwards**: given the discard order, reconstruct the starting
  deck. Harder than it looks and a good challenge item.
- **Ask which position survives**: not the value, but the index it started at.
  One line different in the code, and it separates students who tracked
  positions from those who tracked values.
- **Ask about the cost**: why does `ArrayList.remove(0)` make this $O(N^2)$,
  and what does `ArrayDeque` do instead? Ties directly to 7.3 -- the circular
  array is the answer.
- **Trace by hand**: eight cards, list the deck after each round. Cheap and
  exact.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The simulation itself | `dsa-06-last-card` (Korean set) | Same problem by design. The reserved split below keeps the exams apart. |
| Circular elimination | 7.5 Problem 5 (Josephus) | Not a contest problem here, so the whole Josephus family is free as exam material. |
| Front removal costing $O(n)$ | `ds-07-circular-queue` | That problem builds the structure that fixes it; this one shows why it matters. Good as a pair, bad as two questions on one exam. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Generalise to Josephus -- remove every K-th |
| English (ds) | The closed form for cards 1..N |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
