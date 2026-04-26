# LC-0001 Two Sum

## Key Insight
Instead of checking every pair, store visited numbers and directly check if complement exists.

## Mistake I made
- Used nums.index() → O(n)
- Used "in nums" → still O(n)
- Result: still O(n^2) instead of O(n)

## Pattern
HashMap / Complement Lookup

## Why optimal works
At each step:
target = a + b  
→ b = target - a

So we check:
"Have I already seen b?"

## When to use this again
- Pair sum problems
- Complement-based questions
- Lookup + condition problems

## Complexity
- Brute: O(n^2)
- Optimal: O(n)