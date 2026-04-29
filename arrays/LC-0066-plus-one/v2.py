# Version: v2 (Better carry handling)

# Approach:
# Traverse from end and handle carry manually

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def plusOne(self, digits):
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # if all were 9
        return [1] + digits