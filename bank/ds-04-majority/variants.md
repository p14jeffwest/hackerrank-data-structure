# Exam variation axes: ds-04-majority

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

This problem has no Korean counterpart, so every axis below is available to the
English section.

## The core of the original problem

Return the value occupying more than half the list, without rearranging the
list. Boyer-Moore voting does it in one pass with a single candidate and a
counter.

## Variation axes

- **Remove the guarantee**: the majority element may not exist, so the answer
  must be verified with a second pass. This is the best single variation --
  it is one extra loop, but only a student who understands *why* voting works
  knows that voting alone cannot detect absence.
- **Change the threshold**: find every element appearing more than $n/3$ times
  (at most two exist, and the same voting idea generalizes to two candidates);
  or more than $n/k$ for a given $k$.
- **Change what is returned**: return how many times the majority element
  occurs; return its first position; report whether a *given* value is the
  majority.
- **Change the constraints**: allow an empty list; allow negative values;
  raise `n` past what an $O(n \log n)$ sort can afford.
- **Trace by hand**: give a short list and ask for the candidate and counter
  after each element. This is the cheapest way to test whether voting is
  understood rather than memorized.
- **Run it backwards**: give a candidate-and-counter trace and ask what the
  input could have been.
- **Justify it**: explain why the survivor of the cancellation is necessarily
  the majority element, and what breaks when no majority exists.
- **Compare the approaches**: voting, sorting, and a counting table, in time
  and in extra space. Ask which becomes impossible when the list is a stream
  that can only be read once.
- **Ask about the constraint we enforced**: why should a query method not
  rearrange its argument? Ties back to 4.1, where `get` is specified as
  leaving the list unchanged.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Boxed `Integer` compared with `==` | `ds-04-array-list` | That problem owns it and catches it hard. Here it is only partly caught. |
| Counting occurrences by value | chapter 14 (hash maps) | Chapter 14 is where a counting table is the intended answer rather than the fallback. Keep frequency questions there. |
| Single-pass streaming constraint | chapter 11 (heaps) | "Top k from a stream" is the heap version of the same idea. Do not use both on one exam. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Remove the guarantee -- the majority element may not exist |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
