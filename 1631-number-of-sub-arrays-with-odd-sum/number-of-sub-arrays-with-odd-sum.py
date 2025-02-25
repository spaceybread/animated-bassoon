class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ps, o, e, out = 0, 0, 1, 0
        
        for a in arr:
            ps += a
            if ps % 2 == 1: 
                out += e
                o += 1
            else:
                out += o
                e += 1
        
        return out % (10**9 + 7)