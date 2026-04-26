# LC-0009 Palindrome Number
# Version: v1 (Initial - string conversion)

# Approach:
# Convert number to string and compare characters from both ends

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, x):
        x = str(x)
        n = len(x)

        for i in range(n // 2):
            if x[i] != x[n - 1 - i]:
                return False

        return True
