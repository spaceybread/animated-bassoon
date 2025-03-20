class Solution:
    def minimumCost(self, n: int, es: List[List[int]], qs: List[List[int]]) -> List[int]:
        out = []
        map = defaultdict(list)
        root = {i:i for i in range(n)}
        group = [0] * n
        ct = {i:(1<<32)-1 for i in range(n)}

        def f(a):
            if a != root[a]: return f(root[a])
            else: return a

        for a, b, w in es:
            ct[a] &= w
            ct[b] &= w
            ra, rb = f(a), f(b)

            if ra != rb:
                if group[ra] >= group[rb]:
                    root[rb] = ra
                    group[ra] += 1
                    ct[ra] = ct[ra] & w & ct[rb]
                else:
                    root[ra] = rb
                    group[rb] += 1
                    ct[rb] = ct[ra] & w & ct[rb]

            else:
                ct[ra] &= w
            
        
        for frm, dst in qs:
            ra, rb = f(frm), f(dst)
            if ra != rb: out.append(-1)
            else: out.append(ct[ra])

        return out

        