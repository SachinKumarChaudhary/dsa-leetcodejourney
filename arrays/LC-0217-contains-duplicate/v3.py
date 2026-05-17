# Version: v3 (Optimal - HashSet)

# Approach:
# Convert array to set
# If lengths differ → duplicates exist

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums):
        unique = set(nums)

        return len(nums) != len(unique)