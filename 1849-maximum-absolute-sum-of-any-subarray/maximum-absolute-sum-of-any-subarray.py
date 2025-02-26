class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        return max(list(accumulate(nums, initial=0))) - min(list(accumulate(nums, initial=0)))