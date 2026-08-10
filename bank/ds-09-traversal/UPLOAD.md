# ds-09-traversal: upload checklist

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

The Head carries the `Node` class, the level-order parser and a `join` helper.
**The same Head is used by every chapter 9 problem**, which is deliberate: the
parser is not what any of them is about, and reusing it means the input format
has to be explained once for all five. If it is ever edited, edit it in all
five.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 is the tree from section 9.3's Check Your Understanding, so a student
can check against an answer they have already read.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-09-traversal`
- [ ] **Max Score = 10**
- [ ] Place it first among the chapter 9 problems

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
| The four traversals as written (registered) | 14/14 | -- |
| `inorder` with the visit placed first | 3/14 | 11 cases |
| `levelOrder` delegating to `preorder` | 6/14 | 00 02 07 08 09 10 11 13 |
| `postorder` stopping at leaves instead of checking for `null` | 4/14 | 10 cases |
| Unmodified stub | 0/14 | all |

Reference timing: 216 to 636 ms.

**Case 03 exists to keep the level-order mistake partial.** It is a tree of
three nodes -- a root with two children -- where preorder and level order
happen to give the same answer. A student who has not understood that they are
different traversals passes it and fails the rest, which is more informative
than failing everything.

## The height cap is load-bearing

The constraints allow 100,000 nodes but cap the **height at 5,000**. That is
not decoration: three of the four traversals are recursive, so the stack depth
is the height of the tree. A fully skewed tree of 100,000 nodes would overflow
the Java stack, and the solution that crashed would be the correct one.

Cases 11 and 12 sit exactly at the cap -- case 11 is a caterpillar (a long
spine with nodes hung off it) and case 12 is a plain right spine.

The cap is inherited from the Korean version. **If it is ever raised, the
recursive solutions have to be retested first**, not after.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. Trees are held as three
parallel arrays and every traversal in the model is iterative, so nothing in
the generator can hit Python's recursion limit.

`gen.py` asserts the node count, the value range and the height of every
generated tree, and prints the height of each case. That assertion caught a
mistake during construction: the caterpillar was built with a spine of 5,000
nodes, but every node hung off the spine sits one level below it, so the tree
came out 5,001 tall. The spine is now 4,999.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
