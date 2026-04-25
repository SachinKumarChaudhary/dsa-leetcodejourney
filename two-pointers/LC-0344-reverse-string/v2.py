# Version: v2 (Refined)

# Improvement:
# Use explicit left/right pointers for clarity

class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1