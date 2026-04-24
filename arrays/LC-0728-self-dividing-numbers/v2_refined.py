# Version: v2 (Refined same approach)

class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        result = []

        for num in range(left, right + 1):
            temp = num

            while temp:
                digit = temp % 10
                if digit == 0 or num % digit != 0:
                    break
                temp //= 10
            else:
                result.append(num)

        return result
