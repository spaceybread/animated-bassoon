class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = sorted(nums)
        return (l.pop(-1) - 1) * (l.pop(-1) - 1)
        