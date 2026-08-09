# ds-04-array-growth: upload checklist

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

No code stub. The default Java template is what students should see. See the
note at the end on why this problem, unlike the other two chapter 4 problems
that use a stub, deliberately hands the student no list.

## 2. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

`testcases/SAMPLES` lists the case numbers to mark.

## 3. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 4. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 5. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-04-array-growth`
- [ ] **Max Score = 30**
- [ ] Place it fourth among the chapter 4 problems

## 6. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 7. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 30/30
- [ ] Confirm the two tables in the Problem Statement render
- [ ] **Read the timing note below before publishing.** This problem's
      separation depends on the grader's time limit more than any other so far

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| Reference (sizes only, `long` accumulator) | 14/14 | -- |
| Move counter kept in `int` | 10/14 | wrong on 08 10 11 13 |
| Builds the list and moves elements one at a time | 11/14 | times out on 08 10 13 |
| Grows after the operation instead of before | 6/14 | wrong on 00 04 06 07 08 11 12 13 |

Reference timing: 226 to 300 ms on the four largest cases.

## Timing: read this before publishing

The list-building mistake is the one this problem is really aimed at, and it is
the one whose fate depends on the grader. Measured in this container:

| Case | Reference | Builds the list | Ratio |
|---|---|---|---|
| 08 | 289 ms | 19,434 ms | 67x |
| 13 | 300 ms | 6,846 ms | 23x |
| 10 | 270 ms | 4,461 ms | 17x |
| 11 | 262 ms | 3,279 ms | 13x |
| 12 | 218 ms | 377 ms | 1.7x |

At a 4-second limit that is 11/14, which is the figure recorded above. At a
12-second limit it would be 13/14 and the problem would separate almost
nothing -- an early run of these checks used a 12-second timeout and reported
exactly that, which is how the discrepancy was noticed.

Only case 08 has a comfortable margin. **After publishing, submit the
list-building version yourself and see what the grader says.** If it passes
case 10 or 11, those cases are not doing their job and the honest fix is to
raise `Q` rather than to leave a problem that looks like it discriminates and
does not.

## Why there is no code stub here

`ds-04-rotate` and `ds-04-majority` both supply a complete `Array_List` and ask
the student to write one method against it. This problem does the opposite, on
purpose.

Everything it asks for -- moves, copies, final capacity -- is a function of the
size and the capacity. The values stored never enter into it, which is why the
input carries no values at all. A student who allocates an array and shuffles
elements around is doing work the problem does not require, and the large cases
say so by timing out.

Handing over an `Array_List` would push students toward exactly that. The
chapter 4 content being tested here is 4.3's cost model, not 4.2's
implementation, and the right shape for it is a bare simulation of the counters.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` replays every
generated sequence before writing it, asserting that each position would pass
the book's `checkPosition` -- non-empty list, and $0 \le i < size$.

Case 07 is deliberately capped at a quarter of the maximum total so that its
move counts stay inside `int`. Without that cap the overflow mistake would fail
nearly everything, and a 1/14 tells a student much less than a 10/14 does.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
