# LC-2078 Two Furthest Houses With Different Colors
# Version: v1 (Initial)

# Approach:
# Compare first element with elements from right
# Compare last element with elements from left

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        
        max_dist = 0
        max_dist1 = 0

        # compare first with right side
        for x in range(n):
            if colors[0] != colors[n - 1 - x]:
                max_dist = n - 1 - x
                break

        # compare last with left side
        for x in range(n):
            if colors[n - 1] != colors[x]:
                max_dist1 = n - 1 - x
                break

        return max(max_dist, max_dist1)