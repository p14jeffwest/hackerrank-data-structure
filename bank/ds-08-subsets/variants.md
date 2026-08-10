# Exam variation axes: ds-08-subsets

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean chapter 9 has no backtracking problem, so every axis below is
available to the English section.

## The core of the original problem

Two choices per element -- leave it out or put it in -- give $2^n$ subsets.
The recursion emits the current selection, extends it by each remaining
element in turn, and undoes the extension on the way back. That undoing is
what backtracking means.

## Variation axes

- **Change what is generated**: all subsets of exactly size `k` (combinations);
  all permutations; all subsets whose sum is a given target. The last is the
  best exam version -- it is one extra test and it introduces pruning.
- **Add pruning**: stop descending as soon as the running sum exceeds the
  target. Ask how many nodes that removes, and why the worst case is
  unchanged.
- **Allow duplicates in the input**: now `{1, 2, 2}` should yield each
  distinct subset once. The fix -- skip a value equal to the previous one at
  the same level -- is short and hard to find, which makes it a good
  challenge item.
- **Ask about the copy**: the book's answer stresses
  `result.add(new ArrayList<>(current))`. What exactly goes wrong without the
  copy, and what does the output become? The answer is $2^n$ references to one
  list, all showing whatever it held last.
- **Ask about the order**: why does walking the indices upward produce
  lexicographic order without any sorting of the results? Everything beginning
  with `a[i]` finishes before anything beginning with `a[i+1]` begins.
- **Ask for the cost**: $O(n \cdot 2^n)$, and why the $n$ factor is there.
  Then: what is the recursion **depth**? At most `n`, not $2^n$ -- the same
  confusion `ds-08-hanoi` addresses.
- **Do it without recursion**: subset `i` contains element `j` when bit `j` of
  `i` is set. Ask for that version, and for whether it produces the same
  order. It does, which is a small surprise worth setting.
- **Trace by hand**: for `{1,2,3}`, list the calls in order with their
  arguments and mark where each line of output is produced.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Backtracking | (none) | This is the only backtracking problem in the set, so the whole area is free. |
| Recursion depth versus number of calls | `ds-08-hanoi` | Same confusion, two settings. Ask it once. |
| Gathering output | `ds-tutorial-03-sum`, `ds-08-hanoi` | The tutorial owns it. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Subsets summing to a target, with pruning |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
