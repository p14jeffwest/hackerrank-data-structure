# ds-07-last-card: upload checklist

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

**Case 02 is `N = 1`, and its expected output begins with an empty line.**
Confirm after upload that the blank first line survived. If the form or the
archive strips it, the case is unsolvable and the reason will not be obvious
to anyone.

`testcases/SAMPLES` lists the case numbers to mark.

## 3. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 4. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 5. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-07-last-card`
- [ ] **Max Score = 30**
- [ ] Place it second among the chapter 7 problems

## 6. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 7. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 30/30
- [ ] Confirm the empty first line of the `N = 1` sample displays correctly
- [ ] Confirm the LaTeX in Constraints renders

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| `ArrayDeque` (registered) | 14/14 | -- |
| `ArrayList` with `remove(0)` | 8/14 | times out on 08 through 13 |
| The two steps swapped | 2/14 | passes only N = 1 and the all-equal case |
| Discards two cards per round | 1/14 | passes only N = 1 |

Reference timing: 324 to 363 ms. The `ArrayList` version takes 6.6 s on case
12 alone, against 324 ms for the reference -- a twentyfold margin, so this one
does not depend on the grader's exact limit.

**`java.util.LinkedList` is a correct solution, not a wrong one.** It was
tried as a fourth variant and scored 14/14: its `get(0)` and `remove(0)` are
both $O(1)$, so it works as a deque here. Worth knowing before telling a
student otherwise.

The swapped-steps mistake passes exactly two cases, and both for reasons worth
seeing: `N = 1`, where nothing happens at all, and case 10, where every card
carries the same number so no discard order can be distinguished from another.

## Deviation from the book's statement

7.5 Problem 4 numbers the cards 1 through N and asks only for the survivor.
That version does not need a queue: the survivor of 1..N has a closed form,
and a student who finds it never simulates anything.

Two changes fix it, both taken from the Korean counterpart:

- the cards carry **arbitrary numbers**, so no formula in N gives the answer;
- the **discard order** is part of the answer, and it cannot be produced
  without running the simulation to the end.

The rule and the worked examples are the book's, and the book's own cases are
kept as sample 01 (cards 1..5, survivor 2) and case 04 (cards 1..7,
survivor 6). The closed form is reserved in `variants.md` as an exam question
for the English section -- it is a good question precisely because the contest
version blocks it.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` asserts that the
discard list has exactly `N - 1` entries, which is the cheapest check that the
simulation ran to completion.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
