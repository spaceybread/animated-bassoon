class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        m, out, i = 0, 0, 0
        for j in range(len(nums)): 

            while((m & nums[j]) != 0):
                m ^= nums[i]  
                i += 1
            m |= nums[j]
            out = max(out, j - i + 1)
        
        return out