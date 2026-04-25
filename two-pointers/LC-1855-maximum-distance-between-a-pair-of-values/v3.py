# Version: v3 (Alternative - binary search)

# Approach:
# For each i in nums1, find the farthest j in nums2
# such that nums2[j] >= nums1[i]

import bisect

class Solution:
    def maxDistance(self, nums1, nums2):
        ans = 0

        for i in range(len(nums1)):
            left = i
            right = len(nums2) - 1
            best = i - 1

            while left <= right:
                mid = (left + right) // 2
                if nums2[mid] >= nums1[i]:
                    best = mid
                    left = mid + 1
                else:
                    right = mid - 1

            ans = max(ans, best - i)

        return ans