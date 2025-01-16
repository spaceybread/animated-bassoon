from functools import reduce

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        return reduce(lambda r, x: r ^ x, [n for n in nums1 for _ in range(len(nums2) % 2)] + [n for n in nums2 for _ in range(len(nums1) % 2)], 0)
