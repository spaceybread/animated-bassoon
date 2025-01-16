class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1) % 2, len(nums2) % 2
        r = 0

        for n in nums1:
            for i in range(n2):
                r ^= n
        for n in nums2:
            for i in range(n1):
                r ^= n
        
        return r