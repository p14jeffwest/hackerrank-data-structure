# ds-12-sort-trace: upload checklist

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

Both 01 and 02 earn their places:

- **01** is `K = 0`, where the answer is the input unchanged. A solution that
  simply sorts fails it on sight.
- **02** is one pass on `9 3 7 5 1`, giving `1 3 7 5 9`. The smallest value was
  at the back, so the front value has been thrown to the back -- **the tail is
  not the original order**. That is the part of an intermediate state students
  expect wrongly.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-12-sort-trace`
- [ ] **Max Score = 10**
- [ ] Place it first among the chapter 12 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 10/10
- [ ] Confirm the LaTeX in Constraints renders

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Fails on |
|---|---|---|
| `k` passes of selection sort on a copy (registered) | 14/14 | -- |
| Sort the whole array, ignoring `k` | 6/14 | 00 01 02 04 09 10 12 13 |
| Retrying the position when the smallest is already there | 12/14 | 00 12 |
| `k` passes of **bubble** sort instead | 7/14 | 00 02 04 09 10 12 13 |

Reference timing: 65 to 67 ms. This is the fastest problem in the set.

The self-swap variant only reaches 12/14, and the reason is worth knowing: a
pass that swaps a value with itself changes nothing, so it can only be caught
where the extra pass it awards itself goes on to move something. Case 03 -- an
already sorted array, every pass a self-swap -- cannot catch it and was never
going to.

## The bound was deliberately NOT raised

Every other problem in this set had its bounds raised from the book's. This
one keeps the Korean version's `N <= 2,000`, because selection sort is
$O(n \cdot k)$ and therefore $O(n^2)$ at `k = n-1`. **A larger `n` would time
out the intended solution, not a wrong one.** There is nothing to gain.

## What no test can check

The method is told not to modify the array it is given. The driver never looks
at that array again, so nothing in the output depends on it. It is asked for
in the statement and recorded in `variants.md` as an exam question.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
