# ds-13-merge-two: upload checklist

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

The Tail reads with `StreamTokenizer`, so it never depends on line structure.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 has an empty first array. It shows two things at once: that a
zero-length array has **no values line at all**, and that with nothing to
compare against, one tail loop does all the work while the other must not run.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-13-merge-two`
- [ ] **Max Score = 10**
- [ ] Place it first among the chapter 13 problems

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
| Two indices, both tails copied (registered) | 14/14 | -- |
| Only one of the two tails copied | 6/14 | 01 02 03 05 07 09 12 13 |
| Advancing both indices on a tie | 9/14 | 01 05 09 10 13 |
| Concatenate and call `Arrays.sort` | **14/14** | not excluded -- see below |

Reference timing: 380 to 381 ms.

## Sorting instead of merging cannot be excluded

| Case | Merge | Concatenate and sort |
|---|---|---|
| 10 | 380 ms | 422 ms |
| 11 | 381 ms | 416 ms |
| 12 | 381 ms | 363 ms |

At 400,000 values the log factor costs almost nothing, and on case 12 the
library sort is actually faster -- it detects the two ascending runs.

The book asks for the merge because **it is the step merge sort is built
from**, not because sorting would be too slow here. The constraints say "do
not call a sort library" directly rather than pretending the bound enforces
it. Anyone who ignores that line passes; the requirement is assessed on the
exam.

## An empty array has no values line

A zero-length array writes its length and then **nothing** -- not a blank
line. The Tail reads with `StreamTokenizer`, which ignores line structure
entirely, so a blank line would carry no information and would only be
something an editor or an archive could quietly strip. Earlier problems in
this set (`ds-05-merge-sorted`, `ds-11-merge-k`) do carry blank lines and have
warnings about them; this format avoids the question.

`gen.py`'s own summary had to be rewritten to read the files as token streams
for the same reason -- reading by line broke on exactly these cases, and the
generator crashed rather than producing bad data.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` asserts that
both input arrays are ascending; an unsorted input would make the problem
unsolvable as stated and the failure would look like a bug in the student's
code.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
