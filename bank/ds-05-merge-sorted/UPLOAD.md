# ds-05-merge-sorted: upload checklist

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

The Tail is longer than usual because it carries the enforcement. It puts every
node it builds into an `IdentityHashMap`, and after the call walks the returned
list checking three things: every node was one it handed over, no node appears
twice, and the count still matches `n + m`. Any failure prints `invalid`.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 is the one that must be public. It is nothing but the empty cases, and
a solution that picks its first node by comparing `head1.data` with
`head2.data` throws the moment either list is empty.

**The input contains blank lines**, one for every list of length 0. Confirm
after upload that they survived: an editor or a paste step that strips trailing
blank lines will shift every subsequent test case and the problem will look
broken for reasons unrelated to anything the student did.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-05-merge-sorted`
- [ ] **Max Score = 30**
- [ ] Place it third among the chapter 5 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 30/30
- [ ] **Submit an array-and-rebuild solution on purpose.** The values will be
      perfectly correct and every line should come back `invalid`. This is the
      one piece of driver behaviour students have not met before, and it needs
      to read clearly when it fires
- [ ] Confirm the blank lines in the sample input display correctly
- [ ] Check the run time; the reference sits at 511 to 613 ms here, the
      slowest of any problem so far

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| Dummy head, relinking (registered) | 14/14 | -- |
| Array, sort, rebuild with new nodes | 0/14 | every line `invalid` |
| Forgets to attach the leftover tail | 0/14 | every line `invalid`, nodes lost |
| No dummy; first node chosen by comparison | 9/14 | throws on 00 02 06 08 12 |
| Insert each node by scanning, O(n*m) | 9/14 | times out on 09 through 13 |
| Unmodified stub | 0/14 | all |

Reference timing: 511 to 613 ms on the four largest cases. Higher than the
other problems, and worth watching on the live grader -- the `IdentityHashMap`
bookkeeping in the driver is part of that cost and it is paid by every
submission, correct or not.

## What the identity check buys

This is the main reason to keep both this problem and the Korean
`dsa-07-merge-sorted` rather than treating them as duplicates. There, "do not
create new nodes" sits in the constraints as an honour rule. Here it is
checked, and the difference is not theoretical: the array-and-rebuild solution
prints a perfectly correct sequence of values and scores zero.

Two things the check deliberately does not do:

- **The dummy node is not flagged.** It never appears in the returned list, so
  it never reaches the check. The rule is about the nodes in the answer, not
  about allocation.
- **`<` versus `<=` is not detected.** Choosing the wrong one swaps two nodes
  carrying the same number, and the printed values are identical either way.
  The distinction is real -- it is what stability means -- but no output test
  can see it. `variants.md` reserves it as an exam question.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` asserts that both
lists of every case are actually sorted before writing them, which is the kind
of mistake that would otherwise surface as an unexplainable wrong answer.

Case 13 is two lists of 100,000 identical values, so every comparison is a tie
and the merge never skips ahead. It is the worst case for the comparison count
and the best check that ties are handled without looping.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
