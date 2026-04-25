# Version: v3 (Alternative)

# Approach:
# Reverse using slicing (creates a new list)

class Solution:
    def reverseString(self, s):
        s[:] = s[::-1]