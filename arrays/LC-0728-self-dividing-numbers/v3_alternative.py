# Version: v3 (Alternative approach - string)

class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        return [
            num for num in range(left, right + 1)
            if all(d != '0' and num % int(d) == 0 for d in str(num))
        ]
