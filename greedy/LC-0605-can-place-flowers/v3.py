# Version: v3 (Alternative)

# Approach:
# Count consecutive zeros and compute how many flowers can be placed

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        zeros = 1  # virtual zero at start

        for plot in flowerbed:
            if plot == 0:
                zeros += 1
            else:
                count += (zeros - 1) // 2
                zeros = 0

        zeros += 1  # virtual zero at end
        count += (zeros - 1) // 2

        return count >= n