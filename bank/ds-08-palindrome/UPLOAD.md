# ds-08-palindrome: upload checklist

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

The Head is only the imports and the class opening. The stub exists so the
student writes a **method**, not a program -- which is the point of a
recursion problem, and it also leaves room for the helper method they will
need.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 is the one that must be public. It pairs `Level` with `level`, `Aba`
with `aba`, `AA` with `aa`. A comparison that ignores case accepts all six and
this is the only place a student sees it.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-08-palindrome`
- [ ] **Max Score = 10**
- [ ] Place it first among the chapter 8 problems

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

| Submission | Result | Fails on |
|---|---|---|
| Narrow from both ends with a helper (registered) | 14/14 | -- |
| Comparison ignoring case | 8/14 | 00 02 04 10 11 13 |
| Base case written `low == high` only | 3/14 | 11 cases |
| Recursing on `(low + 1, high)` | 5/14 | 9 cases |
| Unmodified stub | 1/14 | it returns `false`, right for one case by luck |

Reference timing: 91 to 166 ms.

**The base-case mistake is the one worth understanding.** Writing
`low == high` catches odd-length strings, where the range closes on a single
character, and misses even-length ones, where it closes with `low > high` and
the recursion carries on past the ends of the string. Cases 01 and 03 separate
the two parities on purpose.

## What this problem cannot enforce

**It cannot check that the method is recursive.** A student can write

```java
return s.equals(new StringBuilder(s).reverse().toString());
```

and score 10/10. No arrangement of test data changes that. The Korean
counterpart accepts the same limitation and so does this one: recursion is
asked for in the constraints, and it is assessed on the exam rather than here.

This is worth saying out loud when introducing the chapter. Every chapter 8
problem has the same hole, and pretending otherwise is worse than naming it.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed.

Case 13 is worth a note: it takes a lowercase palindrome and uppercases one
character. That almost always breaks it -- but not when the chosen position is
the exact middle of an odd-length string, which is why 11 of the 1,000 come
back `true`. Those eleven are the ones that catch a solution that decided
"uppercase present" means "not a palindrome".

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
