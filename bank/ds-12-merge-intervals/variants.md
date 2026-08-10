# Exam variation axes: ds-12-merge-intervals

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

There is no Korean counterpart, but there is a near neighbour in this set --
`ds-11-meeting-rooms` -- with the opposite boundary rule. The split below has
to keep those apart as well.

## The core of the original problem

Sorting by start is the whole method. Once the intervals are in that order,
everything overlapping a given interval is adjacent to it, so a group can be
closed at the first gap and one pass suffices. The book calls this the
representative example of sorting as preprocessing.

## Variation axes

- **Insert one interval into a merged list**: the list is already merged and
  sorted; add `[s, e]` and re-merge. Doable in $O(n)$ with no sort, and seeing
  why is the point.
- **Ask for the gaps instead**: the intervals *not* covered, within a given
  range. Same pass, complementary output.
- **Ask for the total length covered**: the sum of the merged lengths. Same
  pass, one accumulator, and it needs `long`.
- **Change the boundary rule**: make touching intervals stay separate, which
  is `ds-11-meeting-rooms`'s rule. Ask which comparison changes and give an
  input where the two answers differ. **This is the best exam question here**,
  because it forces the two problems to be told apart rather than
  pattern-matched.
- **Ask why sorting by start and not by end**: sorting by end also works for
  some interval problems and not this one. What breaks?
- **Remove an interval**: given a merged list, subtract `[s, e]` from it. One
  merged interval can split into two, which surprises people.
- **Ask for the cost**: why is the pass $O(n)$ when the group's end keeps
  changing? Because each interval is looked at once and never revisited.
- **Trace by hand**: five shuffled intervals, list the merged groups after
  each step of the pass.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Intervals with a boundary rule | `ds-11-meeting-rooms` | **The rules are opposite**, deliberately, and both are the book's. Setting both on one exam without pointing that out would be a trap rather than a test. If both appear, the boundary difference must be the explicit subject. |
| Sorting as preprocessing | `ds-11-meeting-rooms`, `ds-12-sort-records` | 12.8 names this problem as the representative example. Keep the general question here. |
| Sweeping endpoints | `ds-11-meeting-rooms` | That problem's model uses a sweep; this one does not need it. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Change the boundary rule -- which comparison, and where the answers diverge |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
