class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = sorted(nums)

        prod = 1
        prod *= (l.pop(-1) - 1)
        prod *= (l.pop(-1) - 1)

        return prod
        