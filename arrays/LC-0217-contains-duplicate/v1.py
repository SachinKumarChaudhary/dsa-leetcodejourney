# LC-0217 Contains Duplicate
# Version: v1 (Brute Force)

# Approach:
# Compare every pair of elements

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def containsDuplicate(self, nums):
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True

        return False