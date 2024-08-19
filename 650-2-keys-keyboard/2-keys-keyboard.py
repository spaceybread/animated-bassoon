class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        s, f, = 0, 2

        while n > 1:
            while n % f == 0:
                s += f
                n //= f
            f += 1

        return s