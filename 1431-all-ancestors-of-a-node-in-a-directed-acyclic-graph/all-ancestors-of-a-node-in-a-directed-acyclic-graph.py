class Solution:
    def dfs(self, g, p, cur, res, visited):
        visited[cur] = True

        for d in g[cur]:
            if visited[d] == False:
                res[d].append(p)
                self.dfs(g, p, d, res, visited)


    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [[] for _ in range(n)]
        g = [[] for _ in range(n)]
        
        for e in edges:
            g[e[0]].append(e[1])
        
        for i in range(n):
            self.dfs(g, i, i, res, [False] * n)
        
        for i in range(n):
            res[i].sort()
        
        return res