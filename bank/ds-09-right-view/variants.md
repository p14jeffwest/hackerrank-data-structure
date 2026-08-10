# Exam variation axes: ds-09-right-view

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-10-level-max`, which asks for the largest value at
each level. Different question, same technique, so the axes still have to be
split.

## The core of the original problem

A level-order traversal with the levels kept apart by recording
`queue.size()` at the start of each round. The last node of each round is the
one visible from the right.

## Variation axes

- **Change what is taken from each level**: the largest value (**reserved for
  the Korean section**, which has it as `dsa-10-level-max`); the average; the
  count; the sum. All are the same loop with a different accumulator.
- **Change the direction**: the left side view, which is the first node of
  each level rather than the last.
- **Change the shape of the output**: the levels as separate lines, which is
  the plain "level order by levels" problem and the natural stepping stone.
- **Zigzag**: alternate left-to-right and right-to-left by level.
- **Do it with recursion**: visit the right subtree before the left, and
  record a node the first time a new depth is reached. Ask why visiting right
  first is what makes it work, and what the same code gives if left is visited
  first. **This is the best exam question here** -- it tests the idea rather
  than the loop.
- **Ask what `levelSize` buys**: what does the output become without it?
  (The whole traversal, or only its last node, depending on where the append
  sits.)
- **Ask about the space**: the queue holds at most one level, so the space is
  the width of the widest level, not the height. Which tree shape is worst?
  A complete tree, where the last level is half of all the nodes.
- **Trace by hand**: give a small tree and ask for the queue contents at the
  start of each round.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Largest value per level | `dsa-10-level-max` (Korean set) | Reserved for the Korean exams. |
| Level-order traversal, flat | `ds-09-traversal` | That problem owns plain level order. This one owns the level *boundary*. |
| Width versus height in space | `ds-09-traversal` | Same observation. Ask it once. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Largest value per level, and the other per-level accumulators |
| English (ds) | The recursive version -- why the right subtree must be visited first |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
