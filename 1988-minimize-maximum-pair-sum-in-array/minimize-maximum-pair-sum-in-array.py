class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ns, n = sorted(nums), len(nums)
        a, b = ns[: n // 2], ns[n // 2 :][::-1]
        m = -1
        for i in range(len(a)): m = max(m, a[i] + b[i])
        return m

