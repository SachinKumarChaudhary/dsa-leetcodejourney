# Version: v3 (Optimal - HashMap)

# Approach:
# Store visited elements in dictionary
# Check if complement exists while iterating

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i