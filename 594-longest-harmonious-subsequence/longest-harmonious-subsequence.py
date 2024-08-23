class Solution:
    def findLHS(self, nums: List[int]) -> int:
        k, c = Counter(nums), 0
        
        for ke in k:
            if (ke + 1) in k:
                c = max(c, k[ke] + k[ke + 1])
        
        return c
