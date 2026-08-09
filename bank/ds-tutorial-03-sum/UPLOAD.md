# ds-tutorial-03-sum: upload checklist

Contest: `Data Structure`
URL: not yet published

## 1. Create the challenge

At `hackerrank.com/administration/challenges/create`, paste the files in
numeric order. The form fields map one-to-one onto the file numbers.

| Form field | File |
|---|---|
| Challenge name | `00. challenge-name.txt` |
| Description | `01. description.txt` |
| Problem Statement | `02. statement.md` |
| Input Format | `03. input-format.md` |
| Constraints | `04. constraints.md` |
| Output format | `05. output-format.md` |
| Tags | `06. tags.txt` |

`07. code-stub.java` is **not** entered into the form.

`04. constraints.md` uses LaTeX (`$1 \le N \le 100{,}000$`). Confirm it renders
as mathematics in the preview rather than as raw dollar signs.

## 2. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 15 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 is the one that carries the problem. It is three copies of
1,000,000,000, and an `int` accumulator prints **-1294967296** for it: a
negative answer out of three positive inputs, small enough to check by hand.
Leave it hidden and the student meets overflow only as an unexplained partial
score.

`testcases/SAMPLES` lists the case numbers to mark.

## 3. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 4. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 5. Publish

- [ ] **Publish** the challenge (a Draft does not appear in the contest)
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-tutorial-03-sum`
- [ ] **Max Score = 5**
- [ ] Place it third, after `ds-tutorial-02-echo`

## 6. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 7. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 5/5
- [ ] **Submit an `int` accumulator on purpose** and confirm the partial score
- [ ] **Submit the `Scanner` version and check the reported run time.** The
      statement tells students both methods fit at this size. If the grader is
      slower than this container and Scanner times out, that sentence is wrong
      and has to change.
- [ ] Confirm the LaTeX in Constraints renders

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Slowest case |
|---|---|---|
| BufferedReader + StringTokenizer, `long` sum (registered) | 15/15 | 222 ms |
| Scanner, `long` sum | 15/15 | 479 ms |
| BufferedReader, `int` sum (the intended mistake) | 9/15 | -- |

The `int` version fails 02, 07, 10, 11, 12 and 14.

Scanner runs about twice as slow as BufferedReader on the N = 100,000 cases but
stays comfortably inside the limit, which is what the statement claims. **That
claim is tied to N = 100,000.** Raising `N` in any future variation means
re-measuring before repeating the sentence.

Largest input file is about 1.0 MB (case 12).

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed, so the output is identical
every time. `gen.py` closes by simulating 32-bit wraparound over its own cases
and printing the score an `int` accumulator would earn, which should agree with
the table above.
