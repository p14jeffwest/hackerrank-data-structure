# ds-tutorial-02-echo: upload checklist

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

`07. code-stub.java` is **not** entered into the form. It is a copy of the
default template HackerRank supplies for Java problems, kept for reference.

## 2. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 13 cases)
- [ ] **Mark cases 00 and 01 as samples**

Publishing 01 matters more than usual here. It is the sample that contains
spaces, and it is the only thing that lets a student notice the `next()`
problem before submitting. Publish only 00 and the whole design of the problem
is lost.

`testcases/SAMPLES` lists the case numbers to mark.

## 3. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 4. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 5. Publish

- [ ] **Publish** the challenge (a Draft does not appear in the contest)
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-tutorial-02-echo`
- [ ] **Max Score = 5**
- [ ] Place it second, after `ds-tutorial-01-hello`

## 6. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 7. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 5/5
- [ ] **Submit a `Scanner.next()` solution on purpose** and confirm the score
      comes back partial rather than zero -- this is the whole point of the
      problem, and it is worth seeing the number yourself
- [ ] Confirm case 12 (1000 characters) is not truncated in the sample display

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result |
|---|---|
| `BufferedReader.readLine()` (the registered solution) | 13/13 |
| `Scanner.nextLine()` | 13/13 |
| `Scanner.next()` (the intended mistake) | 4/13, failing 01 03 05 06 07 08 09 11 12 |

The four cases `next()` survives are 00, 02, 04 and 10, the ones with no space
in them.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.

## Note on the test set

Regenerate with `python3 gen.py`. The case list is fixed rather than random, so
the output is identical every time, and `gen.py` prints the expected `next()`
score as a self-check.
