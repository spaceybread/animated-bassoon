class Solution:
    def dfs(self, n, idx, vis, st):
        vis[idx] = True
        for i in range(n): 
            if not vis[i]: 
                if st[idx][0] == st[i][0] or st[idx][1] == st[i][1]: self.dfs(n, i, vis, st)

    def removeStones(self, stones: List[List[int]]) -> int:
        g, n, vis = 0, len(stones), [False] * len(stones)

        for i in range(n):
            if not vis[i]:
                g += 1
                self.dfs(n, i, vis, stones)
        
        return n - g