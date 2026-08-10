# ds-14-word-count: upload checklist

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

**No custom stub.** Leave the platform default, which is what
`07. code-stub.java` records. Students write the whole program, including the
reading -- the same as the Korean version.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 is four queries, none of which appears in the list, so every answer is
`0`. `HashMap.get` returns `null` there and throws when it is unboxed;
`getOrDefault` gives the `0` that is wanted. Nothing else in the samples
reaches that.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-14-word-count`
- [ ] **Max Score = 10**
- [ ] Place it first among the chapter 14 problems

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

| Submission | Result | Cause |
|---|---|---|
| One pass into a `HashMap`, then one lookup per query (registered) | 14/14 | -- |
| Scanning the list for every query, O(N*Q) | 8/14 | times out on 08 through 13 |
| `get()` instead of `getOrDefault()` | 4/14 | throws wherever a query word is absent |
| A `HashSet`, so every count is 1 | 5/14 | wrong on 9 cases |

Reference timing: 331 to 371 ms.

The `get()` mistake throws rather than answering wrongly, so it fails every
case containing a word that is not in the list. Cases 08, 09, 11 and 13 draw
their queries only from words that **do** appear, which is what keeps it at
4/14 rather than 0 -- and tells the student the problem is the missing words
specifically.

## A note on the reading, since there is no stub here

This problem uses the **platform default stub**, so the input reading is the
student's own code. At 400,000 words a naive reader is slow enough to matter,
and that is their problem to notice rather than something the Head hides from
them.

The registered solution reads with `StreamTokenizer` in word mode
(`ordinaryChars` then `wordChars` for letters and digits) and shows one way to
do it. `BufferedReader` with `StringTokenizer` per line is also fine at these
sizes; `Scanner` is not.

## Bounds

Raised fourfold from the Korean version's 50,000, which was comfortable for
both the map and a scan at the smaller size. At 200,000 of each, a per-query
scan is 4 x 10^10 operations and does not finish.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. `gen.py` asserts the word
length and character set, which the constraints also state.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
