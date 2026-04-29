# LC-0066 Plus One
# https://leetcode.com/problems/plus-one/
# Difficulty: Easy

# v3

class Solution:
    pass
# Version: v3 (Clean optimal)

# Approach:
# Same as v2 but cleaner logic

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1

            if digits[i] < 10:
                return digits

            digits[i] = 0

        return [1] + digits