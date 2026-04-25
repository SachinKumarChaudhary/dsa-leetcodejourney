# Version: v3 (Optimal Insight)

# Approach:
# The answer must involve either index 0 or index n-1

class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        
        for i in range(n):
            if colors[i] != colors[0]:
                left = i
                break
        
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[-1]:
                right = n - 1 - i
                break
        
        return max(left, right)