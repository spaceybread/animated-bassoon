class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        c = Counter(i - nums[i] for i in range(len(nums)))
        r = len(nums) * (len(nums) - 1)

        for a in c.values():
            if a > 1: r -= (a * (a - 1))
        
        return r // 2