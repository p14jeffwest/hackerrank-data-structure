# ds-10-balanced: upload checklist

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

The Head is not shared with the other chapter 10 problems: there is no
level-order parser here, because the tree is built rather than read, and the
helpers are a preorder printer and a height function.

The Tail uses `StreamTokenizer`. At 200,000 keys that is 200,001 numbers to
read, which is where it starts to matter.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 01 is six keys -- an **even** count. On an even range there are two
middles, both of which balance the tree, and only one of them is the required
root:

```
required            : 3 1 2 5 4 6   height 2
(lo + hi + 1) / 2   : 4 2 1 3 6 5   height 2
```

The heights are identical. Only the preorder separates them, and a student who
never sees this sample has no way to know which middle was wanted.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-10-balanced`
- [ ] **Max Score = 50** (but read the note below first)
- [ ] Place it fourth among the chapter 10 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 50/50
- [ ] Confirm the LaTeX in Constraints renders

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Fails on |
|---|---|---|
| `(lo + hi) / 2`, ranges passed as indices (registered) | 14/14 | -- |
| `(lo + hi + 1) / 2` | 5/14 | 01 02 05 06 07 10 11 12 13 |
| Keys inserted in order, producing a spine | 2/14 | 12 cases |
| Copying a `subList` per call | **14/14** | not a mistake -- see below |

Reference timing: 268 to 308 ms.

## This problem has no performance discrimination

That was measured rather than assumed. The obvious candidate for a slow
solution -- copying a subarray at every call instead of passing two indices --
was written and **passes everything**. The copying is $O(n)$ per level and
$O(n \log n)$ overall, not quadratic. It is wasteful, not wrong.

There is no natural quadratic mistake available here at all. Every plausible
way of writing this construction is $O(n)$ or $O(n \log n)$.

So what the problem tests is entirely **correctness**: the midpoint rule and
the recursion. **On that evidence this is a Medium sitting in a Hard slot**,
placed there because it is the chapter's Level 3 walkthrough rather than
because it is harder than `ds-10-validate`. Worth deciding deliberately rather
than by position.

If it should be a genuine Hard, the natural addition is a second part: after
building the tree, answer `Q` search queries reporting the number of
comparisons each takes. That exercises 10.4 -- the section on efficiency and
skew, which is otherwise untested in this chapter -- and makes the balanced
height mean something rather than just being printed.

## Why the two output lines

They check different things, and one alone is not enough.

- The **height** checks the book's stated requirement, that the tree is
  minimal in height.
- The **preorder** checks the shape.

A tree can have the right height and the wrong shape: the
`(lo + hi + 1) / 2` variant matches every height in the set and fails nine
preorders.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. The model builds the
preorder from an explicit stack of ranges, so it never recurses, and it
measures the height by walking those ranges rather than deriving it from a
formula -- the two would otherwise be able to agree by sharing one mistake.

`gen.py` asserts that the preorder is a permutation of the input and that
$2^{h+1} > n$, which is the condition for the height to be minimal.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
