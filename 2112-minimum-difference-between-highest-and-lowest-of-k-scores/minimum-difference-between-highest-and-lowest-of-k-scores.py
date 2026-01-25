class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ns, n = sorted(nums), len(nums)
        if k == 1: return 0
        m = max(nums) + 1
        print(ns)
        for i in range(n - k + 1): 
            print(ns[i + k - 1], ns[i])
            m = min(m, ns[i + k - 1] - ns[i])
        return m