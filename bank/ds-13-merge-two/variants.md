# Exam variation axes: ds-13-merge-two

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

There is no Korean counterpart, so every axis below is available to the
English section.

## The core of the original problem

Two indices moving forward, never back. Take the smaller front value; when one
array runs out, copy the rest of the other. This is the step merge sort is
built from, and everything about merge sort's cost follows from it being
$O(n+m)$.

## Variation axes

- **Merge in place**: `a` has room at the end for `b`'s values. Filling from
  the front overwrites what has not been read yet, so the merge has to run
  **backwards** from the largest. A good exam question because the fix is not
  obvious and is one line.
- **Build merge sort from it**: given this method, write merge sort. Then: how
  many times is each value copied? $\log n$ times, which is where the
  $O(n \log n)$ comes from.
- **Ask about the tie**: taking from the left on a tie makes the merge stable.
  Why does it not matter for `int[]`, and when would it? **This is the best
  short exam question here** -- it joins to `ds-12-sort-records`, and the
  answer is that equal ints are indistinguishable while equal records are not.
- **Merge k arrays**: pairwise versus a heap. Ties to `ds-11-merge-k`; ask for
  the cost of merging them one after another ($O(Nk)$) against tournament
  order ($O(N \log k)$).
- **Ask about the space**: this merge needs an output array of size $n+m$.
  What does that make merge sort's space complexity, and how does it compare
  with quicksort's?
- **Intersection or difference** instead of union: the same two-pointer sweep,
  a different rule at each step.
- **Trace by hand**: two short arrays, list which array each output value came
  from.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Merging two sorted sequences | `ds-05-merge-sorted` | That problem merges two linked **lists** by relinking, with no new nodes. Here it is arrays with an output buffer. The contrast -- relink versus copy -- is a good single question. |
| Merging k sequences | `ds-11-merge-k` | Chapter 11 owns the heap version. |
| The merge step counting something | `ds-13-inversions` | That problem hangs a count on this exact loop. Teach this one first. |
| Stability | `ds-12-sort-records` | That problem owns stability as a requirement. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Merge in place into `a`, and why it must run backwards |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
