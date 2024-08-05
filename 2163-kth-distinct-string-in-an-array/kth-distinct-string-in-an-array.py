class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hm = {}

        for a in arr:
            if a in hm:
                hm[a] += 1
            else:
                hm[a] = 1
        
        for a in arr:
            if hm[a] == 1:
                k -= 1
            
            if k == 0:
                return a
        
        return ""