# Exam variation axes: ds-10-bst

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-11-bst`, which asks for insert and search only, so the
axes must be split -- and removal is available to the English section, since
the Korean problem does not cover it.

## The core of the original problem

Insert, search and remove, each descending one side per comparison. Removal
splits three ways, and the two-children case is the whole difficulty: the node
cannot be detached, so its key is overwritten by a neighbour in sorted order
and that neighbour is removed instead.

## Variation axes

- **Add an operation**: minimum and maximum; the successor of a given key;
  count the keys in the tree; check membership without recursion.
- **Trace a removal**: given a tree and a key, draw the tree after removing it
  by the predecessor rule, then by the successor rule. Section 10.5 Problem 3
  already asks which case applies; this asks for the result.
- **Ask why the two-children case is different**: cases 1 and 2 detach a node,
  case 3 cannot. Why not? Because both children need a parent and a node has
  only one slot for each.
- **Ask about the alternation**: 10.3's TIP notes that always taking from one
  side gradually skews the tree, and that some implementations alternate.
  Why would always taking the predecessor skew it left?
- **The skew problem**: insert 1..n in order and give the height, the cost of
  a search, and the reason. Then: what does a balanced tree cost instead?
  Ties to 10.4 and to `ds-10-balanced`.
- **Ask about the return value**: why do `insert` and `deleteKey` return a
  node while `search` returns the node it found? What would the alternative
  be? (A parent pointer, or a wrapper holding the root.) **This is the best
  short exam question here** -- it is the pattern the whole chapter rests on
  and students copy it without seeing why.
- **Rebuild from a traversal**: given a preorder listing of a BST,
  reconstruct the tree. Possible because the BST rule supplies the missing
  information; the same listing of a plain binary tree would not be enough.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Insert and search | `dsa-11-bst` (Korean set) | Same problem. Removal is the English section's; keep insert/search questions for the Korean exam. |
| Skew and height | `ds-10-balanced` | That problem fixes the skew; this one causes it. Good as a pair, and case 13 here is a skewed tree. |
| Reconstructing from traversals | `ds-09-traversal` variants | That one uses preorder + inorder on a plain tree. Here the BST rule replaces the second traversal, which is the interesting difference. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Add an operation -- minimum, maximum, successor |
| English (ds) | Why `insert` and `deleteKey` return a node, and what the alternative would cost |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
