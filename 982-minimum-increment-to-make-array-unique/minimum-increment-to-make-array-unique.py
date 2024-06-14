class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        m = 0
        c = 0

        for n in nums:
            m = max(m, n)
            c += m - n
            m += 1
        return c