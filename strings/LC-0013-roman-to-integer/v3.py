# Version: v3 (Optimal concise)

# Approach:
# Add current value normally
# If previous symbol was smaller, adjust subtraction

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def romanToInt(self, s):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = roman[s[0]]

        for i in range(1, len(s)):
            curr = roman[s[i]]
            prev = roman[s[i - 1]]

            if prev < curr:
                total += curr - 2 * prev
            else:
                total += curr

        return total