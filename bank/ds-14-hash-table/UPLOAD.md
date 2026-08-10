# ds-14-hash-table: upload checklist

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

The Head builds the empty buckets and provides `bucketAt`, `tableSize` and the
`toString` that formats them. The four methods that touch the buckets are the
student's -- including `hash`, which is where the negative-key question lives.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 is negative keys. In Java `-7 % 10` is `-7`, and a negative index
throws. The book states the requirement explicitly and this is the only sample
that reaches it.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-14-hash-table`
- [ ] **Max Score = 30**
- [ ] Place it second among the chapter 14 problems

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
| Chaining, with the negative-key fix (registered) | 14/14 | -- |
| `hash` written as `key % size` | 8/14 | 02 05 09 10 11 13 |
| `put` appending instead of replacing | 10/14 | 03 09 10 13 |
| One entry per slot, overwriting on collision | 4/14 | 10 cases |
| Delegating to `java.util.HashMap` | **0/14** | every case |

Reference timing: 131 to 831 ms.

## The `print` command is what makes this a hash-table problem

A solution backed by `java.util.HashMap` answers **every `get` correctly** and
scores **0/14**, because it never fills the buckets. Without `print`, a
student could ignore the chaining entirely and the problem would be a map
problem wearing a hash table's name.

Same device as `ds-11-heap`'s `print`, and worth keeping for the same reason:
the chapter is about how the structure is built, and only its internals show
that.

## Case 12 had to be cut down, and the reason is instructive

Case 12's keys are all multiples of the table size, so **every one of them
lands in a single chain**. Each `put` then walks the whole chain, and the work
is quadratic **for the correct solution too**.

At the intended 200,000 commands that is 2 x 10^10 steps, and the reference
would have been the thing that timed out. It is now 4,000 commands -- 8 x 10^6
steps, 131 ms -- which makes the degenerate-load point without punishing
anybody.

The case that costs real time is **case 10**: 200,000 commands over 10 slots,
at 831 ms. That is a load factor of thousands and it is what section 14.5 is
about. It is the slowest case in the set and worth a glance on the live
grader.

## The `get` convention has a hole, deliberately

`get` returns `-1` for a missing key, so a stored value of `-1` is
indistinguishable from a miss. That is the book's convention, not an
oversight. Case 06 contains exactly that situation so a student meets it in
the test data rather than discovering it in an exam, and `variants.md` keeps
"what is wrong with this convention" as an exam question.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` asserts that no
case uses more than 20 `print` commands, which is the constraint students are
given.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
