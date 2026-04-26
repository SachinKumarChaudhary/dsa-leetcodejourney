# LC-0001 Two Sum
# Version: v1 (Brute Force)

# Approach:
# Check every pair of elements and return indices if sum equals target

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)

        for i in range(n):
            for j in range(n):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]