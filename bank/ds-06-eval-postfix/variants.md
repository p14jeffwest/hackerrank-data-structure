# Exam variation axes: ds-06-eval-postfix

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-05-eval-postfix` from the same source, so the axes must
be split.

## The core of the original problem

Evaluate a postfix expression with a stack: push operands, and on an operator
take two values off, combine, push the result back. The first value popped is
the right operand.

## Variation axes

- **Drop the validity guarantee**: detect malformed input -- an operator with
  too few operands, or more than one value left at the end -- and report it.
  One extra check each, but only a student who understands the invariant knows
  where to put them.
- **Convert instead of evaluate**: infix to postfix (the shunting-yard idea),
  or postfix back to a fully parenthesised infix string. The second is the
  gentler one and still needs a stack, of strings this time.
- **Change the operator set**: add `%`, or a right-associative `^`, and ask
  what changes in the evaluation loop. The answer for postfix is *nothing*,
  which is the point -- associativity was already resolved when the expression
  was written.
- **Add unary minus**: now `-` is ambiguous and the tokeniser has to decide.
  Connects to the negative-literal trap this problem already carries.
- **Ask about division**: what does `-7 / 2` give in Java, and what would it
  give under floor division? Where does the difference show up?
- **Trace by hand**: give an expression and ask for the stack contents after
  each token. Cheap to mark and impossible to fake.
- **Run it backwards**: give a stack trace and ask which expression produced
  it; or give a wrong answer and ask which single mistake explains it.
- **Ask about the cost**: why is this $O(n)$ when a expression tree would need
  building first? What is the maximum stack depth for an expression of $n$
  tokens, and which shape reaches it?

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Postfix evaluation | `dsa-05-eval-postfix` (Korean set) | Same source. The reserved split below keeps the exams apart. |
| Balanced brackets | `dsa-05-valid-parentheses` (Korean set) | The other half of 6.2. Not a contest problem in the English set, so the whole bracket family is available here as exam material. |
| Integer division and sign | `ds-05-iterator-scan` | That problem carries the negative-remainder version of the same Java surprise. Do not use both on one exam. |
| Maximum stack depth | `ds-06-array-stack` | That one owns capacity and growth. Keep the depth question here. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Convert infix to postfix |
| English (ds) | Drop the validity guarantee -- detect a malformed expression |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
