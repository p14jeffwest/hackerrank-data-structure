# Exam variation axes: ds-04-array-list

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean section and the English section sit on different exam schedules, so
the same problem must yield **different axes** for each. This problem has no
Korean counterpart, so every axis below is available to the English section --
but chapter 5 will ask several of the same questions about a linked list, and
that is where the real competition for axes lies.

## The core of the original problem

Implement `add(int, T)`, `remove(int)` and `indexOf(T)` for an array-based
list: make room by shifting the tail back, close the gap by pulling it
forward, and search by value.

## Variation axes

- **Add an operation**: `addAll(int i, ListInterface<T> other)` inserting a
  whole list at a position with one shift rather than one per element;
  `removeRange(int from, int to)`; `set(int i, T x)` returning the old value;
  `contains`, `lastIndexOf`, `reverse` in place.
- **Loosen a rule**: allow `add(size(), x)` as an append, which forces a
  second bounds rule distinct from `checkPosition`. This is a good exam
  question precisely because the book's `checkPosition` forbids it -- the
  student has to notice that insertion and retrieval want different bounds.
- **Change the growth policy**: grow by a fixed `+10` instead of doubling, or
  by 1.5x as OpenJDK does, and ask for the consequence. Pairs with
  `ds-04-array-growth`; do not use both on one exam.
- **Add shrinking**: halve the array when it falls below a quarter full, then
  ask why a quarter and not a half. (Halving at half full makes an alternating
  add/remove sequence copy on every single operation.)
- **Trace by hand**: give a short command sequence and a starting capacity and
  ask for the list contents, `numberOfEntries` and `list.length` after each
  step.
- **Count the work**: ask how many element moves a given sequence performs.
  Overlaps with `ds-04-array-growth`.
- **Run it backwards**: give an `add(int, T)` whose loop runs the wrong
  direction and ask what `[A, B, C]` becomes when inserting at position 0.
  The answer is not a crash, which is the whole lesson.
- **Ask about the null**: why does `remove` set the vacated slot to `null`
  when no output depends on it? No test case can check this, so an exam is the
  only place it can be assessed.
- **Ask about the cast**: why `(T[]) new Object[n]` rather than `new T[n]`,
  and what `@SuppressWarnings("unchecked")` is asserting.
- **Ask about the comparison**: why `.equals()` and not `==` in `indexOf`.
  Give the `Integer` cache boundary as the concrete case.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Growth policy, counting copies | `ds-04-array-growth` | That problem owns this axis. Keep this one on the shifting. |
| Insert and remove at a position | chapter 5 (linked list) | The interesting exam question is the comparison, not either one alone: same operation, opposite cost profile. Save it for after chapter 5. |
| `.equals()` versus `==` | chapter 14 (hash maps) | Chapter 14 needs `equals` and `hashCode` together. Keep the boxed-Integer version here and the contract version there. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Loosen the rule -- allow append via `add(size(), x)` |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
