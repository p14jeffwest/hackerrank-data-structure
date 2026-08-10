# ds-05-linked-list: upload checklist

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

The Tail is `ds-04-array-list`'s Tail with `Array_List` renamed to
`LinkedList`. Keeping the driver identical is deliberate: the two problems are
meant to be read against each other. If either driver is edited, edit both.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 00 ends on `addAt 3 99` against a three-node list, which appends here and
was an `error` in `ds-04-array-list`. Publishing it is what stops a student
from carrying the array version's bound over by reflex.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-05-linked-list`
- [ ] **Max Score = 10**
- [ ] Place it first among the chapter 5 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] **Submit the stub untouched.** It compiles and scores 0/14
- [ ] **Submit a version with the two splice lines swapped.** It should hang
      and be reported as a timeout, not a crash. Worth seeing once, because it
      is the mistake the book's own TIP singles out and the failure mode is
      counter-intuitive
- [ ] Confirm the LaTeX in Constraints renders

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Fails on |
|---|---|---|
| Reference implementation | 14/14 | -- |
| Splice lines swapped | 6/14 | wrong on 00 06, **times out** on 08 through 13 |
| `tail` not moved back on removing the last node | 11/14 | 04 10 11 |
| `indexOf` using `==` | 9/14 | 02 09 11 12 13 |
| `remove(int)` without `numberOfEntries--` | 5/14 | 01 04 06 08 through 13 |
| Array version's bound, rejecting `i == size` | 10/14 | 00 01 07 13 |
| Unmodified stub | 0/14 | all |

Reference timing at Q = 10,000: 162 to 269 ms.

**The swapped splice does not crash.** Assigning `prev.next = node` before
reading `prev.next` leaves `node.next` pointing at `node` itself, so the list
grows a one-node cycle and `toString` never terminates. That is why it appears
as a timeout on the large cases and merely as a wrong answer on the two small
ones that happen not to print afterwards.

## Why Q is 10,000 here and 20,000 in chapter 4

Measured on the same command mix, this implementation runs:

| Q | Linked | Array (ch04) |
|---|---|---|
| 10,000 | 202 ms | -- |
| 20,000 | 397 ms | 244 to 303 ms |
| 40,000 | 1007 ms | -- |

`addAt`, `removeAt` and `get` all walk from `head`, so the cost grows
quadratically while the array version's stays close to linear. Halving Q buys
back the wall time.

This is worth stating rather than hiding: it is 4.3's comparison table
measured on a real workload, and `variants.md` reserves the comparison as this
problem's best exam question.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` carries a Python
model of the driver, and **the model encodes two different bounds** -- `addAt`
accepts `0 <= i <= size` while `removeAt` and `get` accept `0 <= i < size`. If
either the Tail or the model is changed, change both.

Case 04 exists for one mistake only: remove the last node, then append. A
missing `tail` update is invisible until that append lands on a node that has
already left the list.

As in `ds-04-array-list`, the generator aims 80% of its `indexOf` and
`removeValue` queries at values it actually inserted. Querying at random over
a range up to $10^9$ would make `indexOf` return `-1` either way and let the
`==` mistake through.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
