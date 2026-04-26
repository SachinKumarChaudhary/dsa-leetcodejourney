# Version: v2 (Refined)

# Improvement:
# Avoid creating new substring

class Solution:
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        length = 0

        # skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # count last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length