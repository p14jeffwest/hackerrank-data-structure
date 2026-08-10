# Exam variation axes: ds-11-meeting-rooms

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has a problem of the same name that asks a different question,
so there is a real risk of the two exams colliding by accident. The split
below matters more than usual.

## The core of the original problem

Sort by start time; keep the end times of the rooms in use in a min-heap. The
root is the room that frees up soonest, and the heap grows only when even that
room is still busy.

## Variation axes

- **The Korean question**: the largest number of meetings one room can hold.
  Greedy by end time, no heap. **Reserved for the Korean section**, which has
  it as `dsa-13-meeting-rooms`.
- **Report which room**: assign each meeting a room number and print the
  assignment. The heap then has to carry room identities, not just end times.
- **Report the busiest moment**: the time at which the most meetings overlap,
  not just how many.
- **Change the rule at the boundary**: a room needs cleaning, so a meeting can
  only follow another after a gap of `g`. One `+ g` in the comparison, and it
  makes the `<=` question concrete.
- **Ask about the two comparisons**: what changes if the reuse test is `<`
  instead of `<=`? The answer is one extra room for every pair of meetings
  that meet end to end, which is exactly what sample 02 shows.
- **Solve it without a heap**: sort the start times and the end times
  separately and sweep with two pointers. Same complexity, no heap at all.
  Ask what the heap was buying -- the answer is "nothing here, but the
  identity of the room if you needed it", which is a good discussion.
- **Ask for the cost**: why $O(n \log n)$ and not $O(n^2)$? What dominates,
  the sort or the heap?
- **Trace by hand**: five meetings, list the heap contents after each step.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Meetings in one room, greedy | `dsa-13-meeting-rooms` (Korean set) | **Reserved for the Korean exams.** Setting these two side by side on one exam would be confusing rather than instructive. |
| Using `PriorityQueue` | `ds-11-merge-k`, `ds-11-median-stream` | Three application problems share the tool. Vary the question, not the structure. |
| Sorting by a key | chapter 12, chapter 13 | Those chapters own sorting itself. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | The one-room greedy version, and anything sorted by end time |
| English (ds) | Solve it with two sorted arrays and no heap -- what was the heap for? |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
