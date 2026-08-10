# ds-10-validate: upload checklist

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

The Head is the chapter 9 one with two changes: the node field is `key` rather
than `data`, matching 10.1, and the `join` helper is gone because this problem
prints no lists. `ds-10-range-sum` uses the same Head.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Both 01 and 02 earn their places, and for different mistakes:

- **01** contains `Integer.MIN_VALUE` and `Integer.MAX_VALUE` as keys. Bounds
  held in an `int` have no value left to mean "no bound yet", so a root of
  `Integer.MIN_VALUE` is rejected by its own starting bound.
- **02** is three trees that are locally consistent at every parent-child pair
  and still invalid, because a node sits on the wrong side of a grandparent.
  Two of them are the book's own examples, from 10.1 item 2 and 10.1's Check
  Your Understanding.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-10-validate`
- [ ] **Max Score = 30**
- [ ] Place it second among the chapter 10 problems

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
| Range narrowed, `long` bounds (registered) | 14/14 | -- |
| Each node compared only against its parent | 8/14 | 02 06 08 10 11 13 |
| Bounds held in `int` | 12/14 | 01 03 |
| `<` and `>` so equal keys pass | 12/14 | 03 04 |

Reference timing: 317 to 389 ms.

## Building the counterexamples took two attempts

The whole problem rests on trees that are **locally consistent everywhere and
globally invalid**. Generating them is less obvious than it looks.

The first version of `break_one()` picked an arbitrary node in some left
subtree and raised its key above the grandparent. That node had children of
its own, and raising it above them broke a parent-child pair as well -- so the
parent-only check caught it, and the case stopped testing the thing it was
built for. The parent-only solution scored **11/14**.

`break_one()` now raises the **rightmost** node of the left subtree. By
construction that node is already above its own parent (it is that parent's
right child) and above its own left child, so raising it changes nothing
local. Only the ancestor's bound is broken. That took the parent-only solution
to **8/14**.

The lesson generalises: when a case is meant to isolate one property, check
that it has not accidentally broken a second one.

## A hidden failure made visible

The `int`-bounds mistake originally failed exactly one case, and that case was
hidden. A student would have seen 13/14 with nothing to look at.
`Integer.MIN_VALUE` and `Integer.MAX_VALUE` keys were added to sample 01, so
it now fails 01 and 03 and the reason is on screen.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. Trees are held as
parallel arrays and both the validity check and the height check are
iterative, so the generator cannot hit Python's recursion limit.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
