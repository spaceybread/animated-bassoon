class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        li = defaultdict(int)
        ys = set()
        for p in points: 
            ys.add(p[1])
            li[p[1]] += 1

        ys = sorted(list(ys))
        
        out, lol = 0, 0

        for xc in li.values():
            if xc <= 1: continue
            a = (xc * (xc - 1)) // 2
            out += a
            lol += a**2
    
        return ((out ** 2 - lol) // 2) % (10**9 + 7)


        


