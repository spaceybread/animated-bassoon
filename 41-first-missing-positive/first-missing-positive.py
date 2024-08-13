class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = sorted(nums)
        c = 1 

        for a in n:
            if a == c:
                c += 1
        
        return c