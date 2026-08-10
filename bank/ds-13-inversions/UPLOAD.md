# ds-13-inversions: upload checklist

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

Head and Tail are the Korean version's, unchanged apart from line endings.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 is ten copies of one value, where the answer is `0`. A merge written
with `<` instead of `<=` counts equal values and answers `45`.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-13-inversions`
- [ ] **Max Score = 30**
- [ ] Place it third among the chapter 13 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 30/30
- [ ] Confirm the LaTeX in Constraints renders

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| Merge sort with the count on the merge (registered) | 14/14 | -- |
| Checking every pair, O(n^2) | 12/14 at 5 s, 10/14 at 4 s | see below |
| `<` instead of `<=`, counting equal values | 10/14 | wrong on 02 09 10 13 |
| Counting in an `int` | 11/14 | wrong on 10 11 13 |
| Adding 1 per merge step instead of the block | 6/14 | wrong on 8 cases |

Reference timing: 184 to 290 ms.

The `int` mistake is worth showing: on case 11 it prints **-1474936480** for
an answer of 19,999,900,000. A negative count of inversions, from a program
that throws nothing.

## The quadratic solution depends on the SHAPE, not the size

Measured, all at n = 200,000 and all doing the same 2 x 10^10 comparisons:

| Case | Input | Quadratic solution |
|---|---|---|
| 10 | random | 19.1 s |
| 13 | random, three distinct values | 19.1 s |
| 11 | strictly descending | **4.2 s** |
| 12 | strictly ascending | **4.1 s** |

A factor of **4.6 between identical comparison counts**. On the sorted arrays
the comparison `a[i] > a[j]` has the same answer every time, so the branch
predictor never misses; on random data it misses constantly.

The practical consequence: **cases 11 and 12 sit right on a four-second
limit.** Cases 10 and 13 time the mistake out decisively either way, so it is
caught regardless -- but the score it earns will differ between graders, and
the table above should not be quoted as exactly 10/14 or 12/14.

This is also a good thing to show a class. "Same number of operations" and
"same running time" are not the same statement, and here is a clean example
where they differ by nearly five times.

## One change from the Korean version

The Korean stub lists the merge-counting procedure step by step, including
"when right is chosen first, add remaining left size" -- which is the whole
answer. That has been removed; the stub now says only that merge sort does the
same comparisons in $O(n \log n)$ and that the counting can be hung on its
merge step.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. **The model uses a
Fenwick tree** over the compressed values, sweeping from the right and
counting how many smaller values have already been seen. That is a different
algorithm from the one the problem teaches, so a mistake in the merge-counting
reasoning could not be mirrored in the expected answers.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
