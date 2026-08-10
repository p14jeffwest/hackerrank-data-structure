# Exam variation axes: ds-07-circular-queue

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-06-circular-queue`, deliberately the same problem, so
the axes must be split.

## The core of the original problem

Implement `enqueue`, `dequeue` and `getFront` on a fixed-capacity circular
queue where `rear = (front + count) % capacity`. Every operation is $O(1)$
because nothing is ever shifted.

## Variation axes

- **Drop `count`**: keep `front` and `rear` as indices instead. Now empty and
  full look identical, and the usual fix is to leave one slot unused. Ask for
  the capacity that a `capacity`-sized array then provides, and how `isFull`
  is written. **This is the best exam question this problem supports** --
  7.3 raises the empty-versus-full ambiguity and then sidesteps it.
- **Make it grow**: double the array when full. The elements are not laid out
  from index 0, so a plain `Arrays.copyOf` scrambles the order. Asking what
  copying has to do instead is a sharp question.
- **Add an operation**: `getRear()`; `enqueue` at the front and `dequeue` from
  the rear, which turns the queue into the deque of 7.4; `contains(x)`.
- **Change the boundary policy**: make the empty case throw and the full case
  return a flag, the reverse of this class, and ask which is easier to use
  correctly from the caller's side. Ties back to 6.1.
- **Trace by hand**: give a capacity and a command sequence and ask for
  `front`, `count`, the computed rear, and the array contents after each step.
  The interesting steps are the ones that wrap.
- **Compute the rear**: 7.5 Problem 2 in one line -- given `capacity`, `front`
  and `count`, where does the next element go? Cheap and exact.
- **Run it backwards**: given the array contents, `front` and `count`, write
  out the queue in order. Students who think of the array as the queue get
  this wrong.
- **Ask about `clear`**: why is it $O(n)$ when `front = count = 0` would look
  like enough?

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The three methods | `dsa-06-circular-queue` (Korean set) | Same problem by design. The reserved split below keeps the exams apart. |
| Clearing slots for the GC | `ds-04-array-list`, `ds-06-array-stack` | Third appearance of the same untestable point. It has been reserved for chapter 4; do not spend it again here. |
| Growing an array | `ds-04-array-growth` | Chapter 4 owns growth. The circular twist -- that copying must unwrap the ring -- is new and belongs here. |
| Deque operations | `ds-07-sliding-window-max` | That problem uses a deque; this one can ask how to build one. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Change the boundary policy -- which report is easier to use |
| English (ds) | Drop `count` -- distinguish empty from full without it |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
