# Exam variation axes: ds-tutorial-02-echo

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean section and the English section sit on different exam schedules, so
the same problem must yield **different axes** for each.

## The core of the original problem

Read one **whole line** from standard input and print it back unchanged.

The real target is the gap between `next()`, which works in tokens, and
`nextLine()`, which works in lines. The test set is arranged so that the
mistake produces a partial score rather than a zero.

## Variation axes

A tutorial, so it serves better as material for **written questions** than as a
programming question.

- **Change the I/O format**: read several lines and print them in reverse
  order; print each line with its line number attached; print only the last
  line.
- **Add an operation**: uppercase the line before printing; count the words and
  print the count; reverse the word order (connects to `StringTokenizer` and
  `split`).
- **Run it backwards**: give code and an input, ask for the exact output.
  A `next()` solution fed a line containing spaces is the obvious candidate.
- **The leftover-newline trap (appendix C.5, item 2 TIP)**: give code that
  calls `nextLine()` immediately after `nextInt()` and ask what it prints. The
  leftover newline is consumed first as an empty line.
- **Justify the performance claim (appendix C.5, item 4)**: with 100,000 lines
  of input, ask why `BufferedReader` replaces `Scanner`.
- **Find the compile error**: give code that uses `BufferedReader.readLine()`
  but omits `throws IOException`, and ask for the cause.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Justify BufferedReader over Scanner | `ds-tutorial-03-sum` | Sum is the better home for it, since its input size makes the cost real. Do not use both on one exam. |
| Run it backwards, read an error message | `ds-tutorial-01-hello` | Hello uses a compile error, this one uses a wrong-output trace. Different enough to coexist. |
| The leftover-newline trap | (none) | Unique to this problem, and the sharpest written question of the three tutorials. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Add an operation -- reverse the word order |
| English (ds) | The leftover-newline trap after `nextInt()` |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
