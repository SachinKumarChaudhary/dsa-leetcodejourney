# Version: v2 (Refined)

# Improvement:
# Use count() to simplify logic

class Solution:
    def furthestDistanceFromOrigin(self, moves):
        left = moves.count('L')
        right = moves.count('R')
        blanks = moves.count('_')

        return abs(left - right) + blanks