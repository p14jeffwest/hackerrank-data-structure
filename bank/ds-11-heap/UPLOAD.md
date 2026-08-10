# ds-11-heap: upload checklist

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

The Head gives the array and the index arithmetic (`parent`, `left`, `right`)
but not the two movements. That split is deliberate: index arithmetic is
bookkeeping, and up-heap and down-heap are the chapter.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Samples 00 and 01 are the answers to **11.5 Level 1 Problems 1 and 2**, the
traces students are asked to do by hand. They can be told to check their
pencil work against them.

Case 02 is the down-heap example of 11.3: the root's children are 4 and 6, and
swapping with 6 instead of 4 leaves an array that is broken but still pops a
plausible value next time.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-11-heap`
- [ ] **Max Score = 30**
- [ ] Place it first among the chapter 11 problems

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
| The book's up-heap and down-heap (registered) | 14/14 | -- |
| Down-heap swapping with the **larger** child | 4/14 | 10 cases |
| `pop` removing the root by shifting the array left | 5/14 | 7 cases wrong, 10 and 13 time out |

Reference timing: 405 to 877 ms.

## Why `print` exists, and why the prints are spread out

A heap is not determined by the values it holds -- many arrays satisfy the
heap condition over the same numbers. Printing only the popped values would
let **any** correct priority queue pass, and would not check that the two
algorithms of 11.3 were the ones written.

`print` shows the array, which pins the algorithms down. It also makes the
Level 1 traces of 11.5 checkable directly, which is what those exercises ask
students to produce by hand.

The prints are **spread through** the large cases rather than left at the end,
and that was a deliberate change. `java.util.PriorityQueue` performs the same
sift-up as the book, so after a run of pushes its array agrees with the
book's; the layouts only diverge after removals, because its sift-down
differs. One print at the end catches that far less often than ten spread
through the run.

## Two variants that were tried and are not in the table

**Overwriting the root before detaching the last element** turned out to be
**correct**, not wrong. Setting index 0 to the last value and then removing
the last is the same operation in the other order. If a student writes it that
way, it is fine.

**A `PriorityQueue`-backed solution** is not representative and was dropped.
To answer `print` at all it has to maintain the visible array itself, which
made the variant $O(n)$ per operation and timed it out for a reason unrelated
to the mistake. The real point stands: `PriorityQueue` cannot reproduce these
arrays once removals are involved.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. The model is the book's
two algorithms on a plain Python list.

`gen.py` asserts that no case uses more than 20 `print` commands, which is the
constraint students are given. Case 13 had to have its command count trimmed
when the spread-out prints were added -- pushes plus pops plus prints had
crossed 200,000, and the assertion caught it.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
