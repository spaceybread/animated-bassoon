class Solution:
    def maximumCandies(self, cds: List[int], k: int) -> int:
        l, r, out = 1, max(cds), 0

        while l <= r:
            m = (l + r) // 2
            cc = sum(c // m for c in cds)

            if cc >= k:
                out = m
                l = m + 1
            else: r = m - 1
        return out