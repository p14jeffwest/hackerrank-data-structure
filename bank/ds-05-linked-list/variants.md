# Exam variation axes: ds-05-linked-list

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean section has a counterpart here, `dsa-07-linked-list`, so the axes
must be split. The Korean version asks for `addFront`, `addBack` and
`remove(value)`; this one asks for `add(int, T)`, `remove(int)` and `indexOf`.
The overlap is real and the reserved axes below keep the two exams apart.

## The core of the original problem

Implement insertion at a position, removal at a position, and search on a
singly linked list that keeps both `head` and `tail`. Insertion and removal
are link changes; reaching the position is the part that costs.

## Variation axes

- **Add an operation**: `addLast` without a `tail` reference, and ask what it
  costs; `removeLast`, which is $O(n)$ on a singly linked list and is exactly
  the operation 5.3 uses to justify the doubly linked list; `set(int, T)`;
  `reverse` in place; `lastIndexOf`.
- **Take away `tail`**: which operations change complexity, and by how much?
  This is the cheapest good exam question in the chapter.
- **Change the structure**: make it doubly linked and ask which operations
  improve (only `removeBack`); make it circular and ask what breaks in
  `toString` (there is no `null` to stop at).
- **Compare the two implementations**: give the same command sequence and ask
  which of the array-based and linked lists is faster, and why the answer
  flips depending on where the operations happen. **This is the best exam
  question this problem supports**, and it is only available because
  `ds-04-array-list` asks for the same three methods.
- **Justify the bound difference**: why can a linked list accept
  `add(size(), x)` cheaply when the array-based list's `checkPosition`
  refuses it? Ties directly to the asymmetry the statement points out.
- **Run it backwards**: give an `add(int, T)` with the two splice lines
  swapped and ask what the list becomes. The answer is a one-node cycle, not
  a crash, which is why it hangs rather than throwing.
- **Trace by hand**: give a command sequence and ask for the state of `head`,
  `tail` and `numberOfEntries` after each step. The interesting steps are the
  ones that empty the list or leave one node.
- **Find the bug**: give a `remove(int)` that omits the `tail` update and ask
  why the list looks right until the next append.
- **Ask about the cost of traversal**: why is a `for` loop over `get(i)`
  $O(n^2)$ here and $O(n)$ on the array-based list? Overlaps with
  `ds-05-iterator-scan`, which owns that axis.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The three methods themselves | `ds-04-array-list` | Same methods, opposite cost profile. That contrast is the point; do not spend it on a question about either one alone. |
| `.equals()` versus `==` | `ds-04-array-list`, chapter 14 | Caught here too, but chapter 4 owns the boxed-Integer version and chapter 14 owns the `equals`/`hashCode` contract. |
| Traversal cost, `get(i)` in a loop | `ds-05-iterator-scan` | That problem owns it and enforces it by timing. |
| Removing the last node | 5.3, chapter 7 (deque) | The doubly linked list exists because of this operation. Save the full question for chapter 7. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Take away `tail` -- which operations change complexity |
| English (ds) | Compare the two implementations on one command sequence |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
