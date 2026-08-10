# ds-10-bst: upload checklist

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

The Head is **not** the chapter 9 Head: the node field is `key` rather than
`data`, there is no level-order parser (the tree is built by the commands),
and the two traversal helpers append to a `StringBuilder` instead of a list.

Head and Tail are not actually locked; see the note in
`ds-04-array-list/UPLOAD.md`.

## 3. Test cases

- [ ] Upload `testcases.zip` (`input/` and `output/` folders, 14 cases)
- [ ] **Mark cases 00, 01 and 02 as samples**

Case 02 is the one that must be public:

```
preorder before : 50 30 20 45 70
after delete 50 : 45 30 20 70     <- required (predecessor)
                  70 30 20 45     <- what the successor rule gives
print           : 20 30 45 70     <- identical either way
```

The `print` line cannot tell the two apart. Only `preorder` can, and a student
who never sees this sample has no way to know which rule was wanted.

`testcases/SAMPLES` lists the case numbers to mark.

## 4. Language settings

- [ ] **Keep Java 15 only; clear every other language**

## 5. Register the solution

- [ ] Upload `Solution.java` under Upload solution

## 6. Publish

- [ ] **Publish** the challenge
- [ ] Contest -> Challenges tab -> **Add Challenge** -> `ds-10-bst`
- [ ] **Max Score = 30**
- [ ] Place it first among the chapter 10 problems

## 7. Wrap up

- [ ] Update `published` / `in_contest` / `contest_slug` / `hackerrank_slug` /
      `url` in `meta.yml`
- [ ] git commit & push

## 8. Check it yourself (recommended)

- [ ] Open an incognito window, sign in as a **separate account**, and solve it
      from scratch
- [ ] **Submit the stub untouched.** It compiles and scores 1/14
- [ ] Check the reported time on case 13; it is 1.77 s here, the slowest of
      the set, and it is the one to watch if the grader is slower

## Verification record

Compiled with `javac --release 15 -Xlint:all -encoding US-ASCII` on
JDK 21.0.10. No warnings.

| Submission | Result | Fails on |
|---|---|---|
| Insert, search, predecessor deletion (registered) | 14/14 | -- |
| Deletion promoting the **successor** | 12/14 | 02 08 |
| `insert` not reassigning the returned root | 2/14 | 12 cases |
| Duplicate keys inserted as new nodes | 9/14 | 01 05 09 11 12 |
| Two-children case tested before the one-child cases | 7/14 | 00 03 06 09 10 11 13 |

Reference timing: 400 ms to **1767 ms** (case 13).

Case 13 is slow because of its **shape**, not its size: 4,000 keys inserted in
ascending order make a spine of height 4,032, and every later search walks
thousands of levels. That is section 10.4's skew problem made expensive, and
it is worth keeping -- but it is the case to watch on a slower grader.

## Two additions to the Korean version, and why

**`deleteKey`.** Section 10.3 is devoted to removal and its three cases, and
the Korean problem asks only for insert and search. Without this the whole
section goes untested.

**The `preorder` command.** The Korean version prints inorder only, which on a
BST is just the sorted key list: it reveals the **set** of keys and nothing
about the shape. A student could pass the entire problem with a sorted
collection and no tree at all.

`preorder` closes that, but it is only usable because 10.3 pins down the one
place where a valid BST's shape is ambiguous. A node with two children may be
replaced by either neighbour in sorted order, and **the book uses the
predecessor** -- the largest key in the left subtree. The statement requires
it and `preorder` checks it.

**If that requirement is ever relaxed, remove the `preorder` command with
it.** The successor variant scores 12/14 here, failing only the two cases that
print a preorder after a two-child removal; without the requirement those two
cases would be marking a free choice wrong.

## Note on the test set

Regenerate with `python3 gen.py`. The seed is fixed. The model is an iterative
BST over parallel arrays, so it shares no code with the recursive solution.

One thing to know before editing it: an earlier version measured the tree's
height after **every** command, which is $O(n)$ each and turned generation
into $O(M \cdot n)$ -- at M = 200,000 it did not finish. The height is now
sampled every 2,000 commands and once at the end, which is enough to police
the 5,000 cap because the height only grows while inserts are happening.

Every file in this directory is pure ASCII, and all test files use LF line
endings. Check with:

```
LC_ALL=C grep -rn '[^ -~\t]' .
```

Not verified with the grader's own JDK; this container has JDK 21 only.
