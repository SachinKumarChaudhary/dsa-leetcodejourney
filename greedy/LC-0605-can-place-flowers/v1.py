# LC-0605 Can Place Flowers
# Version: v1 (Initial - cleaned)

# Approach:
# Try placing flower at each position if left and right are empty

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        length = len(flowerbed)
        count = 0

        for i in range(length):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i - 1] == 0)
                right = (i == length - 1) or (flowerbed[i + 1] == 0)

                if left and right:
                    flowerbed[i] = 1
                    count += 1

        return count >= n