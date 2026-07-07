class Solution:
    def sumAndMultiply(self, n: int) -> int:
        a, b = 0, 0
        li = list(str(n))

        for x in li: 
            b += int(x)
            if x != '0': a = (a * 10 + int(x))
        
        print(a, b)
        return b * a