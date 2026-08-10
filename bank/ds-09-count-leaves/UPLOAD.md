# ds-09-count-leaves: upload checklist

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

The Head is byte-identical to `ds-09-traversal`'s. All five chapter 9 problems
share it; edit one and edit all five.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Both 01 and 02 earn their places:

- **01** is a single node, the smallest place the two height conventions part
  company (0 edges against 1 node), and where a `height(null)` of 0 instead of
  -1 shows at once.
- **02** has one-sided nodes with real subtrees under them. A solution that
  counts a node with one child as a leaf reports 2 instead of 4.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-09-count-leaves`
- [ ] **Max Score = 10**
- [ ] Place it second among the chapter 9 problems

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
| The three methods as written (registered) | 14/14 | -- |
| A node with one child counted as a leaf | 11/14 | 02 10 13 |
| `height(null)` returning 0 instead of -1 | 0/14 | all |
| `maxDepth` delegating to `height` | 0/14 | all |

Reference timing: 120 to 368 ms.

## A sample that had to be rebuilt

The one-sided-node trap is the point of this problem, and the obvious test for
it does not work.

A **zigzag** -- every node with exactly one child, alternating sides -- looks
like the ideal case. It is not: such a tree has exactly **one** leaf, and a
solution that stops at the first one-sided node also reports **one**. It
passes by accident, and the first version of case 02 was exactly that.

Case 02 is now a tree where each one-sided node leads to a subtree with
several leaves:

```
        1
       / \
      2   5
     /     \
    3       6
   / \     / \
  4   7   8   9
```

Four leaves; the wrong solution reports two.

The zigzag is still in the set as case 12, where it does a different job --
maximum height with a single leaf.

**The general lesson**: when a wrong answer and a right answer can coincide by
arithmetic accident, check the case actually separates them rather than
assuming the shape looks convincing.

## Why there are three answers and not two

The Korean counterpart asks for the leaf count and the height in edges. This
book uses both conventions: 9.1 counts edges, 9.5 Problem 1 counts nodes, and
9.5's own answer page adds that they differ by one and the problem's
definition has to be checked.

Asking for both turns that warning into something a student has to act on. It
also keeps the Korean answer -- the edge count -- present, so the two courses
still share a number.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` asserts, for
every case, that the node-count depth is exactly one more than the edge-count
height, which is a cheap way to catch a mistake in either measurement.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
