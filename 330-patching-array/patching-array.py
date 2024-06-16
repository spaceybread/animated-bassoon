class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        m, r, i = 1, 0, 0
        while m <= n:
            if i < len(nums) and nums[i] <= m:
                m, i = m + nums[i], i + 1
            else:
                m, r = m*2, r + 1
        return r