# Version: v3 (Alternative - swap with last)

# Approach:
# Swap unwanted element with last and shrink array size

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeElement(self, nums, val):
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1

        return n