class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        l = len(nums)
        dp = [0] * l
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[2] + nums[0]
        for i in range(3, l):  dp[i] = max(dp[i - 2], dp[i - 3])  + nums[i]
        return max(dp[l - 1], dp[l - 2])