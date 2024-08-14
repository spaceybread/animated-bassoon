class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n, l, r = len(nums), 0, nums[-1] - nums[0]

        def count(dist):
            c, j = 0, 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= dist:
                    j += 1
                    c += j - i - 1
            return c
        
        while l < r:
            m = (l + r) // 2
            if count(m) < k:
                l = m + 1
            else:
                r = m
        
        return l