# ds-13-counting-sort: upload checklist

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

The Tail reads bytes directly rather than using `StreamTokenizer`. With a
million values the reading is a real part of the runtime, and it should not be
what a student's score depends on. All values are non-negative, which is why
the reader can be that short.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 contains `maxValue` itself. A count array sized `maxValue` instead of
`maxValue + 1` runs off the end there, and nothing else in the samples reaches
that value.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-13-counting-sort`
- [ ] **Max Score = 10**
- [ ] Place it second among the chapter 13 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 10/10
- [ ] Confirm the LaTeX in Constraints renders

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Note |
|---|---|---|
| Count, prefix sum, place from the back (registered) | 14/14 | -- |
| Count array sized `maxValue` | 0/14 | runs off the end wherever `maxValue` occurs |
| Placing from the front | **14/14** | still correct here -- see below |
| No prefix sum, emitting each value `count[v]` times | **14/14** | the other correct way to write it |
| `Arrays.sort` | **14/14** | not excluded -- see below |

Reference timing: 278 to 371 ms.

## Counting sort cannot be enforced by time

Measured on this container:

| Input | Counting sort | `Arrays.sort` |
|---|---|---|
| case 11 (n = 10^6, k = 10^6) | 371 ms | 565 ms |
| case 12 (n = 10^6, k = 10^3) | 278 ms | 418 ms |
| case 13 (10^6 identical values) | 364 ms | **354 ms** |
| probe: n = 5x10^6, k = 10^6 | 1219 ms | 1972 ms |

Counting sort is about 1.5 times faster, and on case 13 the library sort is
faster still -- it detects the constant run. **Nowhere near a factor a time
limit could turn into a pass or a fail.**

Raising `n` does not fix it. At 5,000,000 both finish inside two seconds and
the input file alone is 34 MB. `n` is therefore capped at 1,000,000: a larger
one costs megabytes and buys nothing. The requirement is stated in the
constraints and assessed on the exam, the same position as `ds-13-merge-two`.

## Placing from the front is not marked wrong

It scores 14/14, and correctly so. Placing from the back is what makes the
sort **stable**, and for plain `int`s there is nothing for stability to
preserve -- equal values are indistinguishable.

It matters in 13.5, where radix sort sorts one digit at a time and needs each
pass to leave the previous digit's order intact. That is 13.5's own Check Your
Understanding, and `variants.md` reserves it as the English section's exam
axis rather than pretending this problem can test it.

The registered solution places from the back anyway, and its comments say why,
so a student reading the answer afterwards sees the reason.

## Deviation from the book

13.7 Level 2 Problem 2 restricts the values to 0, 1 and 2, where a counting
sort collapses into counting three things and the prefix sum never appears.
The range was widened to 0..10^6 so the count array, the prefix sum and the
placement pass are all genuinely needed -- which is what 13.4 describes and
what 13.5 reuses. Agreed with the instructor before building.

The same 0/1/2 array is also 12.7 Level 3 Problem 6, the Dutch National Flag
problem, which was not made into a contest problem. That one wants three
pointers and $O(1)$ space; this one wants counting. Same input, different
method, so they do not collide -- and `variants.md` keeps the flag version as
exam material.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` asserts that no
value exceeds `maxValue`, which would otherwise make a correct solution crash
on an input that is itself wrong.

Case 09 is the shape where counting sort is at its worst: 50 values spread
over a range of a million, so the count array dwarfs the input. It is there to
be pointed at, not to fail anyone.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
