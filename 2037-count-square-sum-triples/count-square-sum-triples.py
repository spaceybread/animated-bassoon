class Solution:


    def countTriples(self, n: int) -> int:
        sols = 0
        for i in range(1, int(n**0.5) + 1):
            for j in range(1, i):
                if i**2 + j**2 > n: continue
                if gcd(i, j) != 1: continue
                if (i % 2 == j % 2): continue
                o = (n // (i**2 + j**2)) * 2
                sols += o

        return sols
                

