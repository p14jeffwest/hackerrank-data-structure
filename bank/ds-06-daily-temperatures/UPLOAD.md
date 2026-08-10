# ds-06-daily-temperatures: upload checklist

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

Case 02 is the important one. On `73 73 74` the answer is `2 1 0`, and a
solution written with `>=` prints `1 1 0`. Nothing else a student can see
distinguishes the two comparisons.

`testcases/SAMPLES` lists the case numbers to mark.

## 3. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 4. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 5. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-06-daily-temperatures`
- [ ] **Max Score = 30**
- [ ] Place it third among the chapter 6 problems

## 6. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 7. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 30/30
- [ ] **Submit the forward-scanning version and read the score.** It should be
      10/14. See the timing note below for the one case that is close
- [ ] Confirm the LaTeX in Constraints renders

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| Monotonic stack of indices (registered) | 14/14 | -- |
| Scan forward from each day, O(n^2) | 10/14 | times out on 08 09 11 13 |
| Comparison written `>=` | 2/14 | wrong on 12 cases |
| Distance as `i - waiting - 1` | 2/14 | wrong on 12 cases |
| Temperatures pushed instead of indices | 2/14 | wrong on 12 cases |

Reference timing: 250 to 446 ms across the large cases.

## Timing

The forward-scanning mistake is caught by the clock, so the margins matter:

| Case | Reference | Forward scan |
|---|---|---|
| 09 | 298 ms | 30,190 ms |
| 12 | 266 ms | 3,434 ms |
| 10 | 258 ms | 755 ms |

Case 09 has a hundredfold margin and is the one to rely on. **Case 12 sits at
3.4 seconds and will fall on either side of a 4-second limit** depending on
the grader; treat its contribution as unreliable rather than assuming it
counts. Cases 08, 11 and 13 do not finish at all.

## Two things worth knowing about the temperature range

The book pins temperatures to 30..100, and that is kept. Two consequences
follow that are easy to get wrong when editing the data.

**It does not rescue the naive solution.** With 71 distinct values a strictly
decreasing run is at most 71 long, which sounds as if the forward scan can
never travel far. It can: when readings repeat, no day finds a warmer one at
all and the scan runs to the end of the array from every position.

**It is also what fills the stack.** An equal reading never pops anything, so
a run of identical temperatures pushes all $n$ indices. Case 08 is exactly
that, and it is the deepest the stack ever gets.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed.

**Case 09 took two attempts.** Built first as descending blocks of 200 to 2000
days, it looked punishing but was not: a warmer day was only a block away, so
the naive scan finished in 0.6 seconds. It is now a single long descent across
the whole array with one warm day at the very end -- every day does have an
answer, but it is the last index, so the scan travels almost the full length
from almost every position. That took the naive solution from 0.6 s to 30 s.

The lesson generalises: for a "next greater" problem, long distances come from
putting the answer far away, not from making the input look complicated.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
