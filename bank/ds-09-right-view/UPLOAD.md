# ds-09-right-view: upload checklist

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
chapter 9 problems.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 is the one that must be public. It is the book's left-leaning tree,
where the answer is `1 2 3` and a solution walking down the right children
prints just `1`.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-09-right-view`
- [ ] **Max Score = 30**
- [ ] Place it third among the chapter 9 problems

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
| Level order with `levelSize` (registered) | 14/14 | -- |
| Walk down the right children only | 4/14 | 02 04 05 07 08 09 10 11 12 13 |
| Level order without separating the levels | 5/14 | 00 03 04 07 08 09 10 11 13 |
| The **first** node of each level (the left view) | 5/14 | same nine cases |
| Unmodified stub | 0/14 | all |

Reference timing: 314 to 366 ms.

## The misconception this problem is aimed at

Students picture the right side view as "follow the right children down", and
that is wrong as soon as a right child is missing while a left one is not.
**The visible node at a level is the rightmost node at that level, which need
not be a right child of anything.**

The book's own second example makes the point in three nodes: a tree leaning
entirely left, where the answer is `1 2 3` and nothing in it has a right child
at all. That is sample 02, and the right-children-only solution prints `1`.

## The one line that is the problem

```java
int levelSize = queue.size();
```

At the top of each round the queue holds exactly one level's nodes. Taking
that many out processes that level and nothing else, and whatever gets added
meanwhile belongs to the next round. Remove the line and the queue is a flat
stream with no boundaries -- which is what the "no level separation" variant
above does, scoring 5/14.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` asserts that the
view has exactly one entry per level of the tree, which is the cheapest check
that the level arithmetic is right.

Case 09 is a complete tree of 100,000 nodes: its last level alone holds 50,000
of them, so the queue reaches its widest there. Case 12 is the opposite -- a
left spine of 5,000 levels holding one node each, where the queue never holds
more than one node and no visible node is reachable by a right link.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
