# LC-0217 Contains Duplicate

## Key Insight
A set only stores unique values.

If duplicates exist:
len(set(nums)) < len(nums)

## Mistake I made
- No major logic mistake
- Could simplify return statement

## Pattern
HashSet / Duplicate Detection

## Why optimal works
Set automatically removes duplicates.

So:
- same length → all unique
- smaller set length → duplicate exists

## When to use this again
- Duplicate detection
- Membership lookup
- Fast uniqueness checking

## Complexity
- v1: O(n^2)
- v2: O(n log n)
- v3: O(n)