# LC-3783 Mirror Distance of an Integer
# Link: https://leetcode.com/problems/mirror-distance-of-an-integer/
# Version: v1 (Initial)

# Approach:
# Reverse digits using modulo and division

# Time Complexity: O(d)
# Space Complexity: O(1)

class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = 0
        temp = n

        while temp > 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp //= 10

        return abs(n - rev)

