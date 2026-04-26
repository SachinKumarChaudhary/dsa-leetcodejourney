# LC-2833 Furthest Point From Origin

## Key Insight
'_' can be used as either L or R → choose direction that maximizes distance.

## Why my approach worked / failed
- Net position from L and R gives current displacement
- All '_' should be used in the same direction to maximize distance

## Pattern
Greedy + counting

## When to use this again
- When flexible choices ('_') can be assigned optimally
- When maximizing/minimizing distance or value

## Alternative Thinking
- Instead of simulating choices, count frequencies
- Final answer = |L - R| + blanks