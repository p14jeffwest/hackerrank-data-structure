# Exam variation axes: ds-06-array-stack

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-05-array-stack`, the same three methods on the same
kind of stack, so the axes must be split.

## The core of the original problem

Implement `push`, `pop` and `peek` on an array-based stack where `top` is an
index and `-1` means empty. Grow the array when it fills, and report underflow
rather than reading past the end of it.

## Variation axes

- **Change the implementation**: write the same three methods for the linked
  stack of 6.3, and ask which operations change complexity (none) and what
  does change (memory per element, and the absence of a capacity limit).
- **Add an operation**: `size` without a counter; `clear` that is $O(1)$
  rather than $O(n)$, and what that costs; a `min()` that reports the smallest
  element currently on the stack in $O(1)$, which needs a second stack and is
  the best programming variation this problem supports.
- **Change the underflow policy**: return `null` instead of throwing, as 6.1
  offers, and ask what the caller now has to do and what can go wrong if they
  forget.
- **Change the growth policy**: grow by a fixed amount instead of doubling.
  Overlaps with `ds-04-array-growth`, which owns that axis.
- **Trace by hand**: give a command sequence and ask for `top`, `item.length`
  and the contents after each step. The interesting steps are the expansions.
- **Run it backwards**: give `item[top++] = newEntry` and ask what happens on
  the first push. The answer is an exception at index -1, which is worth
  reaching by reasoning rather than by running it.
- **Ask about the null**: why does `pop` clear the slot when no caller can
  observe the difference, and why is `clear` therefore $O(n)$ rather than a
  single assignment? No test can check this, so an exam is the only place.
- **Ask about the guard**: what is `MAX_CAPACITY` protecting against, and what
  would happen without it?
- **Stack from two queues**: the mirror of `ds-06-queue-two-stacks`. Save it
  for after that problem.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The three methods | `dsa-05-array-stack` (Korean set) | Same problem. The reserved split below keeps the exams apart. |
| Doubling on expansion | `ds-04-array-growth`, `ds-04-array-list` | Chapter 4 owns growth policy and amortized analysis. Keep this one on the stack discipline. |
| Clearing a slot for the GC | `ds-04-array-list` | Same untestable point, raised twice. Use it once. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Change the underflow policy -- return `null` instead of throwing |
| English (ds) | Add `min()` in $O(1)$ using a second stack |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
