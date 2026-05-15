# LC-0026 Remove Duplicates from Sorted Array
# Version: v1 (Using extra array)

# Approach:
# Store unique elements separately and overwrite original array

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def removeDuplicates(self, nums):
        unique = []

        for num in nums:
            if num not in unique:
                unique.append(num)

        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(unique)