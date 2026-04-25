# LC-0344 Reverse String
# Version: v1 (Initial)

# Approach:
# Swap characters from both ends moving toward the center

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def reverseString(self, s):
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]