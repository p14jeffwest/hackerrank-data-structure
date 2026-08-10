# ds-11-median-stream: upload checklist

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

The Head declares the two heaps already facing the right way -- `lower` with
`Collections.reverseOrder()`, `upper` with the default. That makes "use two
heaps" the shape of the code rather than a rule to remember, the same choice
as `ds-06-queue-two-stacks`, and it leaves the balancing as the problem.

**The Tail formats with `String.format(Locale.ROOT, "%.1f", ...)`.** The
`Locale.ROOT` is load-bearing: under a locale that uses a decimal comma the
same call prints `1,5`, and every median would be marked wrong for a reason no
student could diagnose. Do not remove it.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 is a strictly increasing stream with a median after every arrival.
Every new value belongs to the larger half, so a solution that skips the
rebalancing step drifts immediately.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-11-median-stream`
- [ ] **Max Score = 50**
- [ ] Place it fourth among the chapter 11 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 50/50
- [ ] **Check that a median prints as `1.5` and not `1,5`.** If it does not,
      the `Locale.ROOT` has been lost somewhere
- [ ] Check the reported times; the reference is 785 to 929 ms here

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| Two heaps, rebalanced after every add (registered) | 14/14 | -- |
| Keep everything, sort a copy on each query | 9/14 | times out on 09 through 13 |
| No rebalancing after the cross-over move | 0/14 | reads an empty heap and throws |
| Halving the two middles with `int` arithmetic | 3/14 | wrong on 11 cases |
| Reading the median from the larger heap when the count is odd | 1/14 | wrong on 13 cases |

Reference timing: 785 to 929 ms.

## A variant that had to be rewritten

The sort-on-each-query solution first scored **0/14**, and that was a fault in
the variant rather than a finding. It kept its own `ArrayList` and never
touched the provided heaps, so the Head's `size()` -- which reports
`lower.size() + upper.size()` -- stayed at zero and the driver printed `empty`
for every query. The variant now pushes into `lower` so `size()` is right, and
it scores 9/14, timing out exactly where it should.

Worth remembering when writing wrong-answer variants against a stub: the
variant has to be a solution a student could plausibly submit, which means it
has to keep whatever state the provided code reads.

## The no-rebalancing mistake fails totally, not partially

Without the corrective move, `addNum` pushes into `lower` and immediately
moves that value to `upper`, so `lower` is always empty and `upper` holds
everything. `findMedian` then reads `lower.peek()` on an empty heap and
throws. It scores 0/14.

That is unusual for this set -- most mistakes here are arranged to score
partially -- but it is diagnosed by sample 00 on the first submission, so it
was left alone.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. The model keeps a sorted
list and answers by index, which shares nothing with the two-heap method.

**The model formats from integers, not from a double.** It works out twice the
median as a long and decides between `.0` and `.5` from its parity. The
doubles in this problem are in fact exact -- two values of at most $10^9$ sum
to at most $2 \times 10^9$, comfortably inside what a double represents
exactly -- but formatting the expected output from a double would let the
model and the solution agree by sharing a rounding assumption rather than by
both being right.

The integer formatting also handles the sign correctly. A naive `sum / 2`
prints `0.5` for a median of `-0.5`; case 05 contains exactly that.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
