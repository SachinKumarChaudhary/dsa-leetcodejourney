# LC-1855 Maximum Distance Between a Pair of Values
# Version: v1 (Initial - two pointers)

# Approach:
# Use two pointers i and j.
# Move j forward to maximize distance when condition holds.
# Move i forward when condition breaks.

# Time Complexity: O(n + m)
# Space Complexity: O(1)

class Solution:
    def maxDistance(self, nums1, nums2):
        i = 0
        j = 0
        ans = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1

        return ans