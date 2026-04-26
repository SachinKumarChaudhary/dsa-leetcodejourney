# LC-0605 Can Place Flowers

## Key Insight
A flower can be placed only if both neighbors are empty.

## Why my approach worked / failed
- Initial approach handled edges separately → messy and error-prone
- Cleaner logic is to treat edges as having virtual zeros

## Pattern
Greedy placement / local decision

## When to use this again
- When decisions depend only on neighbors
- When constraints are local (adjacent elements)

## Alternative Thinking
- Instead of simulating placement, count consecutive zeros
- Formula: (zeros - 1) // 2 gives number of flowers possible
