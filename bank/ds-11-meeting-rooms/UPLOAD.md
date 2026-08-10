# ds-11-meeting-rooms: upload checklist

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

The Tail uses `StreamTokenizer`: 200,000 meetings is 400,000 numbers.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 is the one that must be public. Five meetings laid end to start need
**one** room, and a solution that reuses a room only when its end time is
strictly before the next start asks for five:

```
correct : 1 1 2
strict  : 2 2 3
```

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-11-meeting-rooms`
- [ ] **Max Score = 30**
- [ ] Place it second among the chapter 11 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 30/30
- [ ] Confirm the LaTeX in Constraints renders

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| Sort by start, min-heap of end times (registered) | 14/14 | -- |
| Count overlaps pairwise, O(n^2) | 10/14 | times out on 09 10 11 12 |
| Reuse only when the end is strictly before the start | 7/14 | wrong on 02 06 07 08 10 12 13 |
| Not sorting by start time | 6/14 | wrong on 00 03 05 08 09 10 12 13 |

Reference timing: 241 to 600 ms.

## This is NOT the Korean meeting-rooms problem

`dsa-13-meeting-rooms` has the same name and asks a different question:

| | Question | Method |
|---|---|---|
| Korean, chapter 13 | most meetings that fit in **one room** | greedy, sorted by end time |
| This one, chapter 11 | fewest **rooms** for all meetings | sorted by start time, min-heap |

The Korean version uses no heap at all, which is why it lives in that book's
sorting chapter. Nothing is shared -- not the statement, not the data, not the
answer.

**This is worth flagging when teaching both sections.** Two problems with one
name and two different answers is exactly the sort of thing that produces a
confused lecture. `variants.md` reserves the one-room greedy question for the
Korean exams so the two do not meet on a single paper either.

## One thing about the reference worth knowing before marking

The book's code removes **at most one** finished meeting per step and returns
the heap's **final size**. That works because the heap then never shrinks, so
its final size is the largest it ever reached.

A student who instead drains **every** finished meeting at each step has a
heap that does shrink, and must track the maximum separately. That solution is
also correct and looks quite different. Do not mark it down for not matching
the book.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. The model answers by
sweeping the endpoints -- `+1` at a start, `-1` at an end, processing ends
first at equal times -- so it shares no reasoning with the heap solution, and
the "ends first" ordering is the sweep's way of saying that meetings meeting
end to start do not overlap.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
