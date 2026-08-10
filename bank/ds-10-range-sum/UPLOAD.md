# ds-10-range-sum: upload checklist

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

The Head is byte-identical to `ds-10-validate`'s.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 is six keys near $10^9$, so the total passes $5 \times 10^9$. An `int`
accumulator is wrong there and nothing else in the samples reveals it.

The test data is about 35 MB, most of it the four query-heavy cases.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-10-range-sum`
- [ ] **Max Score = 30**
- [ ] Place it third among the chapter 10 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 30/30
- [ ] Check the reported times; the reference is 620 to 840 ms on the large
      cases here, which is not a wide margin

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| Prune by the BST rule, `long` accumulator (registered) | 14/14 | -- |
| Full traversal per query | 10/14 | times out on 09 10 11 13 |
| Accumulating in an `int` | 9/14 | wrong on 02 09 10 12 13 |
| Pruning the wrong side | 2/14 | wrong on 12 cases |

Reference timing: 620 to 840 ms.

## Two things about the query design

**The queries have to be narrow.** A window covering most of the tree visits
most of it however it is written, so a random `low`/`high` pair over the whole
key range separates nothing. Cases 09 through 13 use windows holding a handful
of keys, which is where pruning is the difference between the height and the
whole tree. Case 11 goes furthest: every window falls strictly between two
consecutive keys and matches nothing at all, which is the cheapest possible
answer with pruning and a full traversal without it.

**Case 12 had to have its query count cut**, from 200,000 to 20,000. It is a
spine at the height cap, and on a spine every query costs the height whatever
the solution does -- 200,000 queries against a 5,000-deep tree is $10^9$ steps
for the **correct** solution, which measured 3.45 s. The point of that case is
the depth, not the query count.

That is the general trap with a query-heavy problem: raising `Q` punishes the
reference as fast as it punishes the mistake, and on the shapes where the
reference has no advantage it punishes it faster.

## Why the book's bound was raised

The book states this with **one** query, and a single query cannot punish a
full traversal: $O(n)$ once is fine. Pruning only pays when the same tree is
asked many times, so `Q` is the change that makes the problem a problem.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. The model answers each
query from a **sorted key array with prefix sums** rather than from a tree, so
it shares no code or reasoning with the solution -- and it doubles as the
answer to one of the exam questions in `variants.md`.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
