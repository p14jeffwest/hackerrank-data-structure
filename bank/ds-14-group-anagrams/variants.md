# Exam variation axes: ds-14-group-anagrams

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

There is no Korean counterpart, so every axis below is available to the
English section.

## The core of the original problem

Choosing the key. Anagrams have to collapse to the same key and non-anagrams
must not, and the sorted letters do exactly that. Section 14.7 says as much:
"what to use as the HashMap key" is the crux.

## Variation axes

- **Ask for a different key**: a 26-length count of the letters, written out
  as a string. That is $O(k)$ per word against sorting's $O(k \log k)$. When
  is it worth it? For long words over a small alphabet. **A good exam
  question** because both answers are right and the comparison is the point.
- **Give a key that fails**: the sum of the character codes, or the product,
  or the XOR. Ask for the smallest pair of words each one merges wrongly.
  Two letters suffice for the sum -- `ad` and `bc`.
- **Ask about the order**: what order does `new ArrayList<>(map.values())`
  give for a `HashMap`, and what does `LinkedHashMap` change? Then: is
  `HashMap`'s order random, or just unrelated to insertion? Unrelated but
  deterministic, which is a distinction students get wrong.
- **Detect one anagram** instead of grouping: 14.6 Level 1 Problem 2. Not a
  contest problem here, so it is free.
- **Group by something else**: by length; by the set of distinct letters; by
  the first letter. Same shape, and it shows the key is the only decision.
- **Count instead of listing**: how many groups, or the size of the largest.
  Removes the ordering question entirely, which makes it a fair short-answer
  version.
- **Ask about the cost**: with `n` words of length `k`, what dominates -- the
  sorting or the map? The sorting, and by a factor of $\log k$.
- **Trace by hand**: six words, list the key each produces and the resulting
  groups.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Choosing what to use as a key | `ds-13-largest-number` | That problem chooses what to sort *by*; this one chooses what to hash *on*. The pair makes one good "the decision is the key, not the algorithm" question. |
| Using a hash map | `ds-14-word-count`, `ds-14-longest-consecutive` | Those own counting and membership. This one owns grouping. |
| Insertion order | `ds-12-sort-records` | That problem owns stability. Here the analogous property comes from `LinkedHashMap` rather than from the sort. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | The 26-count key versus the sorted-letters key, and when each wins |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
