# ds-14-longest-consecutive: upload checklist

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

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 02 and 03 as samples**

- **02** is `5 5 6 6 7 7`: six values, three distinct, answer 3. Letting a
  repeat extend a run answers 6.
- **03** is the empty array. `n` is 0 and **there is no second line at all** --
  not a blank one. Confirm after upload that the file is two bytes, `0` and a
  newline.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-14-longest-consecutive`
- [ ] **Max Score = 30**
- [ ] Place it fourth among the chapter 14 problems

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
| Hash set with the start-of-run check (registered) | 14/14 | -- |
| No start-of-run check | 10/14 | times out on 09 10 11 13 |
| A list instead of a set, so duplicates stay | 9/14 | times out on the five large cases |
| Sort and scan | **14/14** | not excluded -- see below |

Reference timing: 280 to 335 ms.

## The book's "sorting is not allowed" cannot be enforced -- sorting is faster

Measured at n = 100,000:

| Input | Hash set | Sort and scan |
|---|---|---|
| one long consecutive run | 197 ms | 228 ms |
| random values, no runs | 228 ms | **191 ms** |

A `HashSet` of boxed `Integer`s carries a large constant; `Arrays.sort` on an
`int[]` carries a tiny one. The $\log n$ factor never closes that gap at any
size this problem can hold, so raising `n` would only make both slower.

The requirement is stated in the constraints and assessed on the exam, the
same position as `ds-13-counting-sort` and `ds-13-merge-two`. **Say this to
students rather than implying the hash set is required for speed** -- the
honest statement is that the hash set is what the chapter is about, and that
here it is not even the faster of the two.

## What the clock does enforce, decisively

The start-of-run check:

| Input | With the check | Without |
|---|---|---|
| one shuffled run of 100,000 | 197 ms | **15,717 ms** |
| random values | 228 ms | 239 ms |

Without it, a run of length `L` is walked from each of its `L` members.
That is precisely the point the book's own answer calls "the key", so the
enforceable half of this problem is the half worth enforcing.

**Case 12 is random values with almost no runs**, and the mistake survives it
-- there is nothing long to re-walk. That keeps it at 10/14 rather than 0 and
tells the student the long runs are what broke them.

## The empty array

Case 03 is `n = 0`, and the input file is two bytes: `0` and a newline, with
**no second line at all**. The Tail reads with `StreamTokenizer`, which
ignores line structure, so a blank line would carry no information and could
only be lost in transit. Same choice as `ds-13-merge-two`.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. The model uses the same
set-and-walk method as the solution; the answer is defined by membership, so
there is no meaningfully independent way to compute it, and the two were run
against each other.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
