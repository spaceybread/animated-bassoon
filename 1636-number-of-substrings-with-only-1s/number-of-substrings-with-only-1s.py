class Solution:
    def numSub(self, s: str) -> int:
        c, a = 0, 0
        for i in s:
            if i == '1': c += 1
            else: 
                a += (c * (c + 1)) // 2 
                c = 0
        else: a += (c * (c + 1)) // 2 

        return a % (10**9+7) 