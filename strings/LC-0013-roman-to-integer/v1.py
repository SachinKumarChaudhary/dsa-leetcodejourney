# LC-0013 Roman to Integer
# Version: v1 (Basic mapping)

# Approach:
# Convert each Roman symbol to integer and handle subtraction cases

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

        total = 0
        n = len(s)

        for i in range(n):
            # subtraction case
            if i < n - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total