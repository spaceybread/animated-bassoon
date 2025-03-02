class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ma = {}
        for a in nums1:
            e, v = a[0], a[1]
            ma[e] = v
        for a in nums2:
            e, v = a[0], a[1]
            if e not in ma: ma[e] = v
            else: ma[e] += v

        return [[e, ma[e]] for e in sorted(ma.keys())]         