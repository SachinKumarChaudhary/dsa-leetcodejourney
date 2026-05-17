# Version: v2 (Sorting)

# Approach:
# Sort array and check adjacent elements

# Time Complexity: O(n log n)
# Space Complexity: O(1) or O(n) depending on sorting

class Solution:
    def containsDuplicate(self, nums):
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False