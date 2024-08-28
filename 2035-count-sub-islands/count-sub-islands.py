class Solution:
    def dfs(self, r, c, grid1, grid2):
        if r < 0 or r >= self.R or c < 0 or c >= self.C or grid2[r][c] == 0: return True
        grid2[r][c] = 0
        if grid1[r][c] == 0: 
            self.isSub = False
        for d1, d2 in self.D: self.dfs(r + d1, c + d2, grid1, grid2)
        return self.isSub
        

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if not grid1 or not grid1[0]: return 0
        if not grid2 or not grid2[0]: return 0
        self.R, self.C, self.D, self.IC = len(grid1), len(grid1[0]), [(1, 0), (-1, 0), (0, 1), (0, -1)], 0

        for i in range(self.R):
            for j in range(self.C):
                if grid2[i][j] == 1:
                    self.isSub = True
                    if self.dfs(i, j, grid1, grid2): self.IC += 1
        
        return self.IC


