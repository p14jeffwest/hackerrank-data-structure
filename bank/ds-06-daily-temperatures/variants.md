# Exam variation axes: ds-06-daily-temperatures

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has two problems of this family, `dsa-05-next-greater` and
`dsa-05-laser-tower`, so the axes have to be split with care -- more than for
any other problem in chapter 6.

## The core of the original problem

For each day, how many days until a warmer one. A stack holds the indices of
days still waiting, with temperatures decreasing from the bottom up; a warmer
day settles everything it beats. Each index is pushed once and popped once, so
the pass is $O(n)$ despite the inner loop.

## Variation axes

- **Return the value instead of the distance**: the next strictly greater
  element itself. **Reserved for the Korean section**, which already has this
  as `dsa-05-next-greater`.
- **Look the other way**: the previous warmer day, or the distance back to it.
  The same stack, walked from the right, and the cheapest good variation.
- **Change the comparison**: the next day that is warmer *or equal*, which
  turns `>` into `>=` and is exactly the mistake this problem catches. Asking
  it deliberately is a fair question once it has been met accidentally.
- **Change what is counted**: how many days are visible from each day looking
  forward until the view is blocked (the "laser tower" shape, **reserved for
  the Korean section**); the largest rectangle in a histogram, which is the
  same stack with a harder invariant and is a genuine step up in difficulty.
- **Ask for the cost argument**: the inner `while` can run many times in one
  iteration, so why is the whole pass $O(n)$? The answer -- each index enters
  and leaves the stack once -- is the only thing worth testing here, and it is
  an amortized argument, so it pairs with 4.3.
- **Ask for the maximum stack depth**: which input fills it to $n$? All equal
  readings, because nothing ever pops.
- **Trace by hand**: give eight temperatures and ask for the stack contents
  after each day. Marks quickly and cannot be guessed.
- **Run it backwards**: give an answer array and ask for a temperature
  sequence that produces it, or show that none does.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Next greater element | `dsa-05-next-greater` (Korean set) | Reserved for the Korean exams. Keep the distance version here. |
| Visibility / blocking | `dsa-05-laser-tower` (Korean set) | Reserved for the Korean exams. |
| Amortized "pushed once, popped once" | `ds-04-array-growth` | That problem owns amortized analysis in general; this is the cleanest stack instance of it. Do not use both on one exam. |
| Strict versus non-strict comparison | `ds-06-eval-postfix` variants | Different flavour there. Safe to use both. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Next greater **value**, and the visibility/blocking shape |
| English (ds) | Look backwards -- the previous warmer day |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
