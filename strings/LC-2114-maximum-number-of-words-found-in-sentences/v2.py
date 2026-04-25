# Version: v2 (Refined)

# Approach:
# Track max directly without extra array

# Time Complexity: O(n * m)
# Space Complexity: O(1)

class Solution:
    def mostWordsFound(self, sentences):
        ans = 0
        
        for sentence in sentences:
            count = 1
            for ch in sentence:
                if ch == ' ':
                    count += 1
            
            ans = max(ans, count)
        
        return ans
