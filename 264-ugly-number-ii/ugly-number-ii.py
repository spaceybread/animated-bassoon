class Solution:
    def nthUglyNumber(self, n: int) -> int:
        he, vis = [1], set()
        vis.add(1)
        f = [2, 3, 5]
        cur = 0

        for i in range(n):
            cur = heapq.heappop(he)
            for num in f:
                new = cur * num

                if new not in vis:
                    vis.add(new)
                    heapq.heappush(he, new)
        
        return cur

        
