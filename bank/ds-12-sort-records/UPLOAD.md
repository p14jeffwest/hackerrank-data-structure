# ds-12-sort-records: upload checklist

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

`Student` is a plain class rather than a `record`, because `record` needs
Java 16 and the grader is on 15. That comment is in the Head; leave it there.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 03 as samples** (03, not 02)

Case 03 has every participant on the same score, so the answer is the input
unchanged. Sorting ascending and reversing the array -- the most common way to
reach for a descending order -- returns it backwards:

```
correct : a 100  b 100  c 100  d 100 ...
reversed: h 100  g 100  f 100  e 100 ...
```

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-12-sort-records`
- [ ] **Max Score = 10**
- [ ] Place it second among the chapter 12 problems

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
| Descending comparator on score only (registered) | 14/14 | -- |
| Sort ascending, then reverse | 4/14 | 10 cases |
| Comparator with a tie-break on name | 7/14 | 00 04 08 10 11 12 13 |
| A hand-written selection sort | 10/14 | 05 wrong; 11 12 13 time out |

Reference timing: 319 to 498 ms.

## One change from the Korean version

The Korean stub's comments explain that `Arrays.sort` on an array of objects
is stable and that the tie rule therefore needs nothing extra. **That has been
removed here.** Saying it outright leaves the student with nothing to work
out; the property is the problem.

Everything else -- signature, format, bounds, Head, Tail -- is unchanged.

## The selection-sort variant is worth understanding

A hand-written selection sort is **unstable**, which is the mistake the
problem is about, and it still scores 10/14. Only one of its failures is a
wrong answer (case 05); the rest are timeouts from being quadratic.

The reason is that a selection sort only disturbs a tie when a swap happens to
cross one. On many inputs it never does. **"Unstable" does not mean "visibly
wrong on every input"**, and that is worth saying to a class that has just
been told stability matters -- it is exactly why the property has to be
reasoned about rather than tested for by trying an example.

## Not a mistake

Writing the comparator as `y.score - x.score` rather than
`Integer.compare(y.score, x.score)`. Scores here are at most 1,000, so the
subtraction cannot overflow. It is a bad habit rather than a bug in this
problem, and no case punishes it.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. Python's `sorted` is
stable, so the model sorts on the negated score alone -- the same one-key idea
the solution uses, which is the one place where sharing the reasoning is
unavoidable and harmless, since the required order is defined by stability.

Ties are the whole test set. Case 13 is 100,000 participants on a single
score; case 12 spreads 100,000 across five scores.

`gen.py` asserts the name length and character set, which the Korean
constraints also specify.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
