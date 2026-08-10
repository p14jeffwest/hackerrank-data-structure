# ds-12-kth-largest: upload checklist

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

Head and Tail are the Korean version's, with the method renamed.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 02 and 04 as samples**

Case 04 is `9 9 9 5 1` with `k = 2`, answer `9`. A solution that counts
**distinct** values answers `5`. Nothing else in the samples shows it.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-12-kth-largest`
- [ ] **Max Score = 30**
- [ ] Place it third among the chapter 12 problems

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
| Sort ascending, read `nums[n-k]` (registered) | 14/14 | -- |
| Size-`k` min-heap | **14/14** | the book's other method, also correct |
| Take the maximum out `k` times | 12/14 | times out on 12 and 13 |
| Reading `nums[k-1]` after an ascending sort | 2/14 | wrong on 12 cases |
| Counting distinct values | 10/14 | wrong on 01 04 05 12 |

Reference timing: 306 to 326 ms.

## The comparison the book asks for cannot be graded

12.8 Problem 1 is explicitly *"compare an approach using a full sort with one
using a partial sort"*. Both are correct, and at these sizes neither is
faster:

| Case | Full sort | Size-k heap |
|---|---|---|
| 11 (k = 5) | 321 ms | 282 ms |
| 12 (k = n/2) | 306 ms | 355 ms |
| 13 (k = n) | 326 ms | 277 ms |

The difference does not show. Say so to students rather than implying the heap
is required -- the honest position is that this problem asks them to write
either one, and the exam asks them **when** the choice would matter.
`variants.md` reserves that question for the English section.

## What the bounds do exclude

The approach students reach for first: take the maximum out, `k` times. That
is $O(N \cdot k)$, which is $2 \times 10^{10}$ at case 12 and
$4 \times 10^{10}$ at case 13.

**Case 11 keeps `k` at 5 on the same array size**, so the same mistake passes
there. That turns a total failure into 12/14, and the two failing cases point
straight at large `k` -- which is exactly the thing to understand.

## Two changes from the Korean version

- It asks for the k-th **largest**, following 12.8, where the Korean version
  asks for the smallest. Same algorithm, opposite end.
- **The stub no longer sketches quickselect.** The Korean comments describe
  the partition step; this book compares a sort with a heap instead, and
  naming a third method in the stub would give away more than the book does.
  Quickselect is reserved in `variants.md` as the Korean section's exam axis.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. The model sorts and
indexes, which is the same idea as the registered solution -- unavoidable
here, since the answer is defined by the sorted order.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
