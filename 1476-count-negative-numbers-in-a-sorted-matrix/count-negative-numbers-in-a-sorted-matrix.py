class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i, j, n, s = len(grid) - 1, 0, len(grid[0]), 0
        while i >= 0 and j < n:
            if grid[i][j] < 0: s, i = s + n - j, i - 1
            else: j += 1
        return s
