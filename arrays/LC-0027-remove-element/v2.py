# Version: v2 (Refined)

# Approach:
# Use slow pointer to overwrite elements not equal to val

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeElement(self, nums, val):
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k