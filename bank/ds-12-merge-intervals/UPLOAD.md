# ds-12-merge-intervals: upload checklist

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

The Tail prints the count first, then the intervals, so the student does not
have to size anything themselves.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 03 and 04 as samples**

Both 03 and 04 are there for a specific mistake:

- **03** is five intervals meeting end to start, collapsing into one. A `>=`
  comparison leaves all five separate.
- **04** is nested: `[1,10]` swallows `[2,3]` and `[4,5]`. Taking the newer
  end instead of the larger shrinks the group to `[1,3]`.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-12-merge-intervals`
- [ ] **Max Score = 30**
- [ ] Place it fourth among the chapter 12 problems

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

| Submission | Result | Fails on |
|---|---|---|
| Sort by start, then one pass (registered) | 14/14 | -- |
| `>=` so touching intervals stay separate | 9/14 | 03 06 10 11 13 |
| Taking the new interval's end, not the larger | 9/14 | 04 07 10 11 12 |
| Not sorting by start | 4/14 | 10 cases |
| Absorbing overlapping pairs repeatedly, O(n^2) | 12/14 | times out on 11 and 13 |

Reference timing: 520 to 728 ms.

The two boundary mistakes both score 9/14 but fail **different** cases, so the
score still identifies which one it was. Only 10 and 11 are failed by both.

## The boundary rule is the opposite of ds-11-meeting-rooms

This is the thing to keep straight when teaching, and when editing either
problem:

| | Two intervals sharing an endpoint |
|---|---|
| `ds-11-meeting-rooms` | do **not** overlap -- one room takes both |
| `ds-12-merge-intervals` | **do** overlap -- they merge |

Both are the book's own rules, each stated in its own chapter, and both
problems take the same `{start, end}` input. **A comparison carried across
from one to the other is wrong in a way that passes most small cases.**

`variants.md` makes this the reserved exam axis rather than something to be
discovered by accident, and both `meta.yml` files cross-reference each other.

## A note on which large case is slowest

Case 11 -- 200,000 short intervals over a wide span -- is the slowest for the
reference at 728 ms, and cases 12 and 13 are faster despite being the same
size. The reason is the **output**: in case 11 almost nothing merges, so the
result list stays nearly as long as the input; in 12 and 13 everything
collapses to a single interval.

Worth remembering for any problem whose output size depends on the answer:
the largest input is not necessarily the slowest case.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. Every case is shuffled
before writing, so no solution can pass by assuming the input arrives sorted.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
