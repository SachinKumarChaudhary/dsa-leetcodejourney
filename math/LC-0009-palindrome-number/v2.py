# Version: v2 (Refined)

# Approach:
# Use Python slicing to reverse

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, x):
        s = str(x)
        return s == s[::-1]
