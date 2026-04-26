# Version: v2 (Improved - direct search)

# Approach:
# For each element, calculate complement and search in array

# Time Complexity: O(n^2)  (because "in" + index())
# Space Complexity: O(1)

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]

            if complement in nums:
                j = nums.index(complement)

                if i != j:
                    return [i, j]