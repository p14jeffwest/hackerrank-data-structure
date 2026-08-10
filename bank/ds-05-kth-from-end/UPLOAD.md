# ds-05-kth-from-end: upload checklist

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

The Head here is short -- just the `Node` class and the opening of `Solution`
-- but it is load-bearing. The premise is that the length is unknown, and the
only way to hold a student to that is to hand them a bare `Node`. Written with
plain standard input, they would read `n` themselves and there would be no
problem left.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

All three matter here, more than usual. See the note below on why an
off-by-one scores zero.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-05-kth-from-end`
- [ ] **Max Score = 10**
- [ ] Place it second among the chapter 5 problems

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

| Submission | Result | Cause |
|---|---|---|
| Two pointers, one pass (registered) | 14/14 | -- |
| Head start of `k - 1` steps | 0/14 | returns the node after the right one |
| Head start of `k + 1` steps | 0/14 | wrong, and throws `NullPointerException` when k = n |
| For each node, count the nodes after it | 10/14 | times out on 08 10 12 13 |
| Unmodified stub | 0/14 | all |

Reference timing: 210 to 247 ms on the five largest cases.

## Why a zero here is acceptable

Both off-by-one mistakes score 0/14 rather than a partial score, which usually
tells a student nothing. It is defensible here only because the three samples
diagnose the error precisely, before submission:

- **00** puts the wrong value next to the right one on the book's own example.
- **01** is `k = 1` in every test case, so a pointer sent one step short
  returns the second-to-last node -- visible immediately.
- **02** is `k = n` in every test case, so a pointer sent one step too far
  walks off the end and throws `NullPointerException` rather than printing
  anything.

Publish all three or this reasoning does not hold.

## What this problem does not enforce

The book asks for a **single traversal**. That cannot be checked. Measuring the
length first and then walking `n - k` is two passes, still $O(n)$, and passes
comfortably. Copying the nodes into an array passes too, at $O(n)$ space.

So the constraints ask for $O(n)$ time and $O(1)$ extra space rather than
claiming a single pass is required. Do not present the single pass to students
as if it were enforced. `variants.md` reserves "which of these survives if the
list can only be read once" as the exam question that does test it.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed.

Case 12 is worth understanding: a list of 200,000 copies of `42` with a single
`-999` planted at exactly the answer position. A solution that returns any
plausible-looking node passes every other large case and fails this one.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
