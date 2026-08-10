# Exam variation axes: ds-09-traversal

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-10-traversal`, the same problem with three traversals
instead of four, so the axes must be split.

## The core of the original problem

Three recursive traversals that differ in one line, plus a level-order
traversal that cannot be written that way at all and needs a queue.

## Variation axes

- **Give two traversals, ask for the tree**: preorder plus inorder determines
  a binary tree uniquely; preorder plus postorder does not. **This is the best
  exam question this problem supports** -- it is short to state, impossible to
  guess, and the "does not" half is the interesting one.
- **Ask which traversal to use**: printing a directory tree, deleting a tree,
  reading a binary search tree in sorted order, finding the nearest node.
  Section 9.3 item 3 answers all four, so this can be set from material
  students have read.
- **Write one iteratively**: preorder with an explicit stack, and then
  inorder, which is much harder. Ties back to 8.3, where recursion is
  converted using a stack.
- **Ask about the space**: why does recursive DFS use space proportional to
  the **height** and level-order to the **width**? Which tree shape is worst
  for each? A skewed tree for DFS, a complete tree for BFS -- and the two are
  opposites, which is the point.
- **Reverse level order**: bottom level first. One extra step at the end, and
  it checks that level order is understood rather than copied.
- **Zigzag level order**: alternate the direction at each level.
- **Trace by hand**: give a small tree and ask for all four; or give the four
  results and ask which tree produced them.
- **Ask about `#`**: why does the input format not list the children of a
  missing node, and what would change if it did? A question about the format
  rather than the algorithm, but it catches students who never read the
  parser.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The three DFS traversals | `dsa-10-traversal` (Korean set) | Same problem by design. The reserved split below keeps the exams apart. |
| Level-order traversal | `ds-09-right-view` | That problem needs level order **with the levels separated**, which this one does not. Do not spend the level-order question here. |
| Recursion depth versus tree shape | `ds-09-diameter`, `ds-08-hanoi` | Chapter 8 owns recursion depth in general; here it is specifically about tree shape. |
| Queue used for BFS | chapter 7 | Chapter 7 owns queues. This is where the payoff shows. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Which traversal for which task (9.3 item 3) |
| English (ds) | Reconstruct the tree from preorder + inorder, and why preorder + postorder is not enough |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
