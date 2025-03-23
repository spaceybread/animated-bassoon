class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # this is just dijkstra's 
        # i dont want to write it myself
        g = defaultdict(list)
        for v,w,t in roads:
            g[v].append((w,t))
            g[w].append((v,t))
        
        MOD = 10**9 + 7
        
        h = [(0, 0, -1)]
        di = defaultdict(lambda : float('inf'))
        c = Counter()
        c[-1] = 1
        while h:
            d, v, p = heappop(h)
            if di[v] < float('inf'):
                if di[v] == d: c[v] = (c[v] + c[p])%MOD
                continue
            di[v] = d
            c[v] = c[p]
            for w, t in g[v]: heappush(h, (d + t, w, v))
        return c[n - 1]