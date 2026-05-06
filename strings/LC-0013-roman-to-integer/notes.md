# LC-0013 Roman to Integer

## Key Insight
Roman numerals usually add values, but smaller value before larger value means subtraction.

Examples:
- IV = 4
- IX = 9
- XL = 40

## Mistakes I made
- Compared characters alphabetically instead of values
- Used x += 1 inside for loop (does not affect iteration)
- Risked index out-of-range with s[x+1]

## Pattern
Mapping + Traversal

## Why optimal works
If previous value is smaller than current:
previous was wrongly added earlier

So:
total += current - 2 * previous

## When to use this again
- Symbol/value mapping problems
- Parsing encoded strings
- Traversal with previous state tracking

## Complexity
- v1: O(n)
- v2: O(n)
- v3: O(n)