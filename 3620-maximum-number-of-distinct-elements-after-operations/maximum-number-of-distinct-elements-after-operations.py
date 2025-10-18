class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        ns = sorted(nums)

        out = 0
        c = - (2**32)

        for n in ns: 
            cu = max(c + 1, n - k)
            if cu <= n + k: 
                out += 1
                c = cu
        return out     
