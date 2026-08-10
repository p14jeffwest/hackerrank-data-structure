# ds-05-iterator-scan: upload checklist

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

## 2. Code stub

| Stub field | File |
|---|---|
| Head (above) | `07. stub-head.java` |
| Body (editable) | `08. stub-body.java` |
| Tail (below) | `09. stub-tail.java` |

- [ ] Paste all three
- [ ] Compare the rendered editor against `stub-preview.java`

The Head is the longest of any problem so far, and every part of it is load
bearing. It offers **both** routes through the list -- index-based `get`,
`add(int, T)` and `set(int, T)`, and a cursor -- because choosing between them
is the whole problem. Remove the index methods and there is nothing to get
wrong; remove the cursor and the problem cannot be solved.

`ListCursor<T>` is our own interface, not `java.util.ListIterator`. It carries
the three capabilities 5.4 emphasises that this task needs and leaves out
backward traversal, which a singly linked list cannot do cheaply anyway.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 01 is the one that must be public. It is all negative odd values, and a
solution testing oddness with `x % 2 == 1` gets every one of them wrong.

**The input contains blank lines** for lists of length 0. Confirm after upload
that they survived; stripped blank lines would shift every subsequent test
case.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-05-iterator-scan`
- [ ] **Max Score = 30**
- [ ] Place it fourth among the chapter 5 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 30/30
- [ ] **Submit the index-based version and read the score.** It should be
      8/14: every small case passing, every large case timing out. Read the
      timing note below before publishing -- this problem depends on the
      grader's clock more than any other in chapters 4 and 5

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| One pass with a cursor (registered) | 14/14 | -- |
| Index-based loop over `get` / `add(int,T)` / `set(int,T)` | 8/14 | times out on 08 through 13 |
| Oddness tested as `x % 2 == 1` | 5/14 | wrong on 00 01 04 05 06 07 10 11 13 |
| The two branches swapped | 0/14 | all |
| Unmodified stub | 0/14 | all |

Reference timing: 330 to 422 ms on the five largest cases.

**The shape of the 8/14 is the lesson.** It passes every case up to
n = 30,000-ish and fails every case at n = 200,000, so a student can read off
that the logic was right and the traversal was not. A score that was simply
low would not say that.

## Timing: read this before publishing

This is the only problem in chapters 4 and 5 whose intended mistake is caught
by the clock alone rather than by a wrong value, so it is the one most exposed
to the grader running at a different speed than this container.

The margin is wide -- the index-based version is quadratic, so at n = 200,000
it is not close to finishing rather than slightly over -- but confirm it after
publishing. If any of cases 08 through 13 passes for the index-based version,
raise `n` rather than leave a problem that appears to test 5.4 and does not.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` asserts the value
cap on every generated list.

**Values are capped at $10^8$, not $10^9$.** Ten times a value has to stay
inside an `int`, and $10^9 \times 10$ does not. Raising the cap would add a
silent overflow to a problem that is not about overflow -- `ds-tutorial-03-sum`
and `ds-04-array-growth` own that lesson.

The reference model in `gen.py` compares `x % 2 != 0` rather than `== 1` for
the same reason the Java solution does: Python and Java disagree on the sign
of the remainder for negative operands, and writing the model the careless way
would have produced expected output matching the careless Java solution.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
