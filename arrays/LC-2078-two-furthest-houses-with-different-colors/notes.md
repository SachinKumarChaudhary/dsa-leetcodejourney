# LC-2078 Two Furthest Houses With Different Colors

## Key Insight
Maximum distance must involve either the first or last house.

## Why my approach worked / failed
- I correctly compared edges, but used extra loops and variables.
- Logic can be simplified using direct scanning.

## Pattern
Greedy / boundary checking

## When to use this again
- When maximizing distance
- When endpoints dominate the answer
- When constraints allow linear scan

## Alternative Thinking
Instead of checking all pairs (O(n²)), use boundary properties to reduce to O(n)