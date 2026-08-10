# Exam variation axes: ds-10-balanced

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

There is no Korean counterpart, so every axis below is available to the
English section.

## The core of the original problem

The middle key becomes the root and each half becomes a subtree by the same
rule. Because the input is sorted, the BST property costs nothing -- no
comparison is ever made -- and each half is within one of the other, so the
height is the minimum possible.

## Variation axes

- **Rebalance an existing tree**: given a BST, produce the balanced tree over
  the same keys. The answer is an inorder traversal into an array followed by
  this construction, and seeing that is the point. **This is the best exam
  question here**, because it joins 10.1's "inorder gives sorted order" to
  this chapter's last section.
- **Ask for the height formula**: what is the height of the tree this builds
  over `n` keys? `floor(log2(n))`. Then: how many keys does a tree of height
  `h` hold at most, and at least?
- **Change the middle**: what does `(lo + hi + 1) / 2` build instead, and is
  it still balanced? Yes -- the mirror image, same height. A good short
  question because the intuitive answer is "it breaks".
- **Build it from a linked list** instead of an array, where reaching the
  middle is not free. The $O(n \log n)$ version finds the middle each time;
  the $O(n)$ version builds bottom-up while walking the list once. Genuinely
  hard, and a fair challenge item.
- **Ask about the skew**: 10.4's problem is that ordered insertion produces a
  spine. Given the keys 1..n inserted in order, state the height and the cost
  of a search, then compare with this construction. Ties `ds-10-bst` (whose
  case 13 is exactly that spine) to this problem.
- **Count the leaves** of the constructed tree, or the number of nodes at the
  deepest level.
- **Trace by hand**: build the tree for eight keys and give its preorder. Eight
  is chosen deliberately -- it is even at every level, so the midpoint rule is
  exercised repeatedly.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Skew versus balance | `ds-10-bst` | That problem's case 13 is a spine of 4,000 nodes built by ordered insertion. This one is the fix. Pair them; do not ask twice. |
| Divide and conquer on a sorted array | `ds-08-subsets` variants | Chapter 8 owns recursion shape. Here the recursion is the easy part and the rule is the content. |
| Height in edges | `ds-09-count-leaves` | Same convention. That problem owns the edges-versus-nodes question. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Rebalance an existing BST -- inorder out, this construction back in |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
