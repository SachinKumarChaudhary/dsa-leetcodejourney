# Version: v3 (Alternative - bit manipulation)

# Approach:
# Use bitwise operations to simulate addition

# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def sum(self, num1, num2):
        while num2 != 0:
            carry = num1 & num2
            num1 = num1 ^ num2
            num2 = carry << 1
        return num1
