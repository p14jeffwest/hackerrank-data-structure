# Exam variation axes: ds-07-process-priority

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-06-print-order`, deliberately the same problem, so the
axes must be split.

## The core of the original problem

Simulate the scheduler: take the front, send it back if anything better is
waiting, otherwise run it. Report where the tracked process lands in the run
order.

## Variation axes

- **Change what is asked**: return the full run order rather than one
  position; return which process runs last; return how many times the tracked
  process is sent to the rear.
- **Change the rule**: equal priorities *do* displace each other, and ask what
  goes wrong. The answer -- the queue never empties -- is a better question
  than it looks, because students expect a wrong answer rather than a hang.
- **Change the tie-break**: among equal priorities, run the one that has
  waited longest, or the one with the smallest original index. The first is
  what the queue already does; noticing that is the point.
- **Ask for the cost**: how many polls does the simulation perform in the
  worst case, and which input achieves it? The answer is $N(N+1)/2$ with
  priorities $1, 2, \dots, N$, and it does not depend on how the
  higher-priority test is implemented. **This is the best exam question here**
  -- see the note below on why it is also the only one the contest version
  could not enforce.
- **Remove the queue**: solve it without simulating, by sorting. A process
  runs after every process of strictly higher priority, and after those of
  equal priority that were ahead of it in the queue at the time. Getting the
  tie-break right without simulating is genuinely harder than it sounds.
- **Trace by hand**: six processes, list the queue after each step. Cheap and
  exact.
- **Add pre-emption**: a new process may arrive mid-run with a given priority.
  Ties to chapter 11, where a priority queue is the right structure.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The simulation itself | `dsa-06-print-order` (Korean set) | Same problem by design. The reserved split below keeps the exams apart. |
| Strict versus non-strict comparison | `ds-06-daily-temperatures` | Both punish `>=`. Different consequence though: there a wrong answer, here a hang. Safe to use both, but say so. |
| Priority scheduling | chapter 11 (heaps) | Chapter 11 owns priority queues. Keep this one as a queue simulation. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Change what is asked -- return the full run order |
| English (ds) | The worst-case poll count, and which input achieves it |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
