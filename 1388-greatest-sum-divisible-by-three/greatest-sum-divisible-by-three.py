class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        @cache
        def dpdp(i, k):
            if i < 0: return 0 if k == 0 else -100000000
            return max(nums[i] + dpdp(i - 1, (k - nums[i]) % 3), dpdp(i - 1, k))
        
        return max(0, dpdp(len(nums) - 1, 0))