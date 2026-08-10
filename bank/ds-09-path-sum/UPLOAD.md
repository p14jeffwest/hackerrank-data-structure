# ds-09-path-sum: upload checklist

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

The Head is byte-identical to `ds-09-traversal`'s and shared by all five
chapter 9 problems. **The Tail is not** -- this is the only chapter 9 problem
that reads a second block of input (the queries), so its Tail differs.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 is the one that must be public. It is a chain of one-sided nodes with
values 1, 2, 3, 4, 5, and the targets are every partial sum along it:

```
targets   :  1      3      6      10     15    14     16
correct   :  false  false  false  false  true  false  false
wrong     :  true   true   true   true   true  false  false
```

Only 15, the full sum, is reachable -- the others require stopping short of
the leaf. A solution whose missing-child case answers `target == 0` says true
to all four.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-09-path-sum`
- [ ] **Max Score = 30**
- [ ] Place it fifth among the chapter 9 problems

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
| Carry the remainder down, test at the leaf (registered) | 14/14 | -- |
| Missing child answering `target == 0` | 7/14 | 00 02 03 05 06 07 12 |
| Leaf testing `target == 0` instead of `target == node.data` | 1/14 | 13 cases |
| Abandoning a branch once the remainder goes negative | 9/14 | 08 09 11 12 13 |

Reference timing: 161 to 931 ms.

## The mistake this problem is built around

```java
if (node == null) return target == 0;   // reads fine, is wrong
```

It looks like a proper base case and it quietly lets a path stop at a node
that still has one child. The statement says a path ends at a **leaf**, and
this version does not enforce that.

The correct arrangement puts the leaf test **before** the recursion:

```java
if (node == null) return false;
if (node.left == null && node.right == null) return target == node.data;
```

Case 02 exists for this and nothing else.

## Why case 10 uses only positive values

The prune-on-negative mistake -- stop descending once the remainder goes below
zero -- is **correct** when every value is positive, and this problem allows
values down to -1,000. Case 10 is built entirely from positive values so that
mistake passes it, which turns a total failure into a 9/14 and tells the
student which half of the input broke them.

## Note on the cost

Each query re-walks the tree, so `Q` queries cost $O(nQ)$, which is $10^8$ at
the limits and runs in about 900 ms. That is why `Q` is capped at 1,000 rather
than raised further. A student who collects every path sum into a set once and
answers the queries by lookup is doing better than the reference, and should
be told so rather than marked down.

## Why this problem is here at all

**This book's chapter 9 has no path-sum problem** -- its Level 3 walkthrough
is the diameter, which is `ds-09-diameter`. Path sum was added at the
instructor's request so that the two courses share one more problem, the same
reasoning as `ds-08-gcd`. `meta.yml` records `in_book: false` so this is not
mistaken for a sourced problem later.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` computes the set
of every root-to-leaf sum iteratively and answers the queries from it, so the
model shares no code with the recursive solution. Targets are drawn half from
sums that exist and half from sums that do not, so a solution that always
answers one way scores about half.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
