# ds-11-merge-k: upload checklist

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

The Tail uses `StreamTokenizer`: 500,000 values plus 100,000 length fields.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 03 as samples** (03, not 02)

Case 03 has empty lists at the front, in the middle and at the end. Offering
an empty list to the heap reads a position that does not exist, and the book's
own code guards against it -- this is the sample that shows why.

**Case 04 is every list empty, and its expected output is a single empty
line.** Confirm after upload that the blank line survived.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-11-merge-k`
- [ ] **Max Score = 30**
- [ ] Place it third among the chapter 11 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] Confirm a correct submission scores 30/30
- [ ] Confirm the empty-line output of case 04 displays correctly

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Cause |
|---|---|---|
| Min-heap, one candidate per list (registered) | 14/14 | -- |
| Scan every list front at each step, O(N*k) | 11/14 | times out on 11 12 13 |
| Never re-offering the next element of the list just used | 2/14 | returns only the k smallest |
| Max-heap instead of min-heap | 4/14 | wrong on 10 cases |
| Pour everything into one array and sort | **14/14** | not a mistake -- see below |

Reference timing: 609 to 751 ms.

## What this problem cannot enforce

**Collecting every value into one array and calling `Arrays.sort` passes**,
and it is not even slower:

| Case | Heap | Sort everything |
|---|---|---|
| 10 | 609 ms | 481 ms |
| 11 | 751 ms | 638 ms |
| 12 | 625 ms | 656 ms |
| 13 | 616 ms | 627 ms |

This cannot be excluded. The required output is the fully merged list, so any
method producing a sorted sequence of the same values is right by definition,
and $O(N \log N)$ is not meaningfully worse than $O(N \log k)$ when `k` is
close to `N`.

So **the heap here is the taught method, not the enforced one**. What the
problem does enforce is that the $O(N \cdot k)$ scan fails, which is the
comparison the book's hint is actually about.

Making the heap necessary would mean changing the question -- asking for only
the first `m` values of the merge, with `N` far larger than `m`. That is no
longer the book's problem, so it is flagged here rather than done, and
reserved in `variants.md` as an exam question instead.

Case 12 is nevertheless shaped for the honest comparison: `k` is at its
maximum and the values are drawn so the lists interleave throughout and none
is exhausted early, which is where a per-step scan pays its full `k`.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. The model just sorts every
value, which is the right choice here precisely because it shares no reasoning
with the heap solution.

`gen.py` asserts that every list it writes is ascending -- an input that is
not sorted would make the problem unsolvable as stated and the failure would
look like a bug in the student's code.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
