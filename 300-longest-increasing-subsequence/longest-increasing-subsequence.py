class Solution:
    def lengthOfLIS(self, a: List[int]) -> int:
        n = len(a)
        best = [1] * n

        for i in range(1, n):
            for p in range(0, i):
                if a[i] > a[p]: best[i] = max(best[i], best[p] + 1)

        return max(best)