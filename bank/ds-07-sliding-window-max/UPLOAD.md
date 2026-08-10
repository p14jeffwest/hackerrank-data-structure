# ds-07-sliding-window-max: upload checklist

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

Case 02 is the one that must be public. On `9 8 7 6 5` with `k = 2` the answer
is `9 8 7 6`, and a deque holding values instead of indices prints `9 9 9 9`:
it cannot tell that the 9 has left the window. Nothing else a student can see
distinguishes the two designs.

`testcases/SAMPLES` lists the case numbers to mark.

## 3. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 4. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 5. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-07-sliding-window-max`
- [ ] **Max Score = 50**
- [ ] Place it fourth among the chapter 7 problems

## 6. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 7. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 50/50
- [ ] **Submit the brute-force version and read the score.** It should be
      10/14, with the four large-window cases timing out
- [ ] Confirm the LaTeX in Constraints renders

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| Monotonic deque of indices (registered) | 14/14 | -- |
| Recompute each window's maximum, O(nk) | 10/14 | times out on 10 11 12 13 |
| Deque holds values instead of indices | 5/14 | wrong on 00 01 02 04 06 07 08 11 13 |
| Expiry tested `<=` instead of `<` | 4/14 | wrong on 10 cases |
| Output starts at `i >= k` | 0/14 | all |

Reference timing: 466 to 595 ms across the large cases.

## A miscounted cost, and how it hid

A brute-force scan costs **(n - k + 1) windows of k elements**, not `n * k`.
The first version of `gen.py` reported `n * k`, and on that figure case 09
(`k = n`) looked like the most expensive case in the whole set at
$2.5 \times 10^{11}$. It is in fact one of the cheapest: at `k = n` there is
exactly **one** window.

The consequence was that the brute-force variant scored 13/14 while the
generator's own summary suggested it should have been failing everywhere.
Cases 11, 12 and 13 now use window sizes near `n/3` and `n/2`, where
`(n - k + 1) * k` is genuinely large, and the score dropped to 10/14.

`gen.py` prints the corrected figure per case, and the comment there records
why. Worth remembering for any future window problem: the product peaks at
`k = n/2` and falls to `n` at both ends.

## What is not a mistake

Dropping from the rear on `<` rather than `<=` leaves indices of equal value
in the deque. The front is still the maximum, so the answers are identical;
the deque just holds a few more indices. No test separates the two, and none
tries to. If a student asks, that is the answer.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` asserts that
each case produces exactly `n - k + 1` answers, which is the cheapest check
that the window arithmetic is right.

Cases 11 and 12 are the two extreme shapes for the deque itself: strictly
decreasing fills it to `k` indices and never pops from the rear, while
strictly increasing clears it on every element and holds exactly one.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
