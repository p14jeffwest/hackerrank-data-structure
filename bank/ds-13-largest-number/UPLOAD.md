# ds-13-largest-number: upload checklist

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

Both 02 and 03 exist for one mistake each:

- **02** is `3 30 302 303`. Numbers that are prefixes of one another are the
  **only** situation where sorting by value and sorting by concatenation
  disagree. Correct: `330330302`. By value: `303302303`.
- **03** is four zeros. Correct: `0`. Without the special case: `0000`.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-13-largest-number`
- [ ] **Max Score = 30**
- [ ] Place it fourth among the chapter 13 problems

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
| Sort on the concatenation comparison (registered) | 14/14 | -- |
| Sort by value, descending | 5/14 | 00 01 02 06 08 09 11 12 13 |
| Sort by plain string order, descending | 8/14 | 00 02 09 11 12 13 |
| No all-zeros case | 13/14 | 03 only |

Reference timing: 343 to 601 ms. Case 12's answer is 888,842 digits long.

## The model was wrong first, and the Java solution caught it

The comparator's sign in `gen.py` was inverted. It sorted **ascending**, and
produced `3033459` for the book's own example instead of `9534330`. Every case
disagreed with the Java solution on the first comparison run.

`gen.py` now puts the comparison in a named function with the sign spelled out
in a comment, along with a note recording what went wrong.

**This is the one problem in the set where the model and the solution
necessarily share their reasoning.** Everywhere else the generator computes
the expected answer a different way -- a Fenwick tree against merge counting,
a sweep against a heap, prefix sums against a BST walk -- precisely so a
mistake in one cannot be mirrored in the other. Here the required order *is*
the comparison, so there is no independent method available. Running the two
implementations against each other is the only check there is, which is
exactly why it is always run.

## What sorting by value gets wrong, and when

Only when one number is a **prefix** of another. `[9, 5, 34]` sorts the same
either way; `[3, 30]` does not. That is why case 02 and case 13 are built from
prefix families, and why a by-value solution still scores 5/14 -- most random
inputs do not contain a prefix pair at all.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed.

Case 12 is 100,000 random values, giving an answer of about 890,000 digits --
far beyond any numeric type, which is the point of asking for a string.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
