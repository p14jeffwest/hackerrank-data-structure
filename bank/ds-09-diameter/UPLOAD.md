# ds-09-diameter: upload checklist

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

Case 02 is the one that must be public: a tree whose longest path never
touches the root, where a root-only solution answers 5 instead of 6.

The test data is about 12 MB, most of it cases 11 and 13.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-09-diameter`
- [ ] **Max Score = 50**
- [ ] Place it fourth among the chapter 9 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 50/50
- [ ] **Submit the naive version -- height at every node -- and read the
      score.** It should be 11/14. Read the timing note below first

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| One pass, returning height and updating a field (registered) | 14/14 | -- |
| `height(left) + height(right)` at every node | 11/14 | times out on 13, overflows the stack on 09 and 12 |
| Measuring only through the root | 11/14 | wrong on 02 08 12 |
| Empty subtree reported as 0 (counting nodes) | 0/14 | all |
| Unmodified stub | 1/14 | returns 0, right for the single-node case |

Reference timing: 116 to 624 ms.

## Why the node cap is 500,000 here and 100,000 elsewhere

The naive solution costs roughly **(number of nodes) x (height)**, not
$O(n^2)$, and that distinction decided the bounds. It took three rounds to
get right:

| Attempt | Largest case | Naive time | Reference |
|---|---|---|---|
| deep but small (5,000-node spine) | -- | stack overflow | 0.12 s |
| large but shallow (100,000 nodes, height 17) | -- | 0.30 s | 0.31 s |
| large **and** deep (100,000 nodes, height 4,000) | -- | 1.58 s | 0.34 s |
| large and deep at 500,000 nodes | case 13 | **5.41 s** | 0.63 s |

Only a tree that is large **and** deep at once pays the full bill, because
each of the other shapes keeps one factor down. Case 13 is a caterpillar: a
spine of 4,900 nodes with a small shallow bush hung off each, filling the tree
to the node cap while the height stays just under the 5,000 cap.

At 100,000 nodes the naive solution finished in 1.6 seconds and would have
passed. That is why this problem alone goes to 500,000.

## The naive solution also overflows the stack, and that is not enough

On cases 09 and 12 -- deep trees -- the naive version dies with a
`StackOverflowError` rather than a timeout, because it nests a `height`
recursion inside a `diameter` recursion and the two depths add. That is a real
failure, but a marginal one: the total is about 5,001 frames against the
reference's 5,000, so it sits right on the edge of whatever stack the grader
provides.

**Do not rely on it.** Case 13 is what catches the naive solution properly,
and it does so on time with an eightfold margin.

It is also worth noticing what this says about the reference: it recurses
5,000 deep on the deep cases and passes here. If the grader's stack turns out
to be smaller, the height cap has to come down for all five chapter 9
problems, not just this one.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. Everything in the model
is iterative -- the trees are three parallel arrays and the diameter is
computed over a post-order index list -- so nothing in the generator can hit
Python's recursion limit.

`gen.py` asserts the node count, the height cap, and that the diameter is
between 0 and twice the height.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
