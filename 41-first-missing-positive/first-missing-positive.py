class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = {}
        for a in nums:
            d[a] = True
        
        c = 1

        while True:
            if d.get(c) == None:
                return c
            c += 1
