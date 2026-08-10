# Exam variation axes: ds-13-largest-number

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

There is no Korean counterpart, so every axis below is available to the
English section.

## The core of the original problem

The order is not a property of the values but of how two of them look written
side by side. Section 13.6's point exactly: the problem is deciding **what to
sort by**, and once that is right the sorting is ordinary.

## Variation axes

- **Ask for the smallest number instead**: flip the comparison. Then the
  leading-zero question becomes real -- `[0, 1]` gives `"01"`, which is not a
  number. A better exam question than the largest version because the edge
  case bites.
- **Ask why the comparison is a valid order**: a sort needs transitivity, and
  an arbitrary "looks bigger" rule need not have it. Show that this one does,
  or at least say why the question has to be asked. **This is the best exam
  question here** -- Java throws
  `IllegalArgumentException: Comparison method violates its general contract`
  when a comparator contradicts itself, and knowing that is worth more than
  the problem itself.
- **Ask about the string lengths**: why is comparing `a+b` with `b+a` as text
  the same as comparing them as numbers? Because the two have equal length, so
  no width or leading-zero question arises. One sentence, and it is the reason
  the trick works at all.
- **Give the counterexample**: show that sorting by value fails, with the
  smallest input you can. Two numbers suffice -- `3` and `30`.
- **Concatenate with a separator**: join with `-` and ask what changes.
  Nothing, which is a useful non-change to notice.
- **Change the objective**: the largest number using at most `k` of them; the
  largest number after deleting `k` digits. The second is a different problem
  entirely (a monotonic stack) and belongs to a later course.
- **Trace by hand**: order `[8, 89, 9]` and explain each comparison.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Writing a comparator | `ds-12-sort-records`, `ds-11-meeting-rooms` | Those sort on a field. This one sorts on something computed from two elements at once, which is the step up. |
| Stability | `ds-12-sort-records` | Nothing here depends on it -- equal concatenations mean identical strings. Worth saying when the contrast is useful. |
| Sorting as preprocessing | `ds-12-merge-intervals` | That problem owns the general question. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Why the comparison is a valid total order, and what Java does when one is not |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
