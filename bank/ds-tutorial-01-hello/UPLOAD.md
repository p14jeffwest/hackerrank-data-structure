# ds-tutorial-01-hello: upload checklist

Contest: `Data Structure` (slug not yet assigned)
URL: not yet published

This is the first problem of the English set, so this checklist doubles as the
template every later problem reuses.

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
default template HackerRank supplies for Java problems, kept here for
reference.

## 2. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders)
- [ ] **Mark case 00 as a sample**. Miss this and students have nothing to see
      when they press Compile and Test

`testcases/SAMPLES` lists the case numbers to mark.

## 3. Language settings

- [ ] **Keep Java 15 only; clear every other language**

See the note in `meta.yml`: the Korean repo's `tutorial-01` still records
java17 because it predates the discovery that the grader tops out at 15.
Check what the Languages tab actually offers. If 17 is available, update
`meta.yml` and this line together, and revisit whether the Korean repo's
ban on `record` is still necessary.

## 4. Register the solution

- [ ] Upload `Solution.java` under Upload solution

Students can then see the expected output for their own custom input, which
cuts down on debugging questions.

## 5. Publish

- [ ] **Publish** the challenge (a Draft does not appear in the contest)
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-tutorial-01-hello`
- [ ] **Max Score = 5**
- [ ] Place it first, ahead of `ds-tutorial-02-echo` and `-03-sum`

## 6. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 7. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm the statement renders correctly (tables, code blocks, headings)
- [ ] Confirm a correct submission actually scores 5/5
- [ ] Submit `public class Main` on purpose and read the error message
- [ ] **Submit a non-ASCII comment on purpose and read the error message**
      (this one is unverified; see below)

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings. Ran against the single test case and matched byte for
byte (13 bytes, trailing `\n` included).

Every file in this directory is pure ASCII, not only the `.java` files. The
markdown fields are pasted into a web form rather than compiled, so nothing
would break either way, but two things argue for the rule. Text that survives a
copy-paste unchanged cannot be corrupted by an encoding mismatch on the way in,
and a statement that tells students to avoid em dashes should not itself be
full of them. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

| Submission | Result |
|---|---|
| `Solution.java` | 1/1 |
| Default template, unmodified | 0/1, prints nothing |
| Same code with the class renamed `Main` | fails to load; no `Solution` class |

**Open item.** The statement warns that non-ASCII characters in the source can
break compilation. That could not be reproduced locally: JDK 18 and later
default to UTF-8 (JEP 400), so the unmappable-character error does not appear
on JDK 21 even when `-encoding US-ASCII` is passed. The corresponding checkbox
in the Korean repo's `UPLOAD.md` was also left unchecked, so the claim appears
never to have been confirmed against the live grader. The statement is
therefore worded conditionally ("can break compilation"). Confirm it on
HackerRank once the problem is live, and tighten or drop the wording to match.

Not verified with the grader's own JDK; this container has JDK 21 only.

## Note on test-case coverage

`CLAUDE.md` asks for 10 to 15 cases per problem, including empty input, a
single element, and maximum size. None of that applies here: the problem takes
no input and has exactly one possible output, so one case covers the whole
input space. The score is all-or-nothing by design, which is the correct
behaviour for a problem whose purpose is to confirm that submission works at
all.
