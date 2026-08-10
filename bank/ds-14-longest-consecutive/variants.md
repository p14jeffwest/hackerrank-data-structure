# Exam variation axes: ds-14-longest-consecutive

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

There is no Korean counterpart, so every axis below is available to the
English section.

## The core of the original problem

A hash set turns "is this value present?" into a constant-time question, which
is what replaces sorting. The second idea is the one that makes it linear:
extend a run only from its smallest member, so each run is walked once rather
than once per member.

## Variation axes

- **Ask why it is $O(n)$**: the inner loop can run a long way, so where does
  the linear bound come from? Because a run is only entered from its start, so
  across the whole pass the inner loop advances at most `n` times in total.
  **This is the best exam question here** -- it is the same amortized
  accounting as `ds-06-daily-temperatures`, in a different disguise.
- **Remove the start check**: what does the cost become, and on which input?
  $O(n^2)$, on one long run. Give the numbers -- 197 ms against 15.7 seconds
  on 100,000 values -- and ask for the reason.
- **Report the run, not its length**: its first and last value, or the values
  themselves.
- **Allow a gap**: the longest run allowing one missing value. The same walk
  with one unit of slack, and it is much harder than it sounds.
- **Compare with sorting**: sorting answers the same question in
  $O(n \log n)$. Which is faster in practice here, and why is the answer not
  the one the complexity suggests? Boxing. See the note in `UPLOAD.md`.
- **Ask about the set**: what does `HashSet` give beyond membership? Removal
  of duplicates, which the problem needs anyway.
- **Change the relation**: the longest run of values in arithmetic progression
  with a given step; the longest run of even numbers.
- **Trace by hand**: `100 4 200 1 3 2` -- which values pass the start check,
  and how far does each walk go?

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Amortized accounting for a nested loop | `ds-06-daily-temperatures`, `ds-07-sliding-window-max` | Three problems rest on it. Chapter 6 owns the monotonic-stack version; ask it once. |
| Hash membership replacing a search | `ds-14-word-count` | That problem owns counting; this one owns membership. |
| A requirement the clock cannot enforce | `ds-13-counting-sort`, `ds-13-merge-two` | Three cases now. Worth one honest discussion about what a grader can and cannot check. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Why the pass is $O(n)$ despite the inner loop |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
