# Version: v3 (Optimal concise)

# Approach:
# Maintain position of next unique element

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums):
        left = 1

        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1

        return left