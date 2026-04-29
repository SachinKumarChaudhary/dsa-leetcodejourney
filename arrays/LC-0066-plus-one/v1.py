# LC-0066 Plus One
# Version: v1 (Convert to number)

# Approach:
# Convert digits to number, add 1, convert back to list

# Time Complexity: O(n^2) (because of index())
# Space Complexity: O(n)

class Solution:
    def plusOne(self, digits):
        n = len(digits)
        num = 0

        for i in range(n):
            num = num * 10 + digits[i]

        num += 1

        res = []
        while num > 0:
            res.append(num % 10)
            num //= 10

        return res[::-1]