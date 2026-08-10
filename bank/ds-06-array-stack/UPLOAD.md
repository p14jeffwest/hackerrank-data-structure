# ds-06-array-stack: upload checklist

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
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 does nothing but touch an empty stack, which is where a missing
`isEmpty` check turns into `crash` rather than `empty`.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-06-array-stack`
- [ ] **Max Score = 10**
- [ ] Place it first among the chapter 6 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] **Submit the stub untouched.** It compiles and scores 0/14
- [ ] Confirm the LaTeX in Constraints renders

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Fails on |
|---|---|---|
| Reference implementation | 14/14 | -- |
| `item[top++]` instead of `item[++top]` | 0/14 | all -- the first push writes to index -1 |
| `pop` without `top--` | 2/14 | 12 cases |
| `push` without `ensureCapacity()` | 6/14 | 04 05 06 09 10 11 12 13 |
| `pop` and `peek` without their `isEmpty` checks | 8/14 | 00 02 03 09 12 13 |
| Unmodified stub | 0/14 | all |

Reference timing at Q = 200,000: 298 to 311 ms.

The `ensureCapacity` mistake fails exactly the cases where the stack ever holds
more than 50 elements, which is the default capacity. Cases 00 through 03 and
07 08 stay under it deliberately, so the score is partial and points at the
right place.

## The driver distinguishes `empty` from `crash`, and it had to

The first version of the Tail caught `RuntimeException` and printed `empty`.
Under it, a solution with **no empty checks at all scored 14/14**: with
`top == -1`, `pop` reads `item[-1]`, that throws
`ArrayIndexOutOfBoundsException`, `ArrayIndexOutOfBoundsException` is a
`RuntimeException`, and the accidental catch produced exactly the right word.

The Tail now catches `IndexOutOfBoundsException` separately and prints
`crash`, which drops that solution to 8/14. Reading outside the array is a bug
and should not be able to impersonate a correct underflow report.

This is worth remembering for chapter 7: the same pattern will appear for an
empty queue, and the same accident is available there.

## What no test can catch

Leaving `item[top] = null` out of `pop` changes no output. Nothing the driver
can see depends on it -- it exists so the garbage collector can reclaim the
object, and it is the reason `clear` is $O(n)$ rather than one assignment.
Same untestable point as in `ds-04-array-list`; `variants.md` records it as an
exam axis and notes that it should be spent once, not twice.

## Deviation from the book

The book's `ArrayStack` sets `MAX_CAPACITY` to 10,000. With the default
capacity of 50 that caps the stack at **6,400 elements**, because the next
doubling would be 12,800 and `ensureCapacity` throws. The constant is a
safeguard against unbounded pushing rather than a teaching point, so it is
raised to 1,000,000 here. Everything else in the Head is the book's code as
written.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` reports the
maximum stack depth of each case, which is the number that decides whether the
`ensureCapacity` mistake is caught by it.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
