# Version: v3 (Alternative)

# Approach:
# Split string and get last word

class Solution:
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])