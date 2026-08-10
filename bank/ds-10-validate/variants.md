# Exam variation axes: ds-10-validate

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

There is no Korean counterpart, so every axis below is available to the
English section.

## The core of the original problem

A node is constrained by every ancestor, not just its parent. Going left
tightens the upper bound, going right tightens the lower bound, and each node
must sit strictly inside the window its ancestors leave it.

## Variation axes

- **Give a tree, ask where the rule breaks**: this is 10.5 Problem 2 with the
  answer required rather than the verdict. Cheap to mark and impossible to
  guess.
- **Ask for the counterexample**: give the parent-only check as code and ask
  for the smallest tree it accepts wrongly. Four nodes suffice. **This is the
  best exam question here** -- it needs the misconception to be understood
  rather than avoided.
- **Validate by inorder**: a tree is a BST exactly when its inorder traversal
  is strictly increasing. Ask for that version, and then ask why it needs the
  comparison to be strict.
- **Allow duplicates**: decide what "valid" should mean if equal keys were
  permitted -- all duplicates on the left, or all on the right -- and adjust
  the bounds. Ties to `ds-10-bst`, which ignores duplicate inserts.
- **Ask about the bounds type**: why `long` and not `int`? Because with keys
  reaching both int limits there is no int value left to mean "unbounded".
  What else could be used instead? (`Integer` objects with `null` for no
  bound, or a boolean flag per side.)
- **Return more than a verdict**: the number of nodes that break the rule, or
  the deepest one.
- **Validate other structures**: is this tree a max-heap? Chapter 11 makes
  that the natural sequel, and the contrast is instructive -- a heap's rule is
  purely parent-child, which is exactly what a BST's is not.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The ancestor rule | `ds-10-bst` | That problem builds trees that obey it; this one checks. Complementary. |
| Inorder gives sorted order | `ds-09-traversal`, `ds-10-range-sum` | Chapter 9 owns traversal itself. Here it is an alternative solution. |
| Heap validation | chapter 11 | Reserve for chapter 11, where the parent-child-only contrast lands. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Give the parent-only check and ask for the smallest tree it wrongly accepts |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
