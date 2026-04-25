# Version: v3 (Alternative - split)

# Approach:
# Use split() to count words directly

# Time Complexity: O(n * m)
# Space Complexity: O(m) due to split

class Solution:
    def mostWordsFound(self, sentences):
        return max(len(s.split()) for s in sentences)
