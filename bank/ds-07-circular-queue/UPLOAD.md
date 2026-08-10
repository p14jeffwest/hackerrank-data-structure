# ds-07-circular-queue: upload checklist

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

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 is the one that must be public. It is the only sample where the ring
wraps, and a solution missing the modulo passes 00 and 01 and then prints
`crash` here. Publish only the first two and the student sees a partial score
with no clue which part is wrong.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-07-circular-queue`
- [ ] **Max Score = 10**
- [ ] Place it first among the chapter 7 problems

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
| Reference implementation | 14/14 | -- |
| `rear` computed without `% capacity` | 7/14 | 02 06 07 08 10 12 13 |
| `front` advanced without `% capacity` | 7/14 | 02 04 05 07 08 10 13 |
| `enqueue` without `count++` | 0/14 | all |
| `enqueue` without the `isFull` check | 8/14 | 03 04 07 08 10 13 |
| `dequeue` and `getFront` without the `isEmpty` checks | 8/14 | 01 08 09 10 11 13 |
| Unmodified stub | 0/14 | all |

Reference timing at Q = 200,000: 284 to 350 ms.

The two missing-modulo mistakes both score 7/14 but fail different sets of
cases, so the score still says something. Seven cases -- 00, 01, 03, 04, 05,
09 and 11 -- never need a wrap, which is what keeps those mistakes partial.
`gen.py` reports, for each case, how many enqueues would run off the array
without the modulo; that number is what to check when editing the data.

**The missing `isFull` check is the quietest of the five.** It does not crash:
`enqueue` simply overwrites the front element, and the queue carries on
answering with the wrong contents. Only `size`, `full` and the values give it
away.

## Where this differs from the Korean version

The two problems are deliberately the same, so that one explanation covers
both courses. The command set matches. The boundary behaviour does not,
because the two books do not agree:

| Situation | Korean book (6.2) | This book (7.3) |
|---|---|---|
| `enqueue` on a full queue | does nothing, no output | throws; driver prints `full` |
| `dequeue` / `peek` on empty | prints `-1` | returns `null`; driver prints `empty` |

Each version follows its own book. Worth knowing before teaching the two
sections from the same slide.

The `crash` line is carried over from `ds-06-array-stack`, for the same
reason: `IndexOutOfBoundsException` is a `RuntimeException`, so without a
separate catch a solution that runs off the array would have its error quietly
reported as a full queue.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
