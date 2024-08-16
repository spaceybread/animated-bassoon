class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mi, ma = 10**4 + 1, -1 * (10**4 + 1)
        md = 0
        for l in arrays:
            md = max(md, max(ma - l[0], l[-1] - mi))
            mi = min(mi, l[0])
            ma = max(ma, l[-1])

        return md