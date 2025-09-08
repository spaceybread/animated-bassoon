import random

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a, b = 0, 0

        while '0' in str(a) or '0' in str(b):
            a = random.randint(1, n - 1)
            b = n - a
        
        return [a, b]