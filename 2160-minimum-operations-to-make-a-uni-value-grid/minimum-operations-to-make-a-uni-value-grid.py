class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        li = sorted([n for r in grid for n in r])
        mod = li[0] % x
        for n in li:
            if n % x != mod: return -1
        mid = li[len(li) // 2]
        return sum(abs(n - mid) // x for n in li)

