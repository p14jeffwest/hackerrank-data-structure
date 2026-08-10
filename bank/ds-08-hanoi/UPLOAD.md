# ds-08-hanoi: upload checklist

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

No code stub. The default Java template is what students should see.

## 2. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 (`N = 2`) is the one that earns its place. With a single disk the peg
roles never rotate, so a solution that mixes them up looks correct until here.
Two disks is the smallest input that uses the spare peg at all.

The test data is about 13 MB, nearly all of it case 13.

`testcases/SAMPLES` lists the case numbers to mark.

## 3. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 4. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 5. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-08-hanoi`
- [ ] **Max Score = 30**
- [ ] Place it second among the chapter 8 problems

## 6. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 7. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 30/30
- [ ] **Submit a `System.out.println`-per-move version and read the reported
      time.** See the note below; it passes here and might not there

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Fails on |
|---|---|---|
| The book's recursion with a `StringBuilder` (registered) | 14/14 | -- |
| `System.out.println` per move | **14/14** | passes; see below |
| Peg roles mixed up in the first recursive call | 2/14 | everything except N = 1 and N = 2 |
| Base case `n == 1` instead of `n == 0` | 0/14 | all |
| Move count printed as `2^n` | 0/14 | all |

Reference timing: 183 to 220 ms.

**The `println` mistake is not caught, and the numbers say why.** At `N = 20`
it takes 1.36 s writing to `/dev/null` and 2.40 s through a pipe, against
0.21 s for the reference -- six to eleven times slower, but probably still
inside a four-second limit.

Catching it would need `N = 22`, which quadruples the output to about 29 MB
per case. That was judged not worth it. The lesson belongs to
`ds-tutorial-03-sum`, which owns gathering output, and keeping `N = 20` keeps
this problem byte-identical in shape to the Korean one, which is the reason
for reusing it at all. If the live grader is slower and `println` does time
out, so much the better.

**The peg-rotation mistake is the real content of this problem.** It still
prints exactly `2^n - 1` lines, so the count comes out right and only the
moves are wrong. That is precisely why the move list is part of the answer
rather than just the total -- a problem asking only for the number of moves
would be answered by `(1 << n) - 1` with no recursion at all.

## Note on the test set

Regenerate with `python3 gen.py`. Nothing here is random; the answer for a
given `N` is unique.

**The reference model in `gen.py` is iterative, not recursive**, and that is
deliberate. `N = 20` means over a million frames, and Python's default
recursion limit is 1,000. The model walks an explicit stack holding the same
frames the recursion would, with a flag saying whether a frame has already
emitted its own move. Its output was checked against the Java solution at
`N = 3` and `N = 20`, byte for byte.

`gen.py` asserts that each case produces exactly `2^n - 1` moves.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
