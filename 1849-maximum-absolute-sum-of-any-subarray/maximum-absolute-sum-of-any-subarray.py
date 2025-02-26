class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ps = [0]
        for a in nums: ps.append(a + ps[-1])
        return max(ps) - min(ps)