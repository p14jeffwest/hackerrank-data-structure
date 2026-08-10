# Exam variation axes: ds-09-count-leaves

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-10-count-leaves`, the same problem without the third
method, so the axes must be split.

## The core of the original problem

One recursion shape, three combining steps: settle the empty case, then
combine what the two children return. The content is the definitions -- what
counts as a leaf, and which unit the height is measured in.

## Variation axes

- **Count something else**: internal nodes; nodes with exactly one child;
  nodes at a given depth; the total number of nodes. All are the same walk
  with a different combining line, which is the point worth making once.
- **Ask for the units**: given a tree, state its height in edges and in nodes,
  and say which section of the book uses which. Cheap, exact, and it is the
  distinction the book itself flags.
- **The empty tree**: what should each of the three return for `null`, and
  why is `height(null)` **-1** rather than 0? Because a leaf's children report
  -1 and `1 + max(-1, -1)` is 0, which is the leaf's height. **This is the
  best short exam question here** -- the answer explains itself and cannot be
  guessed.
- **Add a balance check**: is the tree height-balanced, meaning the two
  subtrees of every node differ in height by at most one? The naive version
  recomputes the height at every node and is $O(n^2)$; returning height and
  balance together makes it $O(n)$. That is the same trick
  `ds-09-diameter` uses, so do not spend both.
- **Minimum depth**: the shortest root-to-leaf path. Sounds symmetric to the
  maximum and is not -- a one-sided node must not be treated as a leaf, which
  is exactly the trap this problem already carries.
- **Count leaves without recursion**: with the queue from chapter 7. Ask what
  changes in the space used.
- **Trace by hand**: give a small tree and ask for the value each recursive
  call returns, from the bottom up.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The problem itself | `dsa-10-count-leaves` (Korean set) | Same problem by design. The reserved split below keeps the exams apart. |
| Returning a value up the recursion | `ds-09-diameter` | That problem returns a height *and* maintains a maximum. Keep the "return two things at once" question there. |
| Recursion depth versus tree shape | `ds-09-traversal` | Same cap, same reason. Ask once. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Count something else -- internal nodes, or nodes at a given depth |
| English (ds) | Why `height(null)` is -1, and what breaks if it is 0 |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
