# Exam variation axes: ds-14-hash-table

This contest does not count toward the course grade. The one thing that keeps
students working on it is the promise that **the programming questions on the
midterm and the final are built as variations of these problems.** So this file
is written *while* the problem is built, not afterwards.

There is no Korean counterpart, so every axis below is available to the
English section.

## The core of the original problem

A slot per hash value, a list per slot. Everything else follows: a lookup is
$O(1)$ to find the slot plus the length of the chain, which is why the load
factor is the number that matters.

## Variation axes

- **Ask for the cost**: what does `get` cost with `n` keys in a table of
  `size` slots, assuming the hash spreads them evenly? $O(1 + n/size)$. Then:
  what if it does not spread them? $O(n)$, and the table is a list. Case 12 of
  this problem is that input.
- **Add resizing**: when the load factor passes a threshold, double the table
  and **rehash everything**. Ask why the entries cannot simply be copied
  across -- because `key % size` changes when `size` does. **This is the best
  exam question here**, and it is what 14.5 is for.
- **Change the collision strategy**: open addressing with linear probing. Then
  the hard part is `remove`, which cannot just blank a slot without breaking
  the probe sequence for keys behind it. A genuinely good challenge item.
- **Ask about the negative key**: why is `key % size` not enough, and what
  does `((key % size) + size) % size` do? Also: why is the second `%` needed?
  Because the sum can reach `size` exactly.
- **Ask about `get` returning -1**: what is wrong with this convention, and
  what would Java's `HashMap` do instead? Return `null`, or use
  `containsKey`. Short and real.
- **Count the collisions**: report how many keys share a slot with another,
  or the longest chain. One extra pass over the buckets.
- **Change the hash function**: multiply by a prime first, or use
  `Integer.hashCode`. Give a key set that defeats `key % size` -- multiples of
  the size -- and ask which functions survive it.
- **Trace by hand**: a table of 5, six keys including a negative one, and ask
  for the bucket contents.

## Overlap with other problems

| Axis | Also appears in | Note |
|---|---|---|
| Using a hash map | `ds-14-word-count`, `ds-14-group-anagrams`, `ds-14-longest-consecutive` | Those three use one; this is the only one that builds one. Keep implementation questions here. |
| Building the structure the chapter describes | `ds-11-heap` | Same role in chapter 11, and the same `print`-the-internals device. The pair makes a good "why can we not just use the library" discussion. |
| Average versus worst case | `ds-14-word-count` variants | That problem's "why $O(1)$ on average" question is answered by this problem's case 12. |

## Draft split between sections

| Section | Axis reserved |
|---|---|
| Korean (dsa) | No counterpart problem exists; nothing reserved. |
| English (ds) | Resizing and rehashing -- why entries cannot be copied across |

## Usage history

| Exam | Axis used | Note |
|---|---|---|
| | | |
