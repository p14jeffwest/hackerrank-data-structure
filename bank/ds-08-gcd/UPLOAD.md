# ds-08-gcd: upload checklist

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

The Tail uses `StreamTokenizer` rather than `BufferedReader` plus
`StringTokenizer`. With `T` at 100,000 and two numbers per line that is
200,000 tokens, which is where the difference starts to show. It is carried
over from the Korean version unchanged.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 gives every pair both ways round, which is where an assumption that
`a >= b` shows.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-08-gcd`
- [ ] **Max Score = 10**
- [ ] Place it fifth among the chapter 8 problems

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
| `gcd(b, a % b)`, base case `b == 0` (registered) | 14/14 | -- |
| Base case `b == 1` | 0/14 | all |
| Arguments reversed: `gcd(a % b, b)` | 0/14 | infinite recursion |
| Subtraction instead of remainder | 8/14 | 03 04 06 08 11 13 |
| Unmodified stub | 4/14 | it returns 1, right for the coprime cases |

Reference timing: 215 to 278 ms at `T` = 100,000. The deepest recursion in the
whole set is 43 calls, on consecutive Fibonacci numbers (cases 05 and 10).

**The subtraction version is the one to show students.** `gcd(a - b, b)` is
mathematically correct and, on `(1, 999999999)`, dies with a
`StackOverflowError` after a billion levels:

```
Exception in thread "main" java.lang.StackOverflowError
        at Solution.gcd(Solution.java:28)
```

That is exactly why Euclid's algorithm uses the remainder rather than
repeated subtraction, and it scores 8/14 -- a partial score that points
straight at the lopsided inputs.

**A fourth variant was written and thrown away**, and the reason is worth
recording for marking. A hand-rolled swap for the `a < b` case turned out to
be *correct*, not wrong. The swap is unnecessary rather than mistaken: when
`a < b`, `a % b` is `a`, so the first call simply reverses the pair at the
cost of one extra step. If a student writes the swap, it is a redundancy to
mention, not an error to mark down.

## Why this problem is here at all

**Euclid's algorithm does not appear anywhere in this book's chapter 8.** It
was added at the instructor's request so that the two courses share one more
problem -- the Korean book has it as a chapter 9 exercise, and teaching it
from one set of notes is worth more than strict book fidelity here.

The recursion it exercises is squarely chapter 8 material: one recursive call,
an argument that shrinks fast, a base case at zero. It is also the cleanest
example of the tail recursion 8.3 discusses, which is why `variants.md` pairs
it with `ds-08-hanoi` rather than treating it as an outlier.

`meta.yml` records `in_book: false` so this does not get mistaken for a
sourced problem later.

## What this problem cannot enforce

It cannot check that the method is recursive. `while (b != 0) { int r = a % b;
a = b; b = r; }` passes everything. Same hole as `ds-08-palindrome`, and the
same answer: recursion is asked for in the constraints and assessed on the
exam.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` checks every
value against the bound before writing, which caught a hand-written case using
$2^{30}$ -- just over $10^9$.

`gen.py` also reports the deepest recursion each case forces, which is the
number to watch if the bounds are ever raised.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
