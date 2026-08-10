# ds-06-eval-postfix: upload checklist

Contest: `Data Structure`
URL: not yet published

## 1. Create the challenge

At `hackerrank.com/administration/challenges/create`, paste the files in
numeric order.

| Form field | File |
|---|---|
| Challenge name | `00. challenge-name.txt` |
| Description | `01. description.txt` |
| Problem Statement | `02. statement.md` |
| Input Format | `03. input-format.md` |
| Constraints | `04. constraints.md` |
| Output format | `05. output-format.md` |
| Tags | `06. tags.txt` |

No code stub. The default Java template is what students should see.

## 2. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 01 is six expressions in three pairs, each pair being the same two
numbers in the other order, so a solution that pops its operands backwards
prints `-2` where `2` belongs. Case 02 puts negative literals next to the
minus operator.

`testcases/SAMPLES` lists the case numbers to mark.

## 3. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 4. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 5. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-06-eval-postfix`
- [ ] **Max Score = 30**
- [ ] Place it second among the chapter 6 problems

## 6. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 7. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 30/30
- [ ] Confirm the LaTeX in Constraints renders

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| Right operand popped first (registered) | 14/14 | -- |
| Operands popped the wrong way round | 3/14 | passes 03 05 11, the cases with no `-` or `/` |
| Operator detected by first character only | 3/14 | reads `-11` as an operator |
| `Math.floorDiv` instead of Java's `/` | 9/14 | fails 00 04 08 09 10 |

Reference timing: 178 to 251 ms on the four largest cases.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed.

**The reference model implements Java's division, not Python's.** Java
truncates toward zero and Python floors, so `-7 / 2` is `-3` in one and `-4`
in the other. Writing the model the natural Python way would have produced
expected output that agrees with a correct Java solution only when the two
operands share a sign -- and it would have marked `Math.floorDiv` correct.
`idiv()` in `gen.py` exists for this reason.

**Two rounds were needed to get the operator-restricted cases right**, and the
reason is worth recording.

Cases 05, 11 and 12 exist so that a solution popping its operands backwards
scores partially rather than zero: with only `+` and `*` present, the order
does not matter and those cases pass. The first generator built them with the
general `build()`, whose fallback -- reached when no operator keeps the result
inside the limit -- emitted `-` regardless of which operators the case was
supposed to allow. Subtraction leaked into the `+*` cases and the reversed
solution scored 1/14 instead of a partial score.

Fixing the fallback to stay inside the allowed set was not enough: with only
`+` and `*`, both candidates can exceed the limit at once, and the
smallest-magnitude fallback then pushes a value above the working threshold,
which the next combine turns into a genuine overflow. Case 11 asserted its way
out.

The operator-restricted cases are now built by `build_chain()`, which nests to
the left so that one operand of every step is a fresh literal of at most 1000.
A literal of the opposite sign always brings the running value back down, so a
safe operator always exists. The cost is that those cases keep the stack only
two deep; stack depth is covered by cases 09, 10 and 13 instead.

`gen.py` asserts, for every generated expression, that no intermediate result
exceeds $10^9$ and that exactly one value remains at the end.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
