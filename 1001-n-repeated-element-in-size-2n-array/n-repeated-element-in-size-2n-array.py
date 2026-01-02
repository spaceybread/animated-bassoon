class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        import random

        seen = set()
        while True:
            idx = random.choice(list(range(0, len(nums))))
            a = nums[idx]
            if a in seen: return a
            seen.add(a)
            del nums[idx]
