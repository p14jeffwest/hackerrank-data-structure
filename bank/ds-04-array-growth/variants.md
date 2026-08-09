# Exam variation axes: ds-04-array-growth

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

This problem has no Korean counterpart, so every axis below is available to the
English section.

## The core of the original problem

Report what a sequence of list operations costs: elements moved by shifting,
elements copied by growing, and the final capacity. None of it depends on the
values stored, so the answer follows from the size and the capacity alone.

## Variation axes

- **Change the growth factor**: grow by 1.5x as OpenJDK's `ArrayList` does
  (4.5 mentions this), or by a fixed `+10`. The fixed increment is the sharper
  question, because it turns appending from amortized $O(1)$ into $O(n)$ and
  the total copy count from about $2n$ into about $n^2 / 20$.
- **Add shrinking**: halve the capacity when the list falls below a quarter
  full, and ask what happens to an alternating add/remove sequence if you
  halve at *half* full instead. The answer is a copy on every operation.
- **Ask for the amortized bound**: given $n$ appends from capacity 1, prove
  the total copying is under $2n$. The geometric series in 4.3 is the answer;
  the picture there is the intuition.
- **Ask for the worst sequence**: which sequence of $Q$ operations maximizes
  total moves, and what is that maximum? ($Q-1$ insertions at position 0,
  giving about $Q^2/2$.)
- **Invert it**: given a total move count and $Q$, what sequence produced it?
  Or: how many appends does it take before capacity reaches a given value?
- **Change what is counted**: count only the growth events; count the maximum
  capacity ever reached; report the largest single operation's cost.
- **Compare the two implementations**: run the same operation sequence against
  a linked list and ask which costs more, and why the answer flips depending
  on whether the position is already held. This is the 4.3 comparison table
  turned into a question, and it is the best version of this problem -- but it
  needs chapter 5 first.
- **Ask about the type**: why does the move count need `long`? Give $Q$ and
  ask for the largest possible total.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The shift itself | `ds-04-array-list` | That problem asks the student to write the shift; this one asks what it costs. Complementary, but do not use both on one exam. |
| Overflow into `long` | `ds-tutorial-03-sum` | The tutorial owns the lesson. Here it is a trap rather than a taught idea. |
| Growth policy | `ds-04-array-list` variants | Listed there too. This problem is the better home for it; strike it from the other. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Change the growth factor -- fixed `+10` instead of doubling |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
