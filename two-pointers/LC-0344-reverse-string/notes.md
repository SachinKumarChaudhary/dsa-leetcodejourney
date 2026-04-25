# LC-0344 Reverse String

## Key Insight
Use two pointers from both ends and swap elements until they meet.

## Why my approach worked / failed
- In-place swapping satisfies O(1) space requirement
- Using indices ensures no extra memory is used

## Pattern
Two pointers / in-place array manipulation

## When to use this again
- Reversing arrays or strings in-place
- Problems requiring O(1) extra space
- Symmetric operations from both ends

## Alternative Thinking
- Python slicing (`s[::-1]`) is simpler but not optimal for space constraints