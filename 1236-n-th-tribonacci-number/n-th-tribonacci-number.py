class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        a, b, c, d = 0, 1, 1, 0
        i = 2
        while i < n: 
            d = a + b + c
            a, b, c = b, c, d
            i += 1
        return d