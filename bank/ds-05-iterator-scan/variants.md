# Exam variation axes: ds-05-iterator-scan

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean book has no `ListIterator` section, so this problem has no
counterpart and every axis below is available to the English section.

## The core of the original problem

Rewrite a linked list in one pass using a cursor. The same task written
against positions is $O(n^2)$, because every `get(i)`, `add(i, x)` and
`set(i, x)` starts over from `head`.

## Variation axes

- **Change the edit**: delete every even value instead (needs `remove`, which
  this cut-down cursor does not have -- ask what it would take to add);
  insert the running sum after each element; duplicate every negative value;
  replace each element with the sum of itself and its neighbour.
- **Insert before rather than after**: a forward-only cursor cannot, because
  the value is only known once the cursor has stepped past it. Ask what has to
  change -- either a one-element lookahead, or a doubly linked list with
  `previous()`. This is a good question precisely because the book's TIP says
  "before" and the interface makes it awkward.
- **Ask for the cost**: write out the total number of link hops for the
  index-based version on a list of length $n$, and compare it with the cursor
  version. The answer is $1 + 2 + \cdots + n$ against $n$.
- **Ask why the array is different**: the same index-based loop on an
  array-based list is $O(n)$. Why? This is 5.4's table in one question, and it
  pairs with `ds-04-array-list`.
- **Ask about the interface**: what does "the collection drives the
  navigation" buy? Give a method written against `ListInterface` and ask how
  its cost changes when the implementation is swapped underneath.
- **Trace by hand**: give a short list and ask for the cursor position and the
  list contents after each `next()`, `add()` and `set()`.
- **The negative remainder**: give `x % 2 == 1` and ask which inputs it gets
  wrong and why. Worth asking on its own -- it is a Java fact, not a data
  structures fact, and it costs students marks in every course.
- **Concurrent modification**: 5.4 ends by noting that calling the
  collection's own `remove()` inside a for-each throws
  `ConcurrentModificationException`. Ask why the iterator's own `remove()` is
  safe when the collection's is not.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Cost of walking from `head` | `ds-05-linked-list` | That problem pays the cost; this one makes avoiding it the whole task. This problem owns the complexity question. |
| Array versus linked traversal | `ds-04-array-list` | The comparison question needs both problems, and is the strongest exam item either one supports. |
| Inserting into a linked list | `ds-05-linked-list`, `ds-05-merge-sorted` | All three relink. Only this one does it from a cursor. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Insert *before* rather than after -- what the cursor would need |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
