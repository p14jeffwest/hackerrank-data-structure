# Exam variation axes: ds-tutorial-03-sum

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean section and the English section sit on different exam schedules, so
the same problem must yield **different axes** for each.

## The core of the original problem

Read `N`, read `N` integers, print the sum.

Two lessons ride along with it. Reading many values in sequence, and noticing
that the accumulator needs a wider type than the values it accumulates. The
test set is arranged so the type mistake produces a partial score.

## Variation axes

The first of the three tutorials that can carry a real programming question,
because the input is large enough for complexity and type to matter.

- **Change the operation, keep the shape**: print the average to two decimal
  places (`printf("%.2f%n")`, appendix C.5 item 3); print the maximum and
  minimum; print the sum of the positive values only; print the count of
  values above the average, which forces two passes.
- **Change the I/O format**: drop `N` and read to end of input; put all values
  on one line; spread one value per line; print the running total after each
  value, which makes output size the bottleneck and pulls in `StringBuilder`.
- **Change the constraints**: raise `N` to one million so `Scanner` genuinely
  times out and `BufferedReader` becomes mandatory; widen each value so even
  `long` needs thought.
- **Ask for the type analysis directly**: give `N` and a value bound and ask
  for the largest possible sum and the narrowest type that holds it. This is
  the axis with the best ratio of marks to writing time.
- **Run it backwards**: give a program that accumulates into `int`, give an
  input, and ask for the exact printed output. Case 02 of this problem is a
  ready-made instance -- three values of 1,000,000,000 print -1294967296.
- **Find the bug**: give a working-looking program that reads into `long` but
  accumulates into `int`, or that declares `long sum` yet computes
  `int a * int b` on the right-hand side, and ask why large inputs fail.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Justify BufferedReader over Scanner | `ds-tutorial-02-echo` | Keep it here. Only this problem has input large enough to make the cost real. |
| Gather output with StringBuilder | `ds-tutorial-01-hello` | Same. The running-total variant gives it a reason to exist; hello can only ask it in the abstract. |
| Overflow and type width | (none yet) | Watch chapter 12 and 13 sorting problems, where sums of key values may raise it again. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Change the operation -- average to two decimal places |
| English (ds) | Run it backwards -- predict the output of the `int` version |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
