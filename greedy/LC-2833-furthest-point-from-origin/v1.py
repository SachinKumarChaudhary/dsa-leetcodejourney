# LC-2833 Furthest Point From Origin
# Version: v1 (Initial)

# Approach:
# Track net movement (L = -1, R = +1)
# Count '_' separately → can be used to maximize distance

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def furthestDistanceFromOrigin(self, moves):
        pos = 0
        blanks = 0

        for ch in moves:
            if ch == 'L':
                pos -= 1
            elif ch == 'R':
                pos += 1
            else:
                blanks += 1

        return abs(pos) + blanks