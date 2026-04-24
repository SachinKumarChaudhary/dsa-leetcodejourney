# LC-0728 Self Dividing Numbers
# Version: v1 (Initial)

# Approach:
# Iterate through each number and check digits using modulo

# Time Complexity: O(n * d)
# Space Complexity: O(1)

class Solution(object):
    def selfDividingNumbers(self, left, right):
        result = []

        for i in range(left, right + 1):
            temp = i

            while temp > 0:
                digit = temp % 10

                if digit == 0 or i % digit != 0:
                    break

                temp = temp // 10

            else:
                result.append(i)

        return result
