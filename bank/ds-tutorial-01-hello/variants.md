# Exam variation axes: ds-tutorial-01-hello

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean section and the English section sit on different exam schedules, so
the same problem must yield **different axes** for each. Record axes generously.

## The core of the original problem

Send one fixed line to standard output, and in doing so learn the `Solution`
class rule and the submit-and-read-the-result cycle.

## Variation axes

This is a tutorial, so there is almost nothing here to vary as an algorithm.
Its real value on an exam is as material for **short written questions about the
environment and about I/O**. For the three tutorials (hello / echo / sum),
concept questions are a better fit than programming questions.

- **Swap the data structure**: not applicable.
- **Add or remove an operation**: grow the output to many lines and ask whether
  to repeat `println` or collect into a `StringBuilder` and print once
  (appendix C.5, item 4).
- **Change the I/O format**: ask what differs among `print` plus `"\n"`,
  `println`, and `printf("%s%n")` for the same string.
- **Change the constraints**: with tens of thousands of output lines, ask why
  repeated `System.out.println` slows down and why gathering into a
  `StringBuilder` is faster (the TIP at the end of C.5).
- **Run it backwards**: give a compiler error message and ask for the cause.
  Good candidates: the class named `Main`; a `public` class whose name does not
  match the file name; an unmappable character in a comment.
- **Trace by hand**: give code that mixes `print` and `println` and ask for the
  exact output line by line, trailing newline included.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| StringBuilder vs repeated println | `ds-tutorial-03-sum` | Do not use both on one exam. Sum is the better home for it, since its input size makes the cost real. |
| Compiler error, run it backwards | (none) | Unique to this problem. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Trace by hand: mixing `print` and `println` |
| English (ds) | Run it backwards: read the compiler error |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
