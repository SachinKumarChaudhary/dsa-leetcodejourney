# LC-0026 Remove Duplicates from Sorted Array

## Key Insight
Since array is sorted, duplicates are adjacent.

We can overwrite duplicates using a slow pointer.

## Mistake I made
- Used set() which:
  - uses extra space
  - does not modify array in-place
  - may break ordering

## Pattern
Two Pointers / Overwrite

## Why optimal works
- right pointer scans array
- left pointer stores next unique position

Whenever a new unique number appears:
overwrite nums[left]

## When to use this again
- In-place array modification
- Removing duplicates
- Sorted array problems
- Overwrite patterns

## Complexity
- v1: O(n) space
- v2: O(1) space
- v3: O(1) space