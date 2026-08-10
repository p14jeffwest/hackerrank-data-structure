# ds-08-subsets: upload checklist

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

Case 02 gives the input in descending order. A solution that skips the sort
produces exactly the right subsets, in the wrong order and with the elements
inside each one reversed:

```
expected:  (empty) / 3 / 3 4 / 3 4 5 / 3 5 / 4 / 4 5 / 5
unsorted:  (empty) / 5 / 5 4 / 5 4 3 / 5 3 / 4 / 4 3 / 3
```

`testcases/SAMPLES` lists the case numbers to mark.

## 3. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 4. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 5. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-08-subsets`
- [ ] **Max Score = 30**
- [ ] Place it fourth among the chapter 8 problems

## 6. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 7. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 30/30
- [ ] Confirm the LaTeX in Constraints renders

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Fails on |
|---|---|---|
| Sort, then emit at every node (registered) | 14/14 | -- |
| Input never sorted | 3/14 | 11 cases |
| No unchoose step after the recursive call | 1/14 | 13 cases |
| Emitting only at the leaves | 0/14 | all |
| The book's shape, saving a reference instead of a copy | 0/14 | all |

Reference timing: 159 to 197 ms.

## The ordering decision

The book says the order of the subsets does not matter. That is fine for a
printed answer and useless for a grader, so this version fixes it: elements
ascending within a subset, subsets in lexicographic order, shorter first when
one is a prefix of the other.

The order was not chosen arbitrarily. **It is exactly what the natural
recursion produces once the input is sorted**, so a student pays for one sort
of `n` values and never has to sort $2^n$ subsets. Walking the indices upward
is what guarantees it: everything beginning with `a[i]` is finished before
anything beginning with `a[i+1]` begins.

The input is then given shuffled on purpose, so that the one sort cannot be
skipped.

## The copy mistake

The book's own answer stresses `result.add(new ArrayList<>(current))` and
explains why. The reference solution here sidesteps the question entirely by
writing each subset into the `StringBuilder` as it is found, rather than
collecting a list of lists.

That is worth knowing when teaching from this problem: **a student following
the book's structure meets a trap that the reference solution does not have.**
Written the book's way without the copy, every saved subset is a reference to
the same list, and the output is $2^n$ copies of whatever it held at the end.
It scores 0/14, and the failure is total rather than partial, so the sample
cases are where it has to be diagnosed.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` asserts that
each case produces exactly $2^n$ subsets and that the input values are
distinct.

The model is iterative rather than recursive, for the same reason as
`ds-08-hanoi`: it is not worth risking Python's default recursion limit on
data this size. Model and Java solution were compared byte for byte on cases
10 and 13.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
