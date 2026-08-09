# ds-04-majority: upload checklist

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

The Head is byte-identical to the one in `ds-04-rotate`: the complete
`Array_List`, including the three methods `ds-04-array-list` asks students to
write. Keep the two in step if either is ever edited.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-04-majority`
- [ ] **Max Score = 30**
- [ ] Place it third among the chapter 4 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 30/30
- [ ] **Submit a solution that sorts the list in place** and confirm the output
      reads `modified` rather than a wrong number. This is the one piece of
      driver behaviour students have not met before, and it needs to be
      legible when it fires
- [ ] Check the reported run time on the largest cases; the reference solution
      sits at 292 to 363 ms here

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| Boyer-Moore voting (registered) | 14/14 | -- |
| Count each element against every other, O(n^2) | 10/14 | times out on 08 10 12 13 |
| Voting loop that never replaces its candidate | 6/14 | wrong on 02 05 06 07 08 10 12 13 |
| Return the middle element without sorting | 6/14 | wrong on 00 through 07 |
| Insertion-sort in place, take the middle | 0/14 | `modified` on the small cases, times out on the rest |
| Voting loop comparing boxed `Integer` with `==` | 11/14 | wrong on 02 07 13 |
| Unmodified stub (returns 0) | 0/14 | all |

Reference timing: 292 to 363 ms on the five largest cases.

## What this problem does and does not enforce

**Boyer-Moore cannot be forced.** Sorting a copy is $O(n \log n)$ and passes.
Counting into a `HashMap` is $O(n)$ time and $O(n)$ space and passes. Neither
can be excluded by a time limit at this size.

What the problem does enforce is narrower and still worth having:

- $O(n^2)$ fails, which is the real difference between a 10-point and a
  30-point problem here.
- The input list must come back unchanged, checked by the driver. This closes
  the cheapest shortcut -- sort in place and take the middle -- and it is
  grounded in 4.1, where the ADT specifies that retrieval does not modify the
  list.

Constraints state $O(1)$ extra space as an expectation. It is not enforced, and
it should not be presented to students as if it were.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed, so the output is identical
every time. `gen.py` asserts that every generated list actually has a majority
element, which caught a hand-written case during construction:
`[5, 5, 1, 2]` has 2 of 4, and a majority needs strictly more than half.

**Two orderings, pulling in opposite directions.** Getting the case set right
took two rounds, and the reason is worth recording.

- An $O(n^2)$ solution returns as soon as it finds the answer. On a *shuffled*
  list the majority element turns up within an element or two, so the solution
  finishes in $O(n)$ and passes. Only when every filler element comes **first**
  does it pay the full quadratic cost. First round: the naive solution scored
  13/14.
- A voting loop comparing boxed `Integer`s with `==` never matches anything,
  so its counter sits at zero and it adopts nearly every element as the new
  candidate -- which means it ends holding **whatever came last**. Putting the
  filler first therefore hands it the right answer by luck. Second round: the
  boxed-`==` solution went *up* from 9/14 to 12/14.

So the two mistakes need opposite arrangements, and the case set now carries
both: `fillers_first` for cases 08, 10, 12 and 13's first list,
`majority_first` for 09, 11 and 13's second list. `build()` in `gen.py`
documents this.

There is also a parity trap. Case 09 ends with a *single* filler element, and
whether the broken `==` loop ends on it correctly comes down to whether the
number of preceding elements is even or odd. Do not rely on a one-element
tail; give the trailing filler some length.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
