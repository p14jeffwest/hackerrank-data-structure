# ds-04-rotate: upload checklist

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

Open the Java language box and switch it from the default template to a custom
stub.

| Stub field | File |
|---|---|
| Head (above) | `07. stub-head.java` |
| Body (editable) | `08. stub-body.java` |
| Tail (below) | `09. stub-tail.java` |

- [ ] Paste all three
- [ ] Compare the rendered editor against `stub-preview.java`, which is the
      three files concatenated in order -- that file is what a student sees

The Head carries the complete `Array_List`, including the three methods that
`ds-04-array-list` asks students to write. That is deliberate: a student who
has not finished the previous problem can still read a working implementation
here, and one who has finished it sees their own work handed back.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

The test data is 24 MB in total, which is much larger than the earlier
problems. If the upload is refused for size, the four single-list cases
(08 through 11) are the ones to thin out, but keep at least one of them: they
are what stops a one-slot-at-a-time solution.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-04-rotate`
- [ ] **Max Score = 10**
- [ ] Place it second among the chapter 4 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 10/10
- [ ] **Submit the stub untouched.** It compiles and returns the list
      unchanged, which scores 2/14 -- the cases where `k % n` happens to be 0.
      Confirm it produces wrong answers rather than a stack trace
- [ ] **Check the reported run time on the largest cases.** This container is
      not the grader, and the correct solution sits at 300 to 460 ms here. If
      the grader is much slower, the timeouts below may start catching correct
      solutions too, and the bounds have to come down
- [ ] Confirm the LaTeX in Constraints renders

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| Reference implementation | 14/14 | -- |
| One slot at a time, `remove(n-1)` then `add(0, x)` | 6/14 | times out on 07 09 10 11; runtime error on 01 02 05 06 |
| Left rotation instead of right | 4/14 | wrong on 00 01 04 05 06 07 08 09 10 13 |
| Unmodified stub (returns the list unchanged) | 2/14 | passes only 02 and 11 |

Timing for the reference solution: 357 to 467 ms on the five largest cases.
Moving from `int[]` to `Array_List` cost nothing measurable, because `get(i)`
on an array-based list is $O(1)$.

The one-slot-at-a-time mistake fails in two different ways here, and both are
worth understanding. On the large cases it simply runs out of time. On the
cases containing a single-element list it **crashes**: `remove(n-1)` empties
the list, and `add(0, x)` on an empty list fails `checkPosition`, since a valid
position must refer to an element that already exists. That is the book's own
bounds rule doing its job, and it is left in place.

The four cases the left-rotation mistake survives are 02, 03, 11 and 12, and
each for a reason worth knowing:

- **02** every test case has `k % n == 0`, so nothing moves either way
- **03** every list has n = 2, where left and right rotation always agree
- **11** `k` is a multiple of `n`
- **12** one list is a single repeated value, the other has `k = n / 2`

## Deviation from the book

The book states this problem with `n` and `k` both at most $10^4$. At that size
every approach passes, including rotating one slot at a time, so nothing is
tested. The bounds here are sum of `n` at most $2 \times 10^5$ and `k` at most
$10^9$, which is what makes the book's own hint (reduce `k` first) matter. This
was agreed before the problem was built and is recorded in `meta.yml`.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed, so the output is identical
every time.

One trap found while generating the data, worth not repeating: **$10^9$ is an
exact multiple of 200,000.** Case 10 was meant to pair the largest `k` with the
largest `n`, but `k % n` came out 0 and the case had quietly turned into a
no-rotation test. It now uses $10^9 - 1$, which reduces to 199,999. Whenever a
bound and a list length are both round numbers, check the remainder before
trusting the case.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
