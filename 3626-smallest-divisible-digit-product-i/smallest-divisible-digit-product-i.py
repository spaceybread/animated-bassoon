class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        import math
        pr = lambda b: math.prod([int(x) for x in list(str(b))])

        sols = [x for x in range(n, ((n // 10) + 1) * 10 + 1)]
        
        for x in sols: 
            if pr(x) % t == 0: return x