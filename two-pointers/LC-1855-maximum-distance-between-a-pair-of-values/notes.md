# LC-1855 Maximum Distance Between a Pair of Values

## Key Insight
Both arrays are non-increasing → enables two-pointer or binary search.

## Why my approach worked / failed
- Two pointers work because both arrays move in one direction.
- If condition holds → expand j to maximize distance.
- If condition fails → increase i to find smaller nums1[i].

## Pattern
Two pointers on sorted / monotonic arrays

## When to use this again
- When arrays are sorted (especially non-increasing)
- When you need max/min distance between valid pairs
- When brute force is O(n^2) but monotonicity exists

## Alternative Thinking
- Binary search for each i to find farthest valid j
- Useful when arrays are large and condition is monotonic