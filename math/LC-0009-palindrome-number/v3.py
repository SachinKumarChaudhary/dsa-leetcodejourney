# Version: v3 (Optimal - reverse half)

# Approach:
# Reverse only half of the number and compare

# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0

        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10

        return x == rev or x == rev // 10