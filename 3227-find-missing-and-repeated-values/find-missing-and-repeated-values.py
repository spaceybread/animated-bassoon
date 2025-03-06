class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s, r = [], -1
        n = len(grid)
        n2 = n**2
        m = (n2 * (n2 + 1)) // 2
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] in s:
                    r = grid[i][j]
                else:
                    s.append(grid[i][j]) 
        return [r, m - sum(s)]