# LC-0066 Plus One

## Key Insight
Work from the last digit and simulate carry like real addition.

## Mistake I made
- Converted array → number → array (unnecessary)
- Used digits.index() → adds extra O(n)
- Overcomplicated simple carry problem

## Pattern
Carry Propagation / Simulation

## Why optimal works
Addition happens from right to left:
- If digit < 9 → just +1 and stop
- If digit = 9 → becomes 0 and carry continues

## When to use this again
- Digit manipulation problems
- Carry-based operations
- Array-based number representation

## Complexity
- v1: O(n^2)
- v2: O(n)
- v3: O(n) again?)
