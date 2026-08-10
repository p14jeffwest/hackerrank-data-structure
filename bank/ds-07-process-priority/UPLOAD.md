# ds-07-process-priority: upload checklist

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

Case 02 is all-equal priorities. A comparison written `>=` makes them displace
each other and the queue never empties, so this is where that mistake shows --
as a hang, which students do not expect from a comparison operator.

`testcases/SAMPLES` lists the case numbers to mark.

## 3. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 4. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 5. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-07-process-priority`
- [ ] **Max Score = 30**
- [ ] Place it third among the chapter 7 problems

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
| Sorted priorities with a pointer (registered) | 14/14 | -- |
| The book's own answer: scan the queue on every poll | **14/14** | passes; see below |
| `ArrayList` with `remove(0)` | **14/14** | passes; see below |
| Higher-priority test written `>=` | 5/14 | hangs on 00 02 03 06 07 08 10 11 12 |
| Run order counted from 0 | 0/14 | all |

Reference timing: 662 ms on case 09, the heaviest.

## What this problem does not test, and why

**It does not discriminate on data structure, and it cannot.** That was
measured rather than assumed:

| Case | Reference | Book's scan | `ArrayList` |
|---|---|---|---|
| 09 | 662 ms | 401 ms | 1140 ms |
| 10 | 485 ms | 569 ms | 902 ms |

Two reasons. The book's scan stops at the **first** higher-priority process it
meets, so it is far shorter than its $O(n)$ bound most of the time. And
`ArrayList.remove(0)` is only about twice as slow as a deque at this size,
because `System.arraycopy` over a thousand ints costs almost nothing next to
the number of polls.

**Raising `N` does not fix it.** The number of queue operations is itself
quadratic: with priorities $1, 2, \dots, N$ the queue turns over completely
before each run, so any faithful simulation performs $N(N+1)/2$ polls. At
$N = 1{,}000$ that is 500,500 polls per test and the reference is already at
662 ms. Push further and the **correct** solution times out before either
wrong one does.

So the bound was raised only tenfold from the Korean version, and the honest
description of this problem is that it tests **the rule**, not the
implementation:

- `>` versus `>=`, which decides whether the queue ever empties;
- counting the run order from 1 rather than 0.

`variants.md` reserves "what is the worst-case poll count, and which input
achieves it" as the English exam question, precisely because the contest
version cannot ask it.

## A trap in the test data worth remembering

The simulation **stops as soon as the tracked process runs**. An earlier
version of case 09 chose the target at random, and with a high-priority target
the loop ended after a handful of polls -- the case looked large and tested
nothing. Cases 09 through 12 now set the target to the process that runs
**last**, which is what forces the full simulation.

Whenever a problem's loop has an early exit, check that the large cases
actually reach the end.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
