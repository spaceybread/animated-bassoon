class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        x, s, a = Counter(nums), list(set(nums)), 0
        for n in s: a += (x[n] * (x[n] - 1)) // 2
        return a
