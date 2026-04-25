# Version: v2 (Refined)
class Solution:
    def mirrorDistance(self, n: int) -> int:
        original = n
        rev = 0

        while n:
            rev = rev * 10 + n % 10
            n //= 10

        return abs(original - rev)
