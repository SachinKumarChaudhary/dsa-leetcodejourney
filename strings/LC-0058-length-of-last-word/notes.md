# LC-0058 Length of Last Word

## Key Insight
The last word starts after the last space (ignoring trailing spaces).

## Why my approach worked / failed
- Using strip simplifies handling trailing spaces
- But slicing creates extra space

## Pattern
String traversal from end

## When to use this again
- Problems involving last element/word
- When trailing spaces complicate parsing

## Alternative Thinking
- Skip spaces manually instead of using strip
- Use split for simplicity (but uses extra memory)