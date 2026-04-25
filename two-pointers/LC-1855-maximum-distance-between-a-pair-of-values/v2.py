# Version: v2 (Refined)

# Improvement:
# Same logic but explicitly ensures j never goes behind i

class Solution:
    def maxDistance(self, nums1, nums2):
        i = 0
        j = 0
        ans = 0

        n, m = len(nums1), len(nums2)

        while i < n and j < m:
            if i > j:
                j = i  # maintain constraint i <= j

            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1

        return ans