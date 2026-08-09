# Exam variation axes: ds-04-rotate

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

This problem has no Korean counterpart, so every axis below is available to the
English section.

## The core of the original problem

Rotate a list `k` slots to the right, where `k` may be far larger than the
list. Reduce `k` with `k % n`, then read the last `k` elements followed by the
first `n - k`.

## Variation axes

- **Change the direction**: rotate left instead of right. The cheapest
  variation there is, and it defeats a memorized split point.
- **Rotate in place**: forbid the second list and require $O(1)$ extra space.
  The reverse-three-times method (reverse the whole list, then reverse each of
  the two runs) is a genuinely different idea and makes a good exam question
  on its own.
- **Change the operation, keep the shape**: print only the element that ends
  up at position 0; print where a given index lands after the rotation, which
  reduces to one modulo and no array at all; report how many elements stay
  where they were.
- **Rotate repeatedly**: give a sequence of rotations $k_1, k_2, \dots$ and
  ask for the final arrangement. The point is that the total is
  $(\sum k_i) \bmod n$ and the list need only be built once.
- **Change the constraints**: allow $k = 0$; allow negative `k` to mean a left
  rotation; raise `k` past the `int` range so it must be read as `long`. That
  last one pairs neatly with `ds-tutorial-03-sum` but should not appear on the
  same exam as it.
- **Ask for the cost**: compare rotating one slot at a time k times against
  the split method, in $O$ notation, and say what happens when $k$ is $10^9$
  and $n$ is 5.
- **Run it backwards**: give a rotated list and `k` and ask for the original.
- **Trace by hand**: give a short list and a large `k` and ask for the result
  in one step, which cannot be done without the modulo.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Shifting elements one slot at a time | `ds-04-array-list` | That problem owns the shift. Here the shift is the *wrong* answer, so the two do not compete -- but do not put both on one exam, since they teach the same motion. |
| Cost of `get(i)` | chapter 5 (linked list) | The sharpest version of this problem is asking what happens to the same `rotate` code when the list underneath becomes linked. Save it for after chapter 5. |
| Reading `k` as `long` | `ds-tutorial-03-sum` | Same overflow lesson. Keep it in the tutorial. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Rotate in place -- the reverse-three-times method, $O(1)$ extra space |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
