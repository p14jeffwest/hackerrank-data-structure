# ds-06-queue-two-stacks: upload checklist

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

The Head carries a complete `ArrayStack` -- the class `ds-06-array-stack` asks
students to finish -- and then opens `StackQueue` with its two stack fields
already declared. That declaration is the point: "use only stacks" is the
shape of the code rather than a rule the student has to remember.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01, 02 and 03 as samples** (four, not the usual three)

Case 03 earns the fourth slot. It is nine commands, and it is the only sample
where refilling the outbox unconditionally gives a different answer: the
expected output is `1 2 3 9` and that solution prints `1 9 2 3`, with the
later element overtaking two earlier ones.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-06-queue-two-stacks`
- [ ] **Max Score = 50**
- [ ] Place it fourth among the chapter 6 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 50/50
- [ ] **Submit the "move everything back afterwards" version.** Every answer
      it produces is correct and it should still score 9/14. That is the whole
      point of the problem and it is worth seeing the number

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| Refill only when the outbox is empty (registered) | 14/14 | -- |
| Refill on every dequeue | 5/14 | wrong order on 00 03 04 07 08 10 11 12 13 |
| Refill, take one, move everything back | 9/14 | correct answers; times out on 09 through 13 |
| `isEmpty` checks the outbox only | 9/14 | wrong on 02 04 07 12 13 |
| Pop the outbox without ever refilling | 0/14 | all |
| Unmodified stub | 0/14 | all |

Reference timing: 308 to 342 ms on the five largest cases.

## The two mistakes are worth telling apart

**Move everything back afterwards** produces correct output on every case. It
fails only on time, and only on the five large ones. This is the clearest
demonstration anywhere in this set that being right and being affordable are
separate questions, and it is why the problem is worth 50 points rather than
30.

**Refill on every dequeue** fails for a second reason that is easier to
diagnose and more instructive: pouring the inbox onto a non-empty outbox
buries older elements under newer ones. The order breaks as soon as an enqueue
lands between two dequeues. Case 03 shows it in nine commands.

A student who finds only the timing problem has not understood the design.
`variants.md` reserves "what goes wrong if you refill every time -- give both
answers" as an exam question for exactly this reason.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` reports the
maximum queue depth of each case, which is what decides whether a per-dequeue
sweep can survive it.

The large cases hold the queue deep on purpose. Case 09 fills to 100,000 and
then drains, so the second half runs against the deepest possible queue; case
10 alternates one dequeue with one enqueue after filling, so the depth never
drops at all. A case that merely has many commands but a shallow queue -- case
06, where the depth never exceeds 1 -- catches none of the timing mistakes,
and it is in the set for the opposite reason: it forces a refill decision on
nearly every call.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
