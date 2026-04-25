# LC-3783 Mirror Distance of an Integer

## Summary
Reverse digits of n and compute absolute difference.

## Learnings
- Digit extraction using % and //
- Need to store original value when modifying n
- String reversal is simpler but less “low-level”

## Mistakes
- In v2, almost lost original value of n
- Could accidentally return wrong result

## Approaches
- v1: basic digit extraction
- v2: cleaner loop
- v3: string slicing

## Pattern
Digit manipulation / number reversal
