# Exam variation axes: ds-09-path-sum

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-10-path-sum`, the same problem, so the axes must be
split.

## The core of the original problem

Carry the remaining amount down instead of the running total up. The two
decisions that matter are what to answer at a leaf, and what to answer at a
missing child.

## Variation axes

- **Return the path**: the values along a path that reaches the target, or
  every such path. Collecting them needs the same backtracking as
  `ds-08-subsets`, so it is a good bridge question.
- **Count instead of decide**: how many root-to-leaf paths sum to the target?
  One line different, and it stops a student from returning early.
- **Drop the leaf requirement**: any downward path, not just root-to-leaf.
  Much harder, and the interesting part is realising the answer is no longer
  a single walk.
- **Ask about the missing child**: why must `hasPathSum(null, t)` be false
  rather than `t == 0`? **This is the sharpest exam question here** -- the
  wrong version reads like a correct base case, and saying exactly which trees
  it breaks (those with one-sided nodes) requires understanding rather than
  recall.
- **Ask about pruning**: when is it safe to stop descending because the
  remainder went negative? Only when every value is positive. Give a tree with
  negative values and ask for the path that the pruning misses.
- **Change the question**: the maximum root-to-leaf sum; the minimum; the
  number of distinct path sums.
- **Ask about the cost**: each query re-walks the tree, so `Q` queries cost
  $O(nQ)$. How would you answer many queries faster? (Collect every path sum
  once into a set.) That is the right answer and it changes the space from
  $O(h)$ to $O(\text{leaves})$.
- **Trace by hand**: give a small tree and a target and list the value of
  `target` at each call.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The problem itself | `dsa-10-path-sum` (Korean set) | Same problem by design. The reserved split below keeps the exams apart. |
| What a leaf is | `ds-09-count-leaves` | Both punish treating a one-sided node as a leaf. Ask it once. |
| Backtracking to collect a path | `ds-08-subsets` | Chapter 8 owns backtracking. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Count the paths, or return one of them |
| English (ds) | Why the missing child must answer false, and which trees the other version breaks |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
