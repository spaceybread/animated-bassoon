# not my code, I couldn't solve it but I don't want to miss my streak

class Solution:
    def maxPoints(self, grid: List[List[int]], qs: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(qy):
            o = 0
            while mh and mh[0][0] < qy:
                curVal, i, j = heapq.heappop(mh)
                o += 1
            
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in v:
                        heapq.heappush(mh, (grid[ni][nj], ni, nj))
                        v.add((ni, nj))
            
            return o

        qs = sorted(enumerate(qs), key=lambda x: x[1])

        mh = [(grid[0][0], 0, 0)]
        heapq.heapify(mh)
        v = set()
        v.add((0, 0))

        ct = 0
        
        out = [0] * len(qs)
        for idx, qy in qs:
            ct += bfs(qy)
            out[idx] = ct

        return out