# LC-2114 Maximum Number of Words Found in Sentences
# Version: v1 (Initial - manual counting)

# Approach:
# Count spaces in each sentence and add 1 → words = spaces + 1

# Time Complexity: O(n * m)
# Space Complexity: O(n)

class Solution:
    def mostWordsFound(self, sentences):
        countarr = []
        
        for sentence in sentences:
            count = 1
            for ch in sentence:
                if ch == ' ':
                    count += 1
            
            countarr.append(count)
        
        return max(countarr)