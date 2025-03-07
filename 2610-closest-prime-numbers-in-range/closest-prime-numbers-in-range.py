class Solution:
    def closestPrimes(self, l: int, r: int) -> List[int]:
        ip = [True] * (r + 1)
        ip[0] = ip[1] = False
        
        for i in range(2, int(r**0.5) + 1):
            if ip[i]:
                for j in range(i * i, r + 1, i): ip[j] = False

        ps = [i for i in range(l, r + 1) if ip[i]]
        if len(ps) < 2: return [-1, -1]

        d = 2 << 32
        p = [-1, -1]

        for i in range(len(ps) - 1):
            de = ps[i + 1] - ps[i]
            if de < d: d, p = de, [ps[i], ps[i + 1]]

        return p