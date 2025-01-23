class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rs, cs = set(), set()

        for i in range(len(grid)):
            if sum(grid[i]) > 1:
                print(sum(grid[i]))
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        rs.add((i, j))
        
        for j in range(len(grid[0])):
            s = 0
            l = []
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    s += 1
                    l.append((i, j))
            
            if s > 1:
                for c in l:
                    cs.add(c)
        print(rs)
        print(cs)
        return len(cs.union(rs))