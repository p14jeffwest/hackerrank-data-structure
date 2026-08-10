# ds-14-group-anagrams: upload checklist

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
- [ ] **Mark cases 00, 03 and 04 as samples**

Each of 03 and 04 exists for one mistake:

- **03** fixes the group order. `zzz` appears first and must come first;
  returning a plain `HashMap`'s values puts `abc cba bac` first instead.
- **04** is `ad bc da cb ae bd ea db`. Those pairs sum to the same character
  total without being anagrams, so a key built from that sum merges them.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-14-group-anagrams`
- [ ] **Max Score = 30**
- [ ] Place it third among the chapter 14 problems

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

| Submission | Result | Fails on |
|---|---|---|
| Sorted-letters key in a `LinkedHashMap` (registered) | 14/14 | -- |
| The same, in a plain `HashMap` | 5/14 | 00 03 04 07 08 10 11 12 13 |
| Key made from the sum of the character codes | 10/14 | 04 11 12 13 |
| The word itself as the key | 4/14 | 10 cases |
| Sorting the words within each group | 8/14 | 00 03 05 08 11 13 |

Reference timing: 293 to 386 ms.

## The order requirement, and why the book's own code scores 5/14

14.7 says the order of the groups and of the words within them is free. **That
cannot be graded**, so this version fixes it: input order within a group,
groups in the order their first word appeared.

The choice is not arbitrary. It is exactly what a `LinkedHashMap` gives, and
requiring it turns the chapter's own point into something testable -- a plain
`HashMap` has **no order at all**, so `new ArrayList<>(map.values())` returns
the groups in an order that follows the hashing rather than the input.

The book's answer code uses a plain `HashMap` and therefore scores **5/14**
here. That is deliberate and worth saying out loud when teaching from it: the
book's code solves the book's problem, and this problem asks for one thing
more.

Sample 03 exists so a student meets that before submitting rather than after.

## The sum-of-character-codes key

It scores 10/14, which is higher than it looks like it should. A collision
needs two words whose letters sum alike **without** being anagrams -- `ad` and
`bc` both come to 197 -- and short random words rarely produce one. Case 04 is
built from such pairs on purpose, and cases 11 to 13 hit them by volume.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. Python dictionaries
preserve insertion order, so the model gets the required group order for free
-- which is the same reason `LinkedHashMap` is the right tool in Java.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
