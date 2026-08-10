# ds-08-climb-stairs: upload checklist

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

Case 02 is the one that must be public. It is `44 45 46 47`, and a solution
counting in `int` prints

```
1134903170
1836311903
-1323752223
512559680
```

A negative number of staircases, from a program that throws nothing and warns
about nothing. Hide this case and the same student sees only an unexplained
partial score.

`testcases/SAMPLES` lists the case numbers to mark.

## 3. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 4. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 5. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-08-climb-stairs`
- [ ] **Max Score = 30**
- [ ] Place it third among the chapter 8 problems

## 6. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 7. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 30/30
- [ ] **Submit an `int` version on purpose** and look at sample 02's output
- [ ] Confirm the LaTeX in Constraints renders

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Fails on |
|---|---|---|
| Table filled once in `long`, then looked up (registered) | 14/14 | -- |
| The same table in `int` | 3/14 | 11 cases |
| Plain recursion, no memoization | 2/14 | times out on 12 cases |
| `ways(2)` set to 1 | 0/14 | all |

Reference timing: 58 to 71 ms. This is the fastest problem in the set; the
table has 90 entries and every query is a lookup.

## Why the bound is 90 and not the book's 45

The book states `n <= 45`. That sits on exactly the wrong side of a line:

| | value | fits in `int`? |
|---|---|---|
| `ways(45)` | 1,836,311,903 | yes |
| `ways(46)` | 2,971,215,073 | **no** |
| `ways(90)` | 4,660,046,610,375,530,309 | fits in `long` |

At `n <= 45` an `int` solution is simply correct, and the type question never
comes up. At `n <= 90` it is the point of the problem. The Korean counterpart
made this change first and this version keeps it, so the two courses stay
identical.

Note also that `ways(90)` is 4.66 * 10^18 against a `long` ceiling of
9.22 * 10^18 -- comfortable, but only just. `n = 92` would overflow `long`
too, which is worth knowing before anyone raises the bound again.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` asserts the
three boundary facts above before writing anything, so if the recurrence or
the bound is ever edited the assertions fail rather than the data quietly
going wrong.

Cases 11 and 13 are drawn entirely from `n <= 20` and `n <= 45`. They exist to
keep the two main mistakes **partial**: without them, plain recursion and the
`int` table would both score near zero and tell the student nothing about
which half of the problem they got wrong.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
