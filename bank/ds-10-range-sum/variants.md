# Exam variation axes: ds-10-range-sum

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

There is no Korean counterpart, so every axis below is available to the
English section.

## The core of the original problem

The BST rule says where the answer cannot be. Above `high`, the right subtree
is out; below `low`, the left one is. Only a node inside the range makes the
walk continue both ways -- and by then it is part of the answer.

## Variation axes

- **Change what is aggregated**: count the keys in the range instead of
  summing them; the largest key in the range; the keys themselves, in order.
  The last one is the natural bridge to an inorder traversal with pruning.
- **Change the range**: half-open `[low, high)`; everything except the range;
  the k-th smallest key at least `low`.
- **Ask for the cost**: what does one query cost with pruning, and what
  without? The pruned version is the height plus the number of keys reported,
  which is worth writing out precisely -- it is not $O(\log n)$ and saying why
  is the real question. **This is the best exam question here.**
- **Ask which subtree is skipped and why**: give a tree and a range and mark
  the nodes never visited. Short, exact, and it cannot be answered by pattern.
- **Precompute instead**: with many queries against an unchanging tree, what
  would you build once to answer each in $O(\log n)$? (A sorted key array with
  prefix sums, which is what `gen.py` does.) Then: what breaks if the tree can
  change between queries?
- **Ask about the type**: how large can one answer get, given the node count
  and key range? Ties to `ds-tutorial-03-sum`, so do not use both.
- **Do it without a BST**: the same query on an unsorted binary tree. Nothing
  can be pruned, and saying why makes the BST rule's value concrete.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The BST ordering rule | `ds-10-validate`, `ds-10-bst` | Those build and check it; this one exploits it. Complementary. |
| Overflow into `long` | `ds-tutorial-03-sum`, `ds-08-climb-stairs` | The tutorial owns the lesson; here it is a secondary trap. |
| Inorder gives sorted order | `ds-09-traversal` | The "return the keys in the range in order" variation joins the two. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | The cost of one pruned query, stated exactly |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
