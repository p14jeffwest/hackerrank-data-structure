# Exam variation axes: ds-14-word-count

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

The Korean set has `dsa-11-word-count`, the same problem, so the axes must be
split.

## The core of the original problem

One pass builds the counts; every query is then a lookup. The hash replaces
the scan, which is the whole point of chapter 14.

## Variation axes

- **Ask for the cost**: what does a scan per query cost, and what does the map
  cost? $O(NQ)$ against $O(N + Q)$ on average -- and **why "on average"?**
  That second half is the better question, and 14.5 answers it.
- **Ask what happens with a bad hash**: if every word hashed to the same
  bucket, what would a lookup cost? $O(n)$, and the map degenerates into a
  list. Ties to 14.4 and to `ds-14-hash-table`.
- **Report the most frequent word**, with ties broken alphabetically. That is
  the Korean set's `dsa-11-top-k-words`, so **reserve it for that section**.
- **Count something else**: characters instead of words; pairs of adjacent
  words; words by their length.
- **Ask about `getOrDefault`**: what does `get` return for an absent key, and
  what happens next? `null`, then a `NullPointerException` when it is
  unboxed. Short, exact, and it is the mistake sample 02 exists for.
- **Ask about `merge`**: what do `merge(w, 1, Integer::sum)` and
  `put(w, getOrDefault(w, 0) + 1)` have in common, and is either faster?
- **Case-insensitive counting**: fold to lower case first. Then: what if the
  key were a `char[]` instead of a `String`? It would not work, because arrays
  do not override `equals` and `hashCode` -- a good trap and a real one.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| The problem itself | `dsa-11-word-count` (Korean set) | Same problem by design. The reserved split below keeps the exams apart. |
| Top-K by frequency | `dsa-11-top-k-words` (Korean set) | Reserved for the Korean exams; not a problem in this set. |
| Grouping by a computed key | `ds-14-group-anagrams` | That problem owns the "what should the key be" question. |
| Average versus worst case for a hash | `ds-14-hash-table` | That problem builds the buckets; ask the degeneracy question there. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | Top-K by frequency, ties broken alphabetically |
| English (ds) | Why a hash map is $O(1)$ **on average**, and what makes it not |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
