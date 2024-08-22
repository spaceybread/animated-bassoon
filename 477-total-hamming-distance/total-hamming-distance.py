class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        a = 0
        for i in range(2**5):
            c = 0
            for j in range(len(nums)):
                c += (nums[j] >> i & 1)
            a += (len(nums) - c) * c
        return a
