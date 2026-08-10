# Exam variation axes: ds-09-diameter

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean chapter 10 has path sum as its Level 3 walkthrough rather than the
diameter, so every axis below is available to the English section.

## The core of the original problem

One recursion doing two jobs. The **return value** is the height, which is
what the parent needs. The **field** is the largest path seen so far, which is
what the answer needs. Confusing the two is the usual way this goes wrong.

## Variation axes

- **Return the path, not its length**: the two endpoints, or the sequence of
  values along it. Same recursion, more bookkeeping, and it forces the student
  to be precise about which node the path turns at.
- **Weight the edges**: each node carries a value and the path length is the
  sum of the values on it. The recursion is unchanged; only what is added
  changes. A good exam version because a memorised solution does not transfer.
- **Change the units**: the diameter in nodes rather than edges. One line, and
  it tests whether the -1 base case was understood or copied.
- **Ask for the base case**: why does an empty subtree report **-1**? Because
  a leaf's two children then report -1 each, and `1 + max(-1, -1)` is 0, which
  is the leaf's height. Also: what does the path-through-here formula become
  if 0 is used instead?
- **Ask about the cost**: what does "compute the height at every node" cost,
  in terms of the number of nodes and the height, and which tree shape is
  worst? **This is the best exam question here**, because the answer is
  $O(n \cdot h)$ and not $O(n^2)$, and getting that right requires actually
  thinking about the shape rather than reciting a bound.
- **The same trick elsewhere**: is the tree height-balanced? The naive
  version recomputes heights and the good one returns height and balance
  together. Overlaps with `ds-09-count-leaves`; use one or the other.
- **Trace by hand**: give a small tree and ask, for each node, what the
  recursion returns and what the running maximum becomes.
- **Prove it**: why is it enough to consider, at each node, only the path that
  turns at that node? Because every path turns at exactly one node -- its
  highest. That sentence is the whole proof and it is worth asking for.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Return one thing, accumulate another | `ds-09-count-leaves` variants | The balance-check question uses the same trick. Do not set both. |
| Height in edges versus nodes | `ds-09-count-leaves` | That problem asks for both explicitly. Here it is a trap. Ask it once. |
| Recursion depth versus tree shape | `ds-09-traversal` | Same cap, same reason. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | The cost of the naive version, and which tree shape is worst |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
