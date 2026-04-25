# LC-2114 Maximum Number of Words Found in Sentences

## Summary
Find the maximum number of words in a sentence by counting spaces or using string split.

## Learnings
- Words = spaces + 1 (since no leading/trailing spaces)
- `split()` is the simplest and cleanest approach
- Avoid unnecessary arrays when tracking max

## Mistakes
- Initially appended count inside character loop (wrong placement)
- That caused incorrect results because counting was done per character, not per sentence

## Approaches
- v1: Manual counting using spaces
- v2: Optimized loop with max tracking
- v3: Using built-in split()

## Pattern
String processing / counting
