# LC-0058 Length of Last Word
# Version: v1 (Initial)

# Approach:
# Strip trailing spaces, then scan from end to find last word

# Time Complexity: O(n)
# Space Complexity: O(n) due to slicing

class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        i = len(s) - 1

        while i >= 0 and s[i] != " ":
            i -= 1

        return len(s[i+1:])