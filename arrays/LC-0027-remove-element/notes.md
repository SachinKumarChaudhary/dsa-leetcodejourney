# LC-0027 Remove Element

## Key Insight
We don’t need to maintain order → we can overwrite or swap.

## Why my approach worked / failed
- remove() works but is inefficient (O(n^2))
- Not scalable for larger inputs

## Pattern
Two pointers / in-place array modification

## When to use this again
- Removing elements in-place
- Filtering arrays
- When order does NOT matter (use swap trick)

## Alternative Thinking
- Overwrite method → keeps order
- Swap with last → faster in practice, order not preserved