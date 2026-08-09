# Hackerrank Java Practice

This repository contains Java solutions and test cases for HackerRank-style practice problems.

## Structure

- `bank/`: problem folders, each with `Solution.java` and `testcases/`
- `test.ps1`: runs compilation and testcase validation for a given problem
- `.work/`: temporary build/output directory used by the test script

## Usage

Run tests for a problem:

```powershell
powershell -ExecutionPolicy Bypass -File .\test.ps1 ds-tutorial-02-echo
```

## Notes

- The test script compiles `Solution.java` in a temporary workspace and compares output against the expected testcase files.
- Line endings are normalized with `.gitattributes` to keep test case files consistent across platforms.
