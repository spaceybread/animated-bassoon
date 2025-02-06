class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        return 4 * sum((v - 1) * v for v in Counter(map(prod, combinations(nums, 2))).values())
