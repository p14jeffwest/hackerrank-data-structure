# ds-04-array-list: upload checklist

Contest: `Data Structure`
URL: not yet published

This is the first problem in the English set that uses a **custom code stub**,
so the stub steps below are new relative to the three tutorials.

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

## 2. Code stub

Open the Java language box and switch it from the default template to a custom
stub. Three fields:

| Stub field | File |
|---|---|
| Head (locked, above) | `07. stub-head.java` |
| Body (editable) | `08. stub-body.java` |
| Tail (locked, below) | `09. stub-tail.java` |

- [ ] Paste all three
- [ ] Compare the rendered editor against `stub-preview.java`, which is the
      three files concatenated in order -- that file is what a student sees

`stub-preview.java` is for checking only; it is not pasted anywhere.

**Head and Tail are not actually locked.** HackerRank presents them as fixed
regions, but a student can edit them. That is accepted: the exam questions are
variations of these problems, so anyone who edits the driver to force a pass
only loses the practice. The statement and constraints ask students to leave
those regions alone, and that is as far as the enforcement goes.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 is the one that must be public. It holds the values 126, 127, 128, 129
and 1000, and an `indexOf` written with `==` answers the first two correctly
and then returns `-1` for the rest. Hide it and the student meets that only as
an unexplained partial score.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

Note that `Solution.java` is the full program (Head + a filled-in Body +
Tail), not just the three methods.

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-04-array-list`
- [ ] **Max Score = 10**
- [ ] Place it first among the chapter 4 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] **Submit the stub untouched.** It compiles and scores 0/14. Confirm that
      it does not error out -- a student's first Compile and Test should show
      wrong answers, not a stack trace
- [ ] Confirm the LaTeX in Constraints renders
- [ ] Confirm the command table in Input Format renders as a table

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings, including on the unchecked cast, which is covered by
`@SuppressWarnings` in the Head.

| Submission | Result | Fails on |
|---|---|---|
| Reference implementation | 14/14 | -- |
| `add(int,T)` shifting front-to-back | 6/14 | 00 04 06 08 09 10 11 12 |
| `indexOf` using `==` | 9/14 | 02 09 11 12 13 |
| `checkPosition` omitted | 11/14 | 00 01 07 |
| `remove(int)` without `numberOfEntries--` | 3/14 | 00 01 02 03 05 06 08 09 10 11 12 |
| Unmodified stub | 0/14 | all |

Every mistake lands on a different set of cases, so the score itself points at
which method is wrong.

Timing on the four largest cases (Q = 20,000): 180 to 303 ms. The worst is
case 12, which is front-heavy insertion, so nearly every command shifts the
whole tail. Total test data is 1.4 MB.

**What no test can catch.** Dropping `list[numberOfEntries - 1] = null` from
`remove` changes no output, because `toString` only reads as far as
`numberOfEntries`. It is a garbage-collection concern, not a correctness one.
If it matters to you, it has to be an exam question or a code-reading exercise;
`variants.md` records it as an axis.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed, so the output is identical
every time. `gen.py` carries a Python model of the driver that produces the
expected output, so the model and the Java Tail must be kept in step -- if you
change one, change the other.

One trap in generating data for this problem is worth recording. An early
version chose `indexOf` arguments at random over the full value range. With
values up to $10^9$ the query almost never hits, `indexOf` returns `-1` either
way, and the `==` mistake scored 13/14. The generator now aims 80% of its
queries at values it actually inserted.
