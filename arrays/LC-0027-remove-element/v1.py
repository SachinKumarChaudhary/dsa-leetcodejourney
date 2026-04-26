# LC-0027 Remove Element
# Version: v1 (Initial - remove loop)

# Approach:
# Repeatedly remove val from array

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)
