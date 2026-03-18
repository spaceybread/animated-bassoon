class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        ng = [[0 for x in range(m)] for y in range(n)]
        ng[0][0] = grid[0][0]

        
        for i in range(n):
            if i != 0: ng[i][0] = ng[i - 1][0] + grid[i][0]

            for j in range(1, m):
                s = ng[i][j - 1] + grid[i][j]
                if i != 0: 
                    s += ng[i - 1][j]
                    s -= ng[i - 1][j - 1] 
                ng[i][j] = s    
        
        out = 0
        for x in ng: out += sum([0 if l > k else 1 for l in x])

        return out
